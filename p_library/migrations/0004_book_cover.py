# Generated by Django 4.0.3 on 2022-04-15 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0003_alter_book_detail_copy_borrowed'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(default='book_covers/default_book_cover.jpg', upload_to='book_covers'),
        ),
    ]