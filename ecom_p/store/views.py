from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from.models import category,product
# Create your views here.
def index(request):
  return render(request,'index.html')
@login_required(login_url='login')
def collections(request):
  cat=category.objects.filter(status=0)
  
  return render(request,'collections.html',{"cati":cat})

def loginn(request):
  if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
          auth.login(request,user)
          return redirect('home')
        else:
          messages.error(request, 'login invalid.')
          return redirect('login')

          
  return render(request,'login.html')



def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Basic validation
        if not username or not email or not password:
            messages.error(request, 'All fields are required.')
            return redirect('register')

        # Check if username or email already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already taken.')
            return redirect('register')

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, 'Registration successful!')
        return redirect('login')  # Replace 'home' with your homepage URL name

    return render(request, 'register.html')
  
  
  
  
  
  
  
  
def logout(request):
  auth.logout(request)
  return redirect('login')





    
def collectionsview(request,slug):
  if(category.objects.filter(slug=slug,status=0)):
    pdt=product.objects.filter(c__slug=slug)
  else:
    messages.error(request,"no products to show")
    return redirect('collections') 
  return render(request, 'product.html',{'pdct':pdt})
    
    
    
    
    
    
    
    
    
    
def productview(request,cate_slug,prod_slug):
  if(category.objects.filter(slug=cate_slug,status=0)):
    if(product.objects.filter(slug=prod_slug,status=0)):
      a=product.objects.filter(slug=prod_slug,status=0)
    
    else:
      messages.error(request,"no products to show")
      return redirect('collections')
  
  
  else:
      messages.error(request,"no category to show")
      return redirect('collections')  
  
  return render(request, 'productview.html',{'a':a})
    