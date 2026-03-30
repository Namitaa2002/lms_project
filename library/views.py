from django.shortcuts import render, redirect
from .models import Book, Student
from .forms import ContactForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, "library/home.html")


def books(request):
    books = Book.objects.all()
    return render(request, "library/books.html", {"books": books})


def students(request):
    students = Student.objects.all()
    return render(request, "library/students.html", {"students": students})


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message sent successfully!")
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, "library/contact.html", {"form": form})


# ✅ ADD THIS (your error fix)
def login_page(request):
    return render(request, "library/login.html")


def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            return render(request, "library/signup.html", {"error": "Username exists"})

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return redirect("signin")

    return render(request, "library/signup.html")


def signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("/admin/")
        else:
            return render(request, "library/signin.html", {"error": "Invalid credentials"})

    return render(request, "library/signin.html")


def signout(request):
    logout(request)
    return redirect("signin")