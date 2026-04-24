from django.db import models
from django.contrib.auth.models import AbstractUser
from Django_Videos.utils.base_model import BaseModel


# create your models here
class UserModel(AbstractUser, BaseModel):
    """用户模型类：继承了Django自带的AbstractUser，也把一些字段继承过来了"""
    phone = models.CharField(max_length=11, unique=True, verbose_name='手机号')
    real_name = models.CharField(max_length=20, null=True, blank=True, verbose_name='用户真实名字')
    nationality = models.CharField(max_length=20, null=True, blank=True, verbose_name='国籍')
    city = models.CharField(max_length=20, null=True, blank=True, verbose_name='城市')
    # 用户头像图片，本身的文件，还是存放在指定的目录
    user_icon = models.FileField(max_length=200, null=True, blank=True,
                                 verbose_name='用户头像，将路径存放到数据库字段中')
    age = models.IntegerField(null=True, blank=True, verbose_name='年龄')
    sex = models.CharField(max_length=4, null=True, blank=True, verbose_name='性别')

    class Meta:
        db_table = 'user'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.username
