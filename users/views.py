from http.client import HTTPResponse

from django.db.models.expressions import result
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from users.models import UserModel


# Create your views here.
@require_http_methods(['POST'])  # 设置装饰器，只允许post请求
def check_username(request):
    """验证用户名是否唯一"""
    # {'valid': True}:如果返回的是True，表示验证合法，通过
    # {'valid': False}:如果返回的是False，表示验证不合法，不通过
    result_data = {'valid': True}  # 先定义一个默认的返回参数
    un = request.POST.get('username')  # 接收请求参数
    user = UserModel.objects.filter(username=un)
    if user:
        # 已经存在一个用户名字相同的用户
        result_data['valid'] = False
    return JsonResponse(result_data)
