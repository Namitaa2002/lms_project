from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('books/', views.books, name="books"),
    path('students/', views.students, name="students"),
    path('contact/', views.contact, name="contact"),

    path('login/', views.login_page, name="login"),
    path('signin/', views.signin, name="signin"),
    path('signup/', views.signup, name="signup"),
    path('signout/', views.signout, name="signout"),
]