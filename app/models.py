from django.db import models


# Create your models here.
# 表1、发布者(主表)
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(unique=True, max_length=20)
    password = models.CharField(max_length=20)
    nickname = models.CharField(max_length=20)
    sex = models.CharField(max_length=4)
    signature = models.CharField(max_length=80)  # 个性签名
    role = models.IntegerField()  # 角色，0为普通用户，1为歌手
