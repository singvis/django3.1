# Generated by Django 3.2 on 2021-05-10 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='用户名', max_length=32)),
                ('password', models.CharField(help_text='密码', max_length=32)),
                ('sex', models.IntegerField(blank=True, choices=[(1, '男'), (2, '女')], null=True)),
            ],
        ),
    ]
