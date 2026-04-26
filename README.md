# Django_video

一个基于 Django 6 的个人视频上传平台（练手项目），目前已完成用户注册相关的基础能力，适合作为后续扩展登录、视频上传、播放与互动功能的起点。

## 项目简介

Django_video 旨在搭建一个「个人可维护」的视频站点后台与前端基础框架。当前版本聚焦在用户体系的第一步：注册页面、用户名唯一性校验和图形验证码生成，为后续视频业务功能打基础。

## 已实现功能

- **用户注册页面**：提供完整的注册表单（用户名、密码、手机号、邮箱、性别、验证码等）。
- **用户名唯一性校验**：通过 Ajax + Django 接口实时检测用户名是否可用。
- **图形验证码生成**：服务端动态生成验证码图片并写入 Session。
- **自定义用户模型**：基于 `AbstractUser` 扩展手机号、头像、城市、年龄等字段。
- **用户关注关系模型**：预留用户之间关注功能的数据结构。

## 技术栈

- Python 3
- Django 6.x
- MySQL（`mysqlclient`）
- Bootstrap + jQuery（前端页面与表单校验）

## 项目结构（核心）

```text
Django_video/
├── Django_Videos/       # 项目配置（settings、urls 等）
├── users/               # 用户模块（模型、视图、路由）
├── templates/           # 页面模板（如 register.html）
├── static/              # 静态资源（CSS/JS/图片）
└── manage.py
```

## 快速启动

1. 安装依赖

```bash
pip install -r requirements.txt
```

2. 配置数据库

- 在 `Django_Videos/settings.py` 中修改 MySQL 连接信息（HOST、PORT、USER、PASSWORD、NAME）。

3. 执行迁移

```bash
python manage.py makemigrations
python manage.py migrate
```

4. 启动项目

```bash
python manage.py runserver
```

5. 访问注册页

- `http://127.0.0.1:8000/users/register/`

## 后续规划（建议）

- 完善注册提交流程与验证码校验接口。
- 增加登录/注销、个人主页、头像上传。
- 新增视频上传、视频列表、详情播放与搜索。
- 增加点赞、评论、关注流等互动能力。
- 补充单元测试与部署文档（Nginx + Gunicorn + MySQL）。

---

如果你正在学习 Django，这个项目适合作为「用户系统 + 媒体业务」的综合实践模板。
