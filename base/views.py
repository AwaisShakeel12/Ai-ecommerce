from django.shortcuts import render, redirect, get_object_or_404
from .forms import ShippingAddressForm, ProductForm, UpdateProfileForm, UpdateProductForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import auth
from django.contrib import messages
from .models import *
from  django.db.models import Q
from django.contrib.auth.decorators import user_passes_test, login_required
from .retriver2 import chain




def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        re_enter_password = request.POST['password1']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        paypal_client_id = request.POST['paypal_client_id']
        image = request.FILES.get('image')
    


        if password == re_enter_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username already exsist')
                return redirect('register')
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email already exsist')
                return redirect('register')
            else:
                if not image:
                    image = 'profile_images/avatar.jpg'

         
                user = User.objects.create_user(username=username, email=email, password=password,  phone_number=phone_number, paypal_client_id=paypal_client_id ,image=image)
                user.save()

                user_login = auth.authenticate(username=username,password=password)
                
                auth.login(request, user_login)

                if user_login.paypal_client_id:
                    return redirect('userfee')
                else:

                    return redirect('home')
              

        
        else:

            messages.info(request, 'invalid data')
            return redirect('register')



    return render(request, 'base/register2.html')




def login(request):

    if request.user.is_authenticated:
        return redirect('home')
   
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'username or password inccorect')

    return render(request, 'base/login.html')



def logout(request):
    auth.logout(request)
    return redirect('login')


def userfee(request):

    userfee = 50

    return render(request,'base/userfee.html',{'userfee':userfee})



def home(request):
    users = User.objects.all()
 
    
    feedbacks = Feedback.objects.all()
    blogs = Blog.objects.all()[:2]
    faqs = FAQ.objects.all()
    plants_type = ProductType.objects.get(title='plant')
    product_type = ProductType.objects.get(title='product')

    plants = Product.objects.filter(product_type=plants_type, quantity__gt=0)[:6]
    products = Product.objects.filter(product_type=product_type,quantity__gt=0)[:6]

    
    result = None
    if request.method == "POST":
            query = request.POST.get('query')
            result = chain.invoke(query)
            

 

    if request.user.is_authenticated:
        cart_items_count = CartItem.objects.filter(user=request.user).count()
            
            # user = request.user
            # feedback = request.POST['feedback']
            # good_or_bad = request.POST['good_or_bad']
            # CreateFeedback = Feedback.objects.create(user=user, feedback=feedback,good_or_bad=good_or_bad)
            # CreateFeedback.save()
            # return redirect('home')
    else:
        cart_items_count = 0   
    
        
   
   
    context = {
        'users':users,
        'blogs':blogs,
        'feedbacks':feedbacks , 
       
        # 'products':products,
        'faqs':faqs,
        'plants':plants,
        'products':products,
        'cart_items_count':cart_items_count
   
        } 
    return render(request, 'base/home.html',{'users':users,'blogs':blogs, 'feedbacks':feedbacks ,'faqs':faqs,   'plants':plants,'products':products,'cart_items_count':cart_items_count, 'result':result})




def plants(request):
    q = request.GET.get('q') if request.GET.get('q') != None  else ''
    plants_type = ProductType.objects.get(title='plant')
    Product.objects.filter(quantity=0).delete()
  
    
    products = Product.objects.filter(
            
            Q(name__icontains=q)|
            Q(price__icontains=q)|
            Q(description__icontains=q)|
            Q(category__title__icontains=q),
            product_type=plants_type,
            quantity__gt=0
           
           
        )
   
    
    
    blogs = Blog.objects.all()[0:5]


    context = {'products':products, 'blogs':blogs }


    return render(request, 'base/plants.html', context)


def lowPricePlants(request):
    q = request.GET.get('q') if request.GET.get('q') != None  else ''
    plants_type = ProductType.objects.get(title='plant')
    Product.objects.filter(quantity=0).delete()
    
    products = Product.objects.filter(
            
            Q(name__icontains=q)|
            Q(price__icontains=q)|
            Q(description__icontains=q)|
            Q(category__title__icontains=q),
            product_type=plants_type,
            price__lte=30,
            quantity__gt=0
            
           
           
        )
    
    
    blogs = Blog.objects.all()[0:5]

    context = {'products':products, 'blogs':blogs }
    return render(request, 'base/plants.html', context)



