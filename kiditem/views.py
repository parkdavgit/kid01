from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import F
from .models import Product, Post, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Product,Category,Point, Cart, Order, Post 
from django.utils import timezone
from .forms import OrderForm


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


@login_required
def cart_or_buy(request, pk):#product.pk를 urls통해 pk로 받음 갈비
    quantity = int(request.POST.get('quantity'))#detail.html에서 선택한 quantity를 받음.
    product = Product.objects.get(pk=pk)#pk=5인 objects 갈비 가격 재고수량....
    user = request.user#login user
    categories = Category.objects.all()#
    initial = {'name': product.name, 'amount': product.price, 'quantity': quantity}#갈비 가격 그리고 카트에 담은 수
    cart = Cart.objects.filter(user=user)#user가 login한 user의 카트 objects - user, products, quantity
    order = Order.objects.filter(user=user) 
    if request.method == 'POST':
        if 'add_cart' in request.POST:
            for i in cart :
                if i.products == product:#카트에 product가 갈비가 있으면  
                    product = Product.objects.filter(pk=pk)#갈비 정보
                    Cart.objects.filter(user=user, products__in=product).update(quantity=F('quantity') + quantity)
                    messages.success(request,'장바구니 등록 완료')
                    return redirect('shop:cart', user.pk)


            Cart.objects.create(user=user, products=product, quantity=quantity)
            messages.success(request, '장바구니 등록 완료')
            return redirect('shop:cart', user.pk)

        elif 'buy' in request.POST:
            form = OrderForm(request.POST, initial=initial)
            if form.is_valid():
                order = form.save(commit=False)
                order.user = request.user
                order.amount = product.price
                order.name = product.name
                order.order_date=timezone.now()
                order.products=product
                order.number=1234
                
                order.save()
                return redirect('Norder_list', user.pk)

            else:
                form = OrderForm(initial=initial)

            context = {'user': user, 'cart': cart, 'categories': categories, 'product':product}
            #context = {'product':product}
            return render(request, 'Norder_list.html', context)

def cart(request, pk):#user.pk =1 or 16
    categories = Category.objects.all()
    user = User.objects.get(pk=pk)#user david 1111 objects
    cart = Cart.objects.filter(user=user)#david cart 
    #paginator = Paginator(cart, 10)
    #page = request.GET.get('page')
    #try:
        #cart = paginator.page(page)
    #except PageNotAnInteger:
        #cart = paginator.page(1)
    #except EmptyPage:
       #cart = paginator.page(paginator.num_pages)
    context = {'user': user, 'cart': cart, 'categories': categories}
    return render(request, 'cart.html', context)

def Norder_list(request, pk):
    categories = Category.objects.all()
    user = User.objects.get(pk=pk)
    orders = Order.objects.filter(user=user)
    paginator = Paginator(orders, 5)
    page = request.GET.get('page')
    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)
    context = {'user': user, 'orders': orders, 'categories': categories}
    return render(request, 'Norder_list.html', context)          