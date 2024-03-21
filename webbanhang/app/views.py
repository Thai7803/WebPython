from ast import Or
from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
# def test(request):
#     if request.user.is_authenticated:
#         customer = request.user
#         order, create = Order.objects.get_or_create(customer=customer, complete=False)
#         items = order.orderitem_set.all()
#         cartItems = order.get_cart_items
#         user_not_login = "hidden"
#         user_login = "show"
#     else:
#         items = []
#         order = {'get_cart_items':0, 'get_cart_total':0}
#         cartItems = order['get_cart_items']
#         user_not_login = "show"
#         user_login = "hidden"
#     categories = Category.objects.filter(is_sub=False)     
#     products = Product.objects.all()
#     context = {'products':products, 'cartItems':cartItems, 'user_not_login':user_not_login, 'user_login':user_login, 'categories':categories}
#     return render(request, 'app/test.html', context)

def test(request):
    return render(request, 'app/test.html')


def detail(request):
    if request.user.is_authenticated:
        customer = request.user
        order, create = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        user_not_login = "hidden"
        user_login = "show" 
    else:
        items = []
        order = {'get_cart_items':0, 'get_cart_total':0}
        cartItems = order['get_cart_items']
        user_not_login = "show"
        user_login = "hidden"
    id = request.GET.get('id','') 
    products = Product.objects.filter(id=id)
    categories = Category.objects.filter(is_sub=False)
    context= {'items':items, 'order':order, 'cartItems' : cartItems, 'user_not_login':user_not_login, 'user_login':user_login, 'categories':categories, 'products':products}
    return render(request, 'app/detail.html', context)


def category(request):
    if request.user.is_authenticated:
        customer = request.user
        order, create = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        user_not_login = "hidden"
        user_login = "show"
    else:
        items = []
        order = {'get_cart_items':0, 'get_cart_total':0}
        cartItems = order['get_cart_items']
        user_not_login = "show"
        user_login = "hidden"
    categories = Category.objects.filter(is_sub=False)
    active_category = request.GET.get('category', '')
    if active_category:
        products = Product.objects.filter(category__slug=active_category)
    context = {'categories':categories, 'products':products, 'active_category':active_category, 'user_not_login':user_not_login, 'user_login':user_login,}
    return render(request, 'app/category.html', context)

def search(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        keys = Product.objects.filter(name__icontains = searched)
    if request.user.is_authenticated:
        customer = request.user
        order, create = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        user_not_login = "hidden"
        user_login = "show"
    else:
        items = []
        order = {'get_cart_items':0, 'get_cart_total':0}
        cartItems = order['get_cart_items']
        user_not_login = "show"
        user_login = "hidden"
    categories = Category.objects.filter(is_sub=False)
    products = Product.objects.all()
    return render(request,'app/search.html', {"searched":searched, "keys":keys, 'products':products, 'cartItems':cartItems, 'categories':categories, 'user_not_login':user_not_login, 'user_login':user_login,})

def loginPage(request):
    if request.method == "POST":
        if 'register' in request.POST:
            username = request.POST.get('username')
            first_name = request.POST.get('first_name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            if User.objects.filter(username = username).exists():
                pass
            else:
                user = User.objects.create_user(username=username, first_name=first_name, email=email, password=password)
                user.save()
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request,user)
                    return redirect('home')
        elif 'login' in request.POST:
            username = request.POST.get('login_username')
            password = request.POST.get('login_password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'user or password not correcr!')
                pass
    user_not_login = "show"
    user_login = "hidden"
    categories = Category.objects.filter(is_sub=False)
    context = {'categories':categories, 'user_not_login':user_not_login, 'user_login':user_login,}
    return render(request, 'app/login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login')

def home(request):
    if request.user.is_authenticated:
        customer = request.user
        order, create = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        user_not_login = "hidden"
        user_login = "show"
    else:
        items = []
        order = {'get_cart_items':0, 'get_cart_total':0}
        cartItems = order['get_cart_items']
        user_not_login = "show"
        user_login = "hidden"
    categories = Category.objects.filter(is_sub=False)     
    products = Product.objects.all()
    context = {'products':products, 'cartItems':cartItems, 'user_not_login':user_not_login, 'user_login':user_login, 'categories':categories}
    return render(request,'app/home.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user
        order, create = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        user_not_login = "hidden"
        user_login = "show" 
    else:
        items = []
        order = {'get_cart_items':0, 'get_cart_total':0}
        cartItems = order['get_cart_items']
        user_not_login = "show"
        user_login = "hidden" 
    categories = Category.objects.filter(is_sub=False)
    context= {'items':items, 'order':order, 'cartItems' : cartItems, 'user_not_login':user_not_login, 'user_login':user_login, 'categories':categories}
    return render(request, 'app/cart.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user
        order, create = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
        user_not_login = "hidden"
        user_login = "show"
        if request.method == "POST":
            phone = request.POST.get('phone') 
            address = request.POST.get('address') 
            city = request.POST.get('city') 
            shipping_address, create = ShippingAddress.objects.get_or_create(customer=customer)
            shipping_address.phone = phone
            shipping_address.address = address
            shipping_address.city = city
            shipping_address.order = order
            shipping_address.save()
    else:
        items = []
        order = {'get_cart_items':0, 'get_cart_total':0}
        cartItems = order['get_cart_items']
        user_not_login = "show"
        user_login = "hidden" 
    shipping_address = ShippingAddress.objects.filter(customer=customer).first()
    categories = Category.objects.filter(is_sub=False)
    context= {'items':items, 'order':order, 'shipping_address':shipping_address, 'cartItems' : cartItems, 'user_not_login':user_not_login, 'user_login':user_login, 'categories':categories}
    return render(request, 'app/checkout.html', context) 

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    customer = request.user
    product = Product.objects.get(id = productId)
    order, create = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, create = OrderItem.objects.get_or_create(order=order, product=product)
    if action == 'add':
        orderItem.quantity += 1
    elif action == 'remove':
        orderItem.quantity -= 1
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('added', safe=False)