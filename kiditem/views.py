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
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {'products': products, 'categories': categories}
    return render(request, 'index.html', context)





def notice(request): 
    question_list = Post.objects.all()
    # 입력 파라미터
    page = request.GET.get('page','1')
     
    # 페이징처리
    paginator = Paginator(question_list, 3)
    page_obj = paginator.get_page(page)
    return render(request, 'notice.html',{'question_list':page_obj})

def notice_detail(request, pk):
    categories = Category.objects.all()
    post = Post.objects.get(pk=pk)
    context = {"post": post, "categories":  categories}
    return render(request, 'notice_detail.html', context)

def product_detail(request, pk):#category.html에서 product.pk로 urls.py로 가서는 pk로 받아서 여기로 가져옴,pk =5 갈비
    categories = Category.objects.all()#카테로리 전체 한국 일본 중국 요리 전부
    product = Product.objects.get(pk=pk)#product에서 pk가 category.html에서 받아온 product.pk 곧 url에서 pk로 받은 
    #곧 n번째 pk =5 요리 예 갈비인 product objects - 갈비 가격 수량 등
    category = Category.objects.get(pk=product.category.pk)
    #category pk는 1,2,3, 한국요리, 일본요리,중국요리 중 하나인데 
    #product.category.5는 ? category.5는 product.pk가 5인 category라면 말이 된다. ????
    
    context = {"product": product, "category": category, "categories": categories}
    return render(request, 'product_detail.html', context)
