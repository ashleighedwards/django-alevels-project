from django.urls import re_path as url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

from project.views import AddItem
from project.views import AddTheItems
from project.views import RemoveItem
from project.views import RemoveTheItems
from project.views import HomeView

urlpatterns = [
    url(r'^home/$', HomeView.as_view(), name='home'),
    url(r'^edit/$', views.edit_profile, name='edit_profile'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', LoginView.as_view(template_name='project/loginform.html'), name='login'),
    url(r'^logout/$', LogoutView.as_view(template_name='project/logoutform.html'), name='logout'),
    url(r'^output/', views.stock_output, name='output'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^password/$', views.change_password, name="change_password"),
    url(r'^remove_items/',RemoveItem.as_view(), name='remove_items'),
    url(r'^remove_answers/$', RemoveTheItems.as_view(), name="remove_answers"),
    url(r'^add_items/$', AddItem.as_view(), name='add_items'),
    url(r'^add_answers/$', AddTheItems.as_view(), name='add_answers'),
    url(r'^budget/$', views.output_budget, name='budget'),
]
