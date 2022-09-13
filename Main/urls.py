from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.HomePage.as_view(), name='home_page'),
    path('home/', views.HomePage.as_view(), name='home_page_alternative'),
    path('create-note/', views.CreateNote.as_view(), name='create_note'),
    path('login/', views.LoginUser.as_view(), name='login_page'),
    path('register/', views.RegisterUser.as_view(), name='register_page'),
    path('logout/', LogoutView.as_view(), name='Logout'),
    path('note/<int:pk>', views.ViewNote.as_view(), name='view_note'),
    path('delete-note/<int:pk>', views.DeleteNote.as_view(), name='delete_note')
]