from django.contrib import admin
from .models import Book, Student, Issue

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'published_date')
    search_fields = ('title', 'author', 'isbn')
    list_filter = ('author', 'published_date')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'department', 'roll_no')
    search_fields = ('name', 'email', 'roll_number')
    list_filter = ('department', 'year')


@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ('student', 'book', 'issue_date', 'return_date')
    search_fields = ('student__name', 'book__title')
    list_filter = ('issue_date', 'return_date')
