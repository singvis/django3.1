# Generated by Django 3.2 on 2021-04-27 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0003_auto_20210427_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='img',
            field=models.ImageField(upload_to='images/', verbose_name='用户头像'),
        ),
        migrations.AlterField(
            model_name='user',
            name='introduce',
            field=models.FileField(upload_to='introduce/', verbose_name='个人简历'),
        ),
    ]
