from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from project.form import RegistrationForm, EditProfileForm
from django.contrib.auth import update_session_auth_hash

from project.form import AddForm
from project.form import AddTheForm
from project.form import RemoveForm
from project.form import RemoveTheForm
from project.form import HomeForm


import sqlite3
connection = sqlite3.connect("db.sqlite3")
cursor = connection.cursor()
cursor.execute("SELECT name FROM crimes")
crime_types = cursor.fetchall()
crimes_list = []
for c in crime_types:
    for a in c:
        crimes_list.append(a)

cursor.execute("SELECT in_stock FROM items")
result = cursor.fetchall()
result_list = []
for r in result:
    for i in r:
        result_list.append(i)
stock_count = 0
for a in result_list:
    stock_count+=a

cursor.execute("SELECT name,price,in_stock FROM items")
all_columns = cursor.fetchall()
all_list = []
for a in all_columns:
    for b in a:
        all_list.append(b)
all_list2 = []
n = 3
for a in range(0,len(all_list),3):
    all_list2.append(all_list[a:n])
    n+=3
calc = []
for a in range(1,len(all_list),3):
    c = all_list[a]/all_list[a+1]
    calc.append(all_list[a-1])
    calc.append(c)
dictionary = {}
for i in range(1,len(calc),2):
    dictionary[calc[i-1]] = calc[i]
sorted_d = sorted((value, key) for (key,value) in dictionary.items())
popular_list = []
for a in reversed(sorted_d):
    for b in range(0,len(a),2):
        popular_list.append(a[b-1])
top_four_items = popular_list[:4]
top_top_four = []
for b in top_four_items:
    for a in range(len(all_list)):
        if b == all_list[a]:
            top_top_four.append(all_list[a])
            top_top_four.append(all_list[a+1])
            top_top_four.append(all_list[a+2])

cursor.execute("SELECT name,in_stock FROM items")
items_columns = cursor.fetchall()
items_list = []
for i in items_columns:
    for a in i:
        items_list.append(a)

cursor.execute("SELECT budget_total FROM Budget")
budg = cursor.fetchall()
budget_list = []
for a in budg:
    for b in a:
        budget_list.append(b)


class HomeView(TemplateView):
    template_name = 'project/home.html'
    def get(self, request):
        form = HomeForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            answer = form.cleaned_data['post']
            form = HomeForm()
        args = {'form':form}
        return render(request, self.template_name, args)

class AddItem(TemplateView):
    template_name = 'project/add.html'
    def get(self,request):
        formed = AddForm()
        return render(request, self.template_name, {'formed':formed})
    def post(self, request):
        formed = AddForm(request.POST)
        if formed.is_valid():
            answer = formed.cleaned_data['item']
            post = formed.save(commit=False)
            post.user = request.user
            post.save()
            formed = AddForm()
        return render(request, self.template_name,{'formed':formed})

class AddTheItems(TemplateView):
    template_name = 'project/add_answers.html'
    def get(self,request):
        form = AddTheForm()
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = AddTheForm(request.POST)
        if form.is_valid():
            item_choice = form.cleaned_data['item_choice']
            many_items = form.cleaned_data['many_items']
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            form = AddTheForm()
        return render(request, self.template_name, {'form':form})

class RemoveItem(TemplateView):
    template_name = 'project/remove.html'
    def get(self,request):
        formed = RemoveForm()
        return render(request, self.template_name, {'formed':formed})
    def post(self, request):
        formed = RemoveForm(request.POST)
        if formed.is_valid():
            answer = formed.cleaned_data['item']
            post = formed.save(commit=False)
            post.user = request.user
            post.save()
            formed = RemoveForm()

        args = {'formed':formed, 'answer':range(answer)}
        return render(request, self.template_name, args)

class RemoveTheItems(TemplateView):
    template_name = 'project/remove_answers.html'
    def get(self, request):
        form = RemoveTheForm()
        return render(request, self.template_name, {'form':form})
    def post(self, request):
        form = RemoveTheForm(request.POST)
        if form.is_valid():
            item_choice = form.cleaned_data['item_choice']
            many_items = form.cleaned_data['many_items']
            crime_type = form.cleaned_data['crime_type']
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            form = RemoveTheForm()
        return render(request, self.template_name, {'form':form})
def output_budget(request):
    budget = budget_list
    return render(request, 'project/budget.html', {'budget':budget})
def profile(request):
    args = {'user':request.user}
    return render(request, 'project/profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/project/profile/')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form':form}
        return render(request, 'project/edit_profile.html', args)

def stock_output(request):
    all_list1 = all_list2
    items = items_list
    crimes = crimes_list
    stock_total = stock_count
    pop_list = popular_list
    four = top_top_four
    args = {'top_four':four,'popular':pop_list,'all':all_list1, 'it':items, 'crim':crimes,'stock_count':stock_total}
    return render(request, 'project/output.html', args)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/project/home/')
    else:
        form = RegistrationForm()
    args = {'form': form}
    return render(request, 'project/reg_form.html', args)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/project/profile/')
        else:
            return redirect('/project/password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form':form}
        return render(request, 'project/change_password.html', args)
