import random
from http.client import HTTPResponse
from io import BytesIO

from PIL import Image, ImageDraw, ImageFont
from django.db.models.expressions import result
from django.http import JsonResponse, HttpResponse
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


@require_http_methods(['GET'])
def generate_code(request):
    # 定义变量 用于画面的背景颜色 、宽、 高
    bg_color = (random.randrange(0, 200), random.randrange(0, 200), random.randrange(0, 200))
    width = 120
    height = 38
    # 创建画面对象
    im = Image.new('RGB', (width, height), bg_color)
    # 创建画笔的颜色
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪声点
    for i in range(0, 1000):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill == fill)

    # 定义验证码的备选值
    str1 = 'ABCDEFGHIJKLMNOPQRSTUVXYZ0123456789'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]

    # 绘制4个字
    # 构造字体对象 字体对象的路径：
    try:
        font = ImageFont.truetype(
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
            23
        )
    except OSError:
        font = ImageFont.load_default()
    # 构造字体的颜色
    # fontcolor = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
    draw.text((5, -3), rand_str[0], font=font,
              fill=(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
    draw.text((25, -3), rand_str[1], font=font,
              fill=(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
    draw.text((50, -3), rand_str[2], font=font,
              fill=(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
    draw.text((75, -3), rand_str[3], font=font,
              fill=(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
    # 释放画笔
    del draw
    """
        1、session在服务器端，cookie在客户端（浏览器）
        2、session默认被存在服务器的一个数据库（不是内存）
        3、session的运行依赖 session id，而 session id 是存在cookie中的
        4、session可以放在 文件，数据库或内存中都可以
        5、用户验证这种场合一般会用session
    """
    # 将图形验证码存储到session
    request.session['verify_code'] = rand_str
    # 内存文件操作
    buf = BytesIO()
    # 将图片保存在内存中 文件类型：png
    im.save(buf, 'png')
    # 将内存中的图片数据返回给客户端 MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')


@require_http_methods(['POST'])
def verify_code(request):
    """验证验证码是否正确"""
    # {'valid': True}:如果返回的是True，表示验证合法，通过
    # {'valid': False}:如果返回的是False，表示验证不合法，不通过
    result_data = {'valid': True}  # 先定义一个默认的返回参数
    code = request.POST.get('captcha')  # 接收请求参数
    # 服务器里前在前一次请求的时候就已经存放了验证码：在session中
    code2 = request.session['verify_code']
    if not code == code2:
        # 客户端的验证码写错了
        result_data['valid'] = False
    return JsonResponse(result_data)


@require_http_methods(['POST'])
def submit_register(request):
    """注册提交"""
    # 下麦代码不合理，会把密码以明文的方式存放到数据库表中
    # UserModel.objects.create()
    user = UserModel.objects.create_user(username=request.POST['username'],
                                         password=request.POST['password'],
                                         email=request.POST['email'],
                                         phone=request.POST['phone'])
    user.phone = request.POST['phone']
    user.sex = request.POST['sex']
    user.save()
    result_data = {'code': 200}
    return JsonResponse(result_data)