def highPricePlants(request):
    q = request.GET.get('q') if request.GET.get('q') != None  else ''
    plants_type = ProductType.objects.get(title='plant')
    
    products = Product.objects.filter(
            
            Q(name__icontains=q)|
            Q(price__icontains=q)|
            Q(description__icontains=q)|
            Q(category__title__icontains=q),
            product_type=plants_type,
            price__gt=30,
            quantity__gt=0
           
           
        )
    
    
    blogs = Blog.objects.all()[0:5]

    context = {'products':products, 'blogs':blogs }
    return render(request, 'base/plants.html', context)




def indoorplants(request):
    q = request.GET.get('q') if request.GET.get('q') != None  else ''
    plants_type = ProductType.objects.get(title='plant')
    
    
    products = Product.objects.filter(
            
            Q(name__icontains=q)|
            Q(price__icontains=q)|
            Q(description__icontains=q)|
            Q(category__title__icontains=q),
            product_type=plants_type,
            category__title =  'indoor',
             quantity__gt=0
           
           
           
        )
    
    
    blogs = Blog.objects.all()[0:5]

    context = {'products':products, 'blogs':blogs }
  
    return render(request, 'base/plants.html', context)


def outdoorplants(request):
    q = request.GET.get('q') if request.GET.get('q') != None  else ''
    plants_type = ProductType.objects.get(title='plant')
    
    
    products = Product.objects.filter(
            
            Q(name__icontains=q)|
            Q(price__icontains=q)|
            Q(description__icontains=q)|
            Q(category__title__icontains=q),
            product_type=plants_type,
            category__title =  'outdoor',
             quantity__gt=0
           
           
           
        )
    
    
    blogs = Blog.objects.all()[0:5]

    context = {'products':products, 'blogs':blogs }
  
    return render(request, 'base/plants.html', context)

def product(request):
    q = request.GET.get('q') if request.GET.get('q') != None  else ''
    product_type = ProductType.objects.get(title='product')
    
    products = Product.objects.filter(
            
            Q(name__icontains=q)|
            Q(price__icontains=q)|
            Q(description__icontains=q)|
            Q(category__title__icontains=q),
            product_type=product_type,
             quantity__gt=0
           
           
        )
    
    
    
    blogs = Blog.objects.all()[0:5]

    context = {'products':products, 'blogs':blogs }

    return render(request, 'base/product.html', context)


@login_required(login_url='login')
def productdetail(request, pk):
    product = Product.objects.get(id=pk)

    context = {'product':product}
    return render(request, 'base/productdetail.html', context)



@login_required(login_url='login')
def add_to_cart(request, product_id):


    
    current_url = request.META.get('HTTP_REFERER')
    
    product = get_object_or_404(Product, id=product_id)
    
    # Get the seller IDs of products currently in the user's cart
    existing_seller_ids = CartItem.objects.filter(user=request.user).values_list('product__seller__id', flat=True).distinct()

    # If the cart already has items from a different seller, clear the cart
    if existing_seller_ids and product.seller.id not in existing_seller_ids:
        CartItem.objects.filter(user=request.user).delete()

    # Add or update the cart item
    try:
        cart_item = CartItem.objects.get(user=request.user, product=product)
        cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        CartItem.objects.create(user=request.user, product=product, quantity=1)

    return HttpResponseRedirect(current_url)


@login_required(login_url='login')
def remove_from_cart(request, product_id):
    CartItem.objects.filter(user=request.user, product_id=product_id).delete()
    return redirect('cart')


@login_required(login_url='login')
def update_cart_item(request, product_id):
    if request.method == 'POST':
        action = request.POST.get('action')
        product = get_object_or_404(Product, id=product_id)
        cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
        
        if action == 'increment':
            if product.quantity > cart_item.quantity:
                cart_item.quantity += 1
                cart_item.save()

        elif action == 'decrement':
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
            # else:
            #     # If quantity is already 1 and decrement is attempted, remove the item from the cart
            #     cart_item.delete()
        else:
            return HttpResponseBadRequest("Invalid action")
        
        return redirect('cart')
    else:
        return HttpResponseBadRequest("Invalid request method")




