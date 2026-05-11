from django.shortcuts import render
import os
import subprocess

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
@login_required(login_url='/users/login/')
def index(request):
    return render(request, 'welcome.html')
