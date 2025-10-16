from django.db import models
from django.utils import timezone

# Book model
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.title} by {self.author}"


# Student model
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20, null=True, blank=True)

    department = models.CharField(max_length=100)
    year = models.IntegerField()
    email = models.EmailField()
   

    def __str__(self):
        return f"{self.name} ({self.roll_no})"

# Issue model (relation between Book & Student)
class Issue(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateField(default=timezone.now)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.book.title} issued to {self.student.name}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name