from django import forms
from .models import ShippingAddress, Product, User

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number','image','paypal_client_id']
        labels = {
            'username': 'Username',
            'email': 'Email',
            'phone_number': 'Phone Number',
            'image': 'Image',
            'paypal_client_id': 'PayPal Client ID',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-input'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control form-input'}),
            'image': forms.FileInput(attrs={'class': 'form-control form-input'}),
            'paypal_client_id': forms.TextInput(attrs={'class': 'form-control form-input'}),
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','description','price','image','quantity' ,'category', 'product_type']
        labels = {
        
            'name': 'Product Name',
            'description': 'Description',
            'price': 'Price',
            'image': 'Image',
            'quantity':'Quantity',
            'category': 'Category',
            'product_type':'Product Type'

        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-input'}),
            'description': forms.Textarea(attrs={'class': 'form-control form-input description-box'}),
            'price': forms.NumberInput(attrs={'class': 'form-control form-input'}),
            'image': forms.FileInput(attrs={'class': 'form-control form-input'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control form-input'}),
            'category': forms.Select(attrs={'class': 'form-control form-input' }),
            'product_type': forms.Select(attrs={'class': 'form-control form-input' }),
        }

class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ['address_line1', 'address_line2', 'city', 'state', 'country', 'postal_code']
        labels = {
            'address_line1': 'Address Line 1',
            'address_line2': 'Address Line 2 (Optional)',
            'city': 'City',
            'state': 'State',
            'country': 'Country',
            'postal_code': 'Postal Code',
        }
        widgets = {
            'address_line1': forms.TextInput(attrs={'class': 'form-control form-input'}),
            'address_line2': forms.TextInput(attrs={'class': 'form-control form-input'}),
            'city': forms.TextInput(attrs={'class': 'form-control form-input'}),
            'state': forms.TextInput(attrs={'class': 'form-control form-input'}),
            'country': forms.TextInput(attrs={'class': 'form-control form-input'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control form-input'}),
        }



class UpdateProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name','description','price','image','quantity' ,'category', 'product_type']
       

        labels = {
        
            'name': 'Product Name',
            'description': 'Description',
            'price': 'Price',
            'image': 'Image',
            'quantity':'Quantity',
            'category': 'Category',
            'product_type':'Product Type'

        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-input'}),
            'description': forms.Textarea(attrs={'class': 'form-control form-input description-box'}),
            'price': forms.NumberInput(attrs={'class': 'form-control form-input'}),
            'image': forms.FileInput(attrs={'class': 'form-control form-input'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control form-input'}),
            'category': forms.Select(attrs={'class': 'form-control form-input' }),
            'product_type': forms.Select(attrs={'class': 'form-control form-input' }),
        }






# # checkout/forms.py

# from django import forms
# from .models import ShippingAddress, Product, User


# class UpdateProfileForm(forms.ModelForm):
#     class Meta:
#         model = User
#         # fields = '__all__'
#         fields = ['username', 'email', 'phone_number','image','paypal_client_id']

# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ['name','description','price','image','category']

# class ShippingAddressForm(forms.ModelForm):
#     class Meta:
#         model = ShippingAddress
#         fields = ['address_line1', 'address_line2', 'city', 'state', 'country', 'postal_code']
#         labels = {
#             'address_line1': 'Address Line 1',
#             'address_line2': 'Address Line 2 (Optional)',
#             'postal_code': 'Postal Code',
#         }