@login_required(login_url='login')
def cart(request):

    cart_items = CartItem.objects.filter(user=request.user)
    cart_items_count = CartItem.objects.filter(user=request.user).count()
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    
    # Calculate and attach the total price for each item
    for item in cart_items:
        item.total_price = item.product.price * item.quantity

    return render(request, 'base/cart2.html', {'cart_items': cart_items, 'total_price': total_price, 'cart_items_count':cart_items_count})


@login_required(login_url='login')
def checkout(request):
    # superuser = User.objects.get(username='admin')
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    superuser = User.objects.get(username='admin')
    superuser_paypal_id = superuser.paypal_client_id 


    return render(request, 'base/checkout.html', {'superuser_paypal_id':superuser_paypal_id,'superuser':superuser,'total_price': total_price, 'cart_items': cart_items})



@login_required(login_url='login')
def shipping_address(request):
    # Here you can handle the shipping address form
    user = request.user
    shipping_address = user.shippingaddress_set.first()
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
  


    if request.method == 'POST':
        form = ShippingAddressForm(request.POST, instance=shipping_address)
        if form.is_valid():
            shipping_address = form.save(commit=False)
            shipping_address.user = request.user
            shipping_address.save()
            
            # Create an order and add items from the cart
            order = Order.objects.create(user=request.user, total_price=total_price)
            cart_items = CartItem.objects.filter(user=request.user)
            # order.items.add(*cart_items)

            for cart_item in cart_items:
                product = cart_item.product
                product.quantity -= cart_item.quantity
                product.save()
                
                order.items.add(cart_item)
            
            
            
            # Clear the cart
            cart_items.delete()
            
            return redirect('order_success')
    else:
        form = ShippingAddressForm(instance=shipping_address)

    return render(request, 'base/shipping_address.html', {'form': form})



@login_required(login_url='login')
def order_success(request):
    return render(request, 'base/order_success.html')



@login_required(login_url='login')
def uploadproduct(request):
    form = ProductForm()
    seller = request.user

    if request.method == "POST":
        seller = request.user
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            if request.user.paypal_client_id:
                
                product = form.save(commit=False)
                product.seller = request.user
                product.save() 
                return redirect('product')
            else:
                messages.info(request, 'You dont have paypal client id please add your PayPal client id')
    context = {'form':form}
    return render(request, 'base/uploadProduct.html', context)    


def updateproduct(request, pk):
    product = Product.objects.get(id=pk)

    if request.method == 'POST':

        form = UpdateProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            print('form error: ',form.errors)
    else:
        form = UpdateProductForm(instance=product)    

    return render(request, 'base/update_product.html', {'form':form})


def updateprofile(request):
    user = request.user
    initial_paypal_client_id = user.paypal_client_id  # Store the initial value

    form = UpdateProfileForm(instance=user)
    if request.method == "POST":
        form = UpdateProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            update_user = form.save(commit=False)
            form.save()

            # Check if PayPal client ID was added for the first time
            if not initial_paypal_client_id and update_user.paypal_client_id:
                return redirect('userfee')
            else:
                return redirect('home')

    context = {'form': form}
    return render(request, 'base/update_profile.html', context)

def restrict_message(request):
    return render(request, 'base/restrict_message.html')

def is_superuser(user):
    return user.is_superuser

@user_passes_test(is_superuser)
def adminpanel(request):

    users = User.objects.all()
    plants = Product.objects.all()
    products = Product.objects.all()
    blogs = Blog.objects.all()
    communitys = CommunityForm.objects.all()
    feedbacks = Feedback.objects.all()

    
    context = {
        'users':users,
        'plants':plants,
        'products':products,
        'blogs':blogs,
        'communitys':communitys,
        'feedbacks':feedbacks
    }
    return render(request, 'base/admin_panel.html', context)


def deleteuser(request, pk):
    if request.method == 'POST':
        user = User.objects.get(id=pk)

        user.delete()
        return redirect('adminpanel')

    return render(request, 'base/delete.html')

