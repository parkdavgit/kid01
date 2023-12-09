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

