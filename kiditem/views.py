from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import F
from .models import Product, Post, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Product,Category,Point, Cart, Order, Post 
from django.utils import timezone

def index(request): 
    return render(request, 'index.html')

def notice(request): 
    question_list = Post.objects.order_by('-create_at') 
    # 입력 파라미터
    page = request.GET.get('page','1')
     
    # 페이징처리
    paginator = Paginator(question_list, 3)
    page_obj = paginator.get_page(page)
    return render(request, 'notice.html',{'question_list':page_obj})
