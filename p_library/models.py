# from tkinter import CASCADE
from django.db import models
from django.core.validators import MaxValueValidator


# Create your models here.
class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)

    def __str__(self):
        return self.full_name


class Publisher(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Reader(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name

    def get_books(self):
        return ", ".join([book_detail.book.title for book_detail in self.details_reader.all()])


class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    copy_count = models.SmallIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE,
                               related_name='book_author')
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE,
                                  related_name='book_publisher', null=True)
    # readers = models.ManyToManyField(
    #     Reader, through='Book_detail', through_fields=('book', 'reader'), null=True)

    def __str__(self):
        return self.title


class Book_detail(models.Model):
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name='details_book')
    reader = models.ForeignKey(
        Reader, on_delete=models.CASCADE, related_name='details_reader')
    copy_borrowed = models.SmallIntegerField(
        default=0)

    def __str__(self):
        return self.book.title
