from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from project.models import AddItem
from project.models import AddTheItems
from project.models import RemoveItem
from project.models import RemoveTheItems
from project.models import Post


import sqlite3
connection = sqlite3.connect("db.sqlite3")
cursor = connection.cursor()
cursor.execute("SELECT name FROM crimes")
crime_types = cursor.fetchall()
crimes_list = []
for c in crime_types:
    for a in c:
        crimes_list.append(a)

cursor.execute("SELECT name FROM items")
items_columns = cursor.fetchall()
items_list = []
for i in items_columns:
    for a in i:
        items_list.append(a)

class HomeForm(forms.ModelForm):
    post = forms.CharField()
    class Meta:
        model = Post
        fields=(
            'post',
        )

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password'
        )

class AddForm(forms.ModelForm):
    item = forms.IntegerField(label='How many different items were bought?')
    class Meta:
        model = AddItem
        fields = (
            'item',
        )
class AddTheForm(forms.ModelForm):
    CHOICES = (('','Choose an item:'),)
    for i in items_list:
        CHOICES += ((str(i),str(i)),)
    item_choice = forms.ChoiceField(widget=forms.Select,choices=CHOICES, label="Which item was it?")
    many_items = forms.IntegerField(label="How many of this item were bought?")

    class Meta:
        model = AddTheItems
        fields = (
            'item_choice',
            'many_items',
        )

class RemoveForm(forms.ModelForm):
    item = forms.IntegerField(label='How many different items were given away?')
    class Meta:
        model = RemoveItem
        fields = (
            'item',
        )
class RemoveTheForm(forms.ModelForm):
    CHOICES = (('','Choose an item:'),)
    CHOICES2 = (('','Choose a crime type:'),)
    for i in items_list:
        CHOICES += ((str(i),str(i)),)
    item_choice = forms.ChoiceField(widget=forms.Select(),choices=CHOICES, label="Which item was it?")
    many_items = forms.IntegerField(label="How many of this item were given away?")
    for a in crimes_list:
        CHOICES2 += ((str(a), str(a)),)
    crime_type = forms.ChoiceField(widget=forms.Select(),choices=CHOICES2, label="Which crime type was it given away to?")
    class Meta:
        model = RemoveTheItems
        fields = (
            'item_choice',
            'many_items',
            'crime_type',
        )
