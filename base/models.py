from django.db import models
from django.conf import settings
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid



# Create your models here.


class User(AbstractUser):

    user = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, blank=True)
    phone_number = models.BigIntegerField(null=True , blank=True)
    image = models.ImageField(upload_to='profile_images' , null=True, blank=True, default='profile_images/avatar.jpg' )
    paypal_client_id = models.CharField(max_length=300, null=True, blank=True )
   
    REQUIRED_FIELDS = []


    
class ProductType(models.Model):
    title  = models.CharField(max_length=100)

    
    def __str__(self):
        return self.title 

class ProductCategory(models.Model):
    title  = models.CharField(max_length=100)

    
    def __str__(self):
        return self.title       




class Product(models.Model):
  

    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    quantity = models.PositiveIntegerField(default=1)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True, blank=True)  
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, null=True, blank=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    

    def __str__(self):
        return self.name
    




class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.address_line1}, {self.city}, {self.country}"






# ---------------

class Feedback(models.Model):
    Feedback_Choices = (
        ('good', 'Good'),
        ('bad', 'Bad'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=100)
    good_or_bad = models.CharField(max_length=100, choices=Feedback_Choices)
    
    
    def __str__(self):
        return self.feedback

class FAQ(models.Model):
    question = models.CharField(max_length=100)
    answer = models.TextField()
    
    def __str__(self):
        return self.question



class Blog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caption = models.CharField(max_length=500)
    image = models.ImageField(upload_to='blogs')
    text = models.TextField()
    no_of_likes = models.IntegerField(default=0)
    no_of_comments = models.IntegerField(default=0)

    
    def __str__(self):
        return self.caption


        
class LikeBlog(models.Model):
    post_id = models.CharField(max_length=100)
    user = models.CharField(max_length=100)

    def __str__(self):
        return self.user
    

    


class CommunityForm(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blogs', null=True, blank=True)
    no_of_comments = models.IntegerField(default=0)

    
    def __str__(self):
        return self.question


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    community = models.ForeignKey(CommunityForm,  on_delete=models.CASCADE)
    body = models.TextField(default='add comment')
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]
    



class ProcessedID(models.Model):
    product_id = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.product_id)