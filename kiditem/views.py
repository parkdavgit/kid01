from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import F
from .models import Product, Post, Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Product,Category,Point, Cart, Order, Post , Address
from django.utils import timezone
from .forms import OrderForm, AddressForm


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
                    return redirect('cart', user.pk)


            Cart.objects.create(user=user, products=product, quantity=quantity)
            messages.success(request, '장바구니 등록 완료')
            return redirect('cart', user.pk)

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
                #return redirect('Norder_list')
                return redirect('Norder_list', user.pk)
            else:
                form = OrderForm(initial=initial)

            context = {'user': user, 'cart': cart, 'categories': categories, 'product':product}
            #context = {'product':product}
            return render(request, 'Norder_list.html', context)
        
#def checkout(request, pk):#user.pk =1 or 16
def checkout(request):#user.pk =1 or 16
    user = request.user
    order = Order.objects.get(user=request.user)
    
    #initial = {'street_address': address.street_address, 'apartment_address': address.apartment_address, 'zip': address.zip}

    if request.method == 'POST':
        #address= Address.objects.get(user=request.user)
        form = AddressForm(request.POST)
        if form.is_valid():
            address= Address()
            address.street_address = form.cleaned_data['street_address']
            address.apartment_address = form.cleaned_data['apartment_address']
            address.zip = form.cleaned_data['zip']
            #street_address = request.POST.get('street_address')

            #apartment_address = request.POST.get('apartment_address')
       #address.country = request.country
            #zip = request.POST.get('zip')
        #address_type=request.POST.get('address_type')
            address.save()
        #address= Address.objects.create(user=request.user, street_address=street_address, apartment_address=apartment_address,zip=zip,address_type=address_type)
            return redirect('Norder_list', user.pk)       
        else:
            form = AddressForm()
        context = {'user': user, 'order': order}
            #context = {'product':product}
        return render(request, 'checkout.html', {'form':form})


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

#def Norder_list(request):
def Norder_list(request, pk):    
    categories = Category.objects.all()
    product = Product.objects.all()
    user = User.objects.get(pk=pk)
    #user = request.user
    orders = Order.objects.filter(user=user)
    paginator = Paginator(orders, 5)
    page = request.GET.get('page')
    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        orders = paginator.page(paginator.num_pages)
    context = {'user': user, 'orders': orders, 'categories': categories, 'product': product }
    return render(request, 'Norder_list.html', context) 

def delete_cart(request, pk): #user.pk =1 or 16 david
    
    user = request.user#david
    cart = Cart.objects.filter(user=user)#
    quantity = 0

    if request.method == 'POST':
     
        pk =int(request.POST.get('product'))
        product = Product.objects.get(pk=pk)
        for i in cart:
            if i.products == product :
                quantity =  i.quantity

        if quantity > 0 :
            product = Product.objects.filter(pk=pk)
            cart = Cart.objects.filter(user=user, products__in=product)
            cart.delete()
            return redirect('cart', user.pk)
        
def delete_order(request, pk): #user.pk =1 or 16 david
    
    user = request.user#david
    order = Order.objects.filter(user=user)#
    quantity = 0

    if request.method == 'POST':
     
        pk =int(request.POST.get('order_product'))
        order = Order.objects.get(pk=pk)
        order.delete()
        return redirect('Norder_list', user.pk)
        #for i in order:
            #if i.products == product :
                #quantity =  i.quantity

        #if quantity > 0 :
            #product = Product.objects.filter(pk=pk)
            #order = Order.objects.filter(user=user, products__in=product)
            #order.delete()
            #return redirect('Norder_list', user.pk)











        

def show_category(request, category_id):#category_id는 index에서 받아 온 숫자를 URLS에서 할당함 여기서 1 
    categories = Category.objects.all()#카테로리 전체 한국 일본 중국 요리 전부
    category = Category.objects.get(pk=category_id)#pk가 1인 object 곧 KOREAN FOOD(한국요리) 
    #products = Product.objects.filter(category=category).order_by('pub_date')#category가 category(KOREAN FOOD)인
    #product objects 할당. product에 category_id만 있지만 category에 연결된 외래키이므로 이렇게 사용가능한것같다
    # 곧 product에 category가 한국요리 전체를 products에 할당해서 쓰겠다 
    # 모든 한국요리 가격 수량 해설 등 모든 것 가짐 즉 카테로리를 한국 요리로 누르고 왔으니 그 요리 정보를 여기에 담음

    products = Product.objects.filter(category_id=category_id).order_by('pub_date')
    lank_products = Product.objects.filter(category_id=category_id).order_by('-hit')[:4]# 그 중에서 인기 순 정렬
    paginator = Paginator(products, 3)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    context = {'lank_products': lank_products, 'products': products, 'category': category, 'categories': categories}
    return render(request, 'category.html', context)#이런 context를 category.html에서 사용할 거야


