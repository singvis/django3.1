# !/usr/bin/env python3
# --*-- coding=utf-8 --*--


from django.db import models

# class Publisher(models.Model):
#     """
#     出版社
#     """
#     name = models.CharField(max_length=256)
#     address = models.CharField(max_length=256)
#     city = models.CharField(max_length=256)
#
#     def __str__(self):
#         return self.name


# class Author(models.Model):
#     """
#     作者
#     """
#     name = models.CharField(max_length=256)
#     email = models.EmailField()
#
#     def __str__(self):
#         return self.name


# class Book(models.Model):
#     """
#     书名
#     """
#     title = models.CharField(max_length=256, help_text="书名")
#     # 作者和书是多对多关系
#     authors = models.ManyToManyField(Author, verbose_name="作者", help_text="作者")
#     # 一本书只能被一家出版社出版，出版社可以出多本书
#     publisher = models.ForeignKey(Publisher, verbose_name="出版社", help_text="出版社", on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.title
