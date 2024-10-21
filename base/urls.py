from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('update-cart-item/<int:product_id>/', views.update_cart_item, name='update_cart_item'),

   
    path('userfee/', views.userfee, name='userfee'),
    path('checkout/', views.checkout, name='checkout'),

   

    
    path('shipping-address/', views.shipping_address, name='shipping_address'),
    path('order-success/', views.order_success, name='order_success'),



    
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('deleteuser/<str:pk>/', views.deleteuser, name='deleteuser'),
    path('deleteblog/<str:pk>/', views.deleteblog, name='deleteblog'),
    path('deletecommunity/<str:pk>/', views.deletecommunity, name='deletecommunity'),
    path('deletefeedback/<str:pk>/', views.deletefeedback, name='deletefeedback'),
    path('adminpanel', views.adminpanel, name='adminpanel'),
    
    path('plants', views.plants, name='plants'),
    path('lowPricePlants', views.lowPricePlants, name='lowPricePlants'),
    path('highPricePlants', views.highPricePlants, name='highPricePlants'),
    path('indoorplants', views.indoorplants, name='indoorplants'),
    path('outdoorplants', views.outdoorplants, name='outdoorplants'),
    
    
    
    path('product', views.product, name='product'),
    path('productdetail/<str:pk>/', views.productdetail, name='productdetail'),
    path('blog', views.blog, name='blog'),
    path('likeblog', views.likeblog, name='likeblog'),
    path('uploadproduct', views.uploadproduct, name='uploadproduct'),
    path('updateproduct/<str:pk>/', views.updateproduct, name='updateproduct'),


    path('search', views.search, name='search'),
    path('profile/<str:pk>/', views.profile, name='profile'),
    path('updateprofile', views.updateprofile, name='updateprofile'),
    path('community', views.community, name='community'),
    path('communitypostdetail/<str:pk>/', views.community_post_detail, name='community_post_detail'),
]
