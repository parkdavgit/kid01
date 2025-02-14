from django.test import TestCase

# Create your tests here.
Owner: ubuntu/4444
User : parkav/4444

Cart view
Order always add?
next step to add delivery ADDRESS
next step to add payment 

def delete_order(request, pk): #user.pk =1 or 16 david
    
    user = request.user#david
    orders = Order.objects.filter(user=user)
    
    if request.method == 'POST':
        for i in orders:
            od= Order.objects.filter(user=user)
        od.delete()
        return redirect('shop:Norder_list', user.pk)      

def delete_order(request, pk): #user.pk =1 or 16 david
    
    user = request.user#david
    order = Order.objects.filter(user=user)
   
    if request.method == 'POST':
        pk =int(request.POST.get('product.products.id'))
        
        product = Product.objects.filter(pk=pk)

        order = Order.objects.filter(user=user, products__in=product)
        order.delete()
        return redirect('shop:Norder_list', user.pk)              