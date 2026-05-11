from django.shortcuts import render
import os
import subprocess

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from videos.models import VideoModel


# Create your views here.
@login_required(login_url='/users/login/')
def index(request):
    return render(request, 'welcome.html')


class Video(LoginRequiredMixin, View):

    def post(self, request):
        """上传视频的函数"""
        title = request.POST['title']
        remark = request.POST['remark']
        video_file = request.FILES['video']

        # 代码执行到此位置，表单中文件的上传已经成功！
        if not video_file:
            return HttpResponse('没有选中任何文件')
        # 处理：1、保存到数据库    2、获取视频播放市场以及视频的预览图片
        current_user = request.user
        VideoModel.objects.create(title=title, remark=remark, video_file=video_file, user=current_user)
