from django.db import models

from Django_Videos.utils.base_model import BaseModel


# Create your models here.


class VideoModel(BaseModel):
    """视频的模型类"""
    title = models.CharField('视频标题', max_length=64)
    # 播放时长精确到秒
    running_time = models.CharField('播放时长', max_length=10, blank=True, null=True)
    # FileField 类型的对象有三个很重要的属性： video_file.name代表文件，video_file.path代表文件，video_file.url代表访问地址
    video_file = models.FileField('原始视频文件', max_length=100)
    # 用户上传一个原始的视频文件之后，服务器自动生成视频预览图片文件。
    video_icon = models.CharField('视频预览图片路径', max_length=100, blank=True, null=True)
    running_count = models.IntegerField('视频播放次数', default=0)
    # 在视频上传之后：video_icon，running_time都由代码生成的，
    is_success = models.BooleanField('是否发布成功', default=False)  # 默认为0，表示不成功， 1：表示成功
    remark = models.CharField('视频描述', max_length=1024, blank=True, null=True)
    user = models.ForeignKey('users.UserModel', related_name='videos_list', on_delete=models.CASCADE,
                             verbose_name='视频所属用户')

    class Meta:
        db_table = 't_videos'
        verbose_name = '视频'
        verbose_name_plural = verbose_name
        ordering = ['id']  # 默认的排序字段

    def __str__(self):
        return self.title


class OperatorLogModel(models.Model):
    """客户端操作记录模型类"""
    ip_addr = models.CharField('客户端IP地址', max_length=65)
    method = models.CharField('客户端的请求方法', max_length=10)
    user_name = models.CharField('操作的用户', max_length=65)
    operate_time = models.DateTimeField('请求操作的时间', auto_now_add=True)
    path = models.CharField('访问路径', max_length=128)
    duration = models.IntegerField('访问视图函数的耗时，单位毫秒', default=0)
    response_type = models.CharField('响应类别', max_length=65)
    status = models.IntegerField('响应状态码', default=200)
    is_success = models.BooleanField('操作是否成功', default=False)

    class Meta:
        db_table = 't_operator_log'
        verbose_name = '客户端操作记录表'
        verbose_name_plural = verbose_name
