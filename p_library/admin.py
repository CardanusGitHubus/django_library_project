from dataclasses import field
from django.contrib import admin

from .models import Author, Book, Publisher, Reader

# Register your models here.
# admin.site.register(Author)
# admin.site.register(Book)


# class BookInline(admin.TabularInline):
#     model = Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    @staticmethod
    def author_full_name(obj):
        if obj.author is not None:
            return obj.author.full_name
        else:
            return "no author"

    @staticmethod
    def publisher_name(obj):
        if obj.publisher is not None:
            return obj.publisher.name
        else:
            return "no publisher"
    list_display = ('title', 'author_full_name',
                    'publisher_name', 'copy_count')
    # exclude = ('copy_count',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    # @staticmethod
    # def book_list(obj):
    #     return obj.book_publisher.all()

    # list_display = ('name', 'book_list')
    # fields = ('name', 'book_list')
    # inlines = [
    #     BookInline,
    # ]
    # list_select_related = ('book_publisher',)
    pass


@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    # list_display = ('name', 'get_books')
    pass
