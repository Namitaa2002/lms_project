from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('books/', views.books, name="books"),
    path('students/', views.students, name="students"),
    path('contact/', views.contact, name="contact"),
    path('login/', views.login_page, name="login"),
    path('signin/', views.signin, name="signin"),
    path("signup/", views.signup, name="signup"),
    path("students/", views.students, name="students"),
    path("books/", views.books, name="books"),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
]