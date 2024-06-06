from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .models import Product, Cart
from .forms import CartForm
from django.conf import settings
from django.core.mail import send_mail
from django.conf import settings
from .forms import SubmitCartForm


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('products')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

@login_required
def add_to_cart(request):
    if request.method == 'POST':
        form = CartForm(request.POST)
        if form.is_valid():
            product_id = form.cleaned_data['product_id']
            quantity = form.cleaned_data['quantity']
            product = Product.objects.get(id=product_id)
            Cart.objects.create(user=request.user, product=product, quantity=quantity)
            return redirect('cart')
    return redirect('products')

@login_required
def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)
    if request.method == 'POST':
        form = SubmitCartForm(request.POST)
        if form.is_valid():
            recipient_email = form.cleaned_data['email']
            cart_details = "\n".join([f"{item.product.name}: {item.quantity}" for item in cart_items])
            send_mail(
                'Your Cart Details',
                cart_details,
                settings.EMAIL_HOST_USER,
                [recipient_email],
                fail_silently=False,
            )
            cart_items.delete()
            return redirect('products')
    else:
        form = SubmitCartForm()
    return render(request, 'cart.html', {'cart_items': cart_items, 'form': form})
def logout_view(request):
    auth_logout(request)
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

