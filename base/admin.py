from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(User)
admin.site.register(ProductCategory)
admin.site.register(ProductType)
admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(ShippingAddress)


admin.site.register(FAQ)
admin.site.register(Feedback)
admin.site.register(Blog)
admin.site.register(LikeBlog)
admin.site.register(Comment)
admin.site.register(CommunityForm)