# Generated by Django 3.2 on 2021-05-15 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('address', models.CharField(max_length=256)),
                ('city', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='书名', max_length=256)),
                ('authors', models.ManyToManyField(help_text='作者', to='books.Author', verbose_name='作者')),
                ('publisher', models.ForeignKey(help_text='出版社', on_delete=django.db.models.deletion.CASCADE, to='books.publisher', verbose_name='出版社')),
            ],
        ),
    ]
