2023.12.08 add in index
<form action="#" method="post">
    
  {% csrf_token %}

  <input type="text" name="first_name" placeholder="First Name"><br>
  <input type="text" name="last_name" placeholder="Last Name"><br>
  <input type="email" name="email" placeholder="email"><br>
  <input type="phone" name="phone" placeholder="phone"><br>
  <input type="text" name="request" placeholder="request"><br>
  <input type="Submit">

</form>

2023.12.13 add Appointment in models
class Appointment(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    request = models.TextField(blank=True)
    sent_date = models.DateField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    accepted_date = models.DateField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.user.first_name

    class Meta:
        ordering=["-sent_date"]

add Appointment in admin
from .models import Category, Product, Post, Order, Address, Appointment
# Register your models here.
admin.site.register(Appointment)

Putty connection / change server IP in VSC / GIT push / reset servers iginx / makemigrations 

Could see Appoitment in admin ( ubuntu 4444)

2023.12.15 make appointment like notice in index link 

<div class="container my-3">
  <h3>BOOK AN APPOINTMENT</h3>
</div>

<div class="card">

<form class="form-card" method="POST" action="{% url 'appointment' %}">
    
  {% csrf_token %}

  <div class="row justify-content-between text-left">
    <div class="form-group col-sm-6 flex-column d-flex">
      <label class="form-control-label px-3">First Name<span class="text-danger">*</span></label>
      <input required type="text" id="fname" placeholder="Enter your First Name">
    </div> 
    <div class="form-group col-sm-6 flex-column d-flex">
      <label class="form-control-label px-3">Last Name<span class="text-danger">*</span></label>
      <input required type="text" id="lname" placeholder="Enter your Last Name">
    </div> 
  </div>

  <div class="row justify-content-between text-left">
    <div class="form-group col-sm-6 flex-column d-flex">
      <label class="form-control-label px-3">email<span class="text-danger">*</span></label>
      <input required type="email" id="email" placeholder="Enter your email">
    </div> 
    <div class="form-group col-sm-6 flex-column d-flex">
      <label class="form-control-label px-3">mobile<span class="text-danger">*</span></label>
      <input required type="text" id="mobile" placeholder="Enter your mobile#">
    </div> 
  </div>  

  <div class="row justify-content-between text-left">
    <div class="form-group col-sm-6 flex-column d-flex">
      <label class="form-control-label px-3">request<span class="text-danger">*</span></label>
      <input required type="text" id="request" placeholder="Enter your request">
    </div> 
    
  </div>  
<input type="Submit">
</form>
<div>
       
{% endblock contents %} 

2023.12.15 make appointment url and views.py 
url(r'^appointment/$', views.appointment, name='appointment'),
views.py 
from .models import Product,Category,Point, Cart, Order, Post , Address, Appointment
def appointment(request):
    if request.method == 'POST':
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        email=request.POST.get("email")
        mobile=request.POST.get("mobile")
        message=request.POST.get("request")

        appointment=Appointment.objects.create(
            firstname=fname,
            lastname=lname,
            email=email,
            phone=mobile,
            request=message,
        )

        appointment.save()

        messages.add_message(request, messages.SUCCESS, f"Thanks {fname} for making an appointment")

    return redirect('index') 

Add in index
{% if messages %}
<div class="card notification-card nitification-invitation">
  <div class="card-body">
  {% for message in messages %}
    <div class="card-title">{{messaga}}</div>
    {% endfor %}
  </div>
</div>
{% endif %}  

2023.12.22
Add in index
<!-- Email Contact Form -->
<div class="container py-5">

<form method="POST" action="{% url 'appointment' %}">
    
  {% csrf_token %}

  
  <div class="mb-3">
    <label for="fname" class="form-label">First Name<span class="text-danger">*</span></label><br>
    <input required type="text" name="fname" placeholder="Enter your First Name"><br>
  </div>
  <div class="mb-3">
    <label for="lname" class="form-label">Last Name<span class="text-danger">*</span></label><br>
    <input required type="text" name="lname" placeholder="Enter your Last Name"><br>
  </div>

  <div class="mb-3">
    <label for="Email" class="form-label">Email</label><br>
    <input required type="email" name="email" placeholder="Enter your email">
  </div>
  <div class="mb-3">
    <label for="Mobile" class="form-label">Mobile</label><br>
    <input required type="text" name="mobile" placeholder="Enter your mobile">
  </div>
  
  <div class="mb-3">
    <label for="message" class="form-label">Message</label><br>
    <textarea name="request" rows="5" placeholder=""></textarea>
  </div>

  <div class="mb-3">    
    <button type="submit" class="btn btn-primary">Send</button>
  </div>

</form>
<div>

2023.12.23 - Book Appointment Complete
def __str__(self):
        return self.first_name
        return self.user.first_name(error - no found user)

2023.12.27 - Manage Appointment.html
<div class="container my-3">
  <h3>{{title}}</h3>
</div>

<div class="container py-5">
  {% for app in appointments %}

  <div class="mb-3">
    {{app.firstname}}
  </div>
  <div class="mb-3">
    {{app.lastname}}
  </div>
  <div class="mb-3">
    {{app.email}}
  </div>
  <div class="mb-3">
    {{app.phone}}
  </div>
  <div class="mb-3">
    {{app.sent_date}}
  </div>
  
  <div class="mb-3">
    {{app.request}}
  </div>
  
  <hr class ="w-100"> 
  <div class="form-group">
    <input type="date" name="date" class="form-control mb-2" placeholder="dd-mm-yyyy" value=" " min="1997-01-01" max="2024-12-31">
    <input class="btn-block btn-primary form-control" type="submit" value="Accept">
  </div>


  {% endfor %}
<div>
       
{% endblock contents %} 


submit then what?
        