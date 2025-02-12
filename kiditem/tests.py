from django.test import TestCase

# Create your tests here.
Owner: ubuntu/4444
User : parkav/4444

Cart view
Order always add?
next step to add delivery ADDRESS
next step to add payment 

@login_required        
def address(request,pk):#user.pk =1 or 16
    
    user = request.user #login user
    address = Address.objects.all()
    for i in address :
        if i.user == user:
            messages.success(request,'Address already exist')
            return redirect('shop:Norder_list', user.pk)
    
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.user = user   
                      
            address.save()
            return redirect('shop:Norder_list', user.pk)
        
        else:
            return HttpResponseRedirect('index')
             
    else:
        form = AddressForm()
        context = {'user': user, 'form':form}
        return render(request, 'shop/address.html', context)
    