def deleteblog(request, pk):
    blog = Blog.objects.get(id=pk)

    if request.method == 'POST':

        blog.delete()
        if request.user.is_superuser:
            return redirect('adminpanel')
        else:
            return redirect('home')

    return render(request, 'base/delete.html')
    


def deletecommunity(request, pk):
    community = CommunityForm.objects.get(id=pk)

    if request.method == 'POST':

        community.delete()
        if request.user.is_superuser:
            return redirect('adminpanel')
        else:
            return redirect('home')

    return render(request, 'base/delete.html')


def deletefeedback(request, pk):
    feedback = Feedback.objects.get(id=pk)

    if request.method == 'POST':

        feedback.delete()
        if request.user.is_superuser:
            return redirect('adminpanel')
        else:
            return redirect('home')

    return render(request, 'base/delete.html')





@login_required(login_url='login')
def blog(request):
    q = request.GET.get('q') if request.GET.get('q') != None  else ''
    # blogs = Blog.objects.all()
    users= User.objects.all()

    blogs = Blog.objects.filter(
            Q(user__username__icontains=q)|
            Q(caption__icontains=q)|
            Q(text__icontains=q)

            
    )

    
    if request.method == "POST":
        user = request.user
        caption = request.POST['caption']
        text = request.POST['text']
        image = request.FILES.get('image')

        if Blog.objects.filter(caption=caption).exists():
            messages.info(request, 'caption already exsist try somethig new')
            return redirect('blog')
            
        else:
            new_post = Blog.objects.create(user=user, caption=caption, text=text, image=image)
            new_post.save()
            return redirect('blog')

    context = {'blogs':blogs, 'users':users}
    return render(request, 'base/blog.html', context)




def likeblog(request):
    user = request.user.username
    post_id = request.GET.get('post_id')

    blog = Blog.objects.get(id=post_id)

    likefilter = LikeBlog.objects.filter(user=user, post_id=post_id).first()
    

    if likefilter == None:
        newlike = LikeBlog.objects.create(user=user, post_id=post_id)
        newlike.save()
        blog.no_of_likes = blog.no_of_likes+1
        blog.save()
        return redirect('blog')
    else:
        likefilter.delete()
        blog.no_of_likes = blog.no_of_likes-1
        blog.save()
        return redirect('blog')





def profile(request, pk):
    user = User.objects.get(id=pk)
    blogs = Blog.objects.filter(user=pk)
    products = Product.objects.filter(seller=pk)


    context = {'user':user, 'products':products , 'blogs':blogs }


    return render(request, 'base/profile.html', context)




def search(request):



    query = request.GET.get('q')
    if query:


        products = Product.objects.filter(
                Q(name__icontains=query)|
                Q(price__icontains=query)
            
        )
    
  

        users = User.objects.filter(
                Q(username__icontains=query)
                
        )


        context = {'query':query,'users':users, 'products':products,'products':products }
        return render(request, 'base/search.html', context)
    else:
        return render(request, 'base/search.html')




@login_required(login_url='login')
def community(request):

    communitys = CommunityForm.objects.all()

    if request.method == "POST":
        user = request.user
        question = request.POST['question']
        image = request.FILES.get('image')


        community_ask = CommunityForm.objects.create(user=user, question=question,  image=image)
        community_ask.save()
        return redirect('community')
        
    context = {'communitys':communitys}
    return render(request, 'base/community.html', context)

@login_required(login_url='login')
def community_post_detail(request, pk):
    community = CommunityForm.objects.get(id=pk)
    community_comment = community.comment_set.all().order_by('-created')

    
    if request.method == 'POST':
        comment = Comment.objects.create(
            user= request.user,
            community= community,
            body = request.POST.get('body')
        )
        community.no_of_comments = community.no_of_comments +1
    
    commnet_count = len(community_comment)   
    
    context = {'community':community, 'commnet_count':commnet_count,'community_comment':community_comment}
    return render(request, 'base/community_post_detail.html', context)


def profile(request, pk):
    user = User.objects.get(id=pk)
    blogs = Blog.objects.filter(user=pk)
    products = Product.objects.filter(seller=pk)


    context = {'user':user, 'products':products , 'blogs':blogs }


    return render(request, 'base/profile.html', context)












