from xmlrpc.client import DateTime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import User, auth

# Create your views here.
from products.models import Product, Order


def home(response):
    return render(response, "base.html", {'user': auth})


@login_required(login_url='login')
def products(request):
    products = Product.objects.all()

    return render(request, 'products.html', {'products': products})


def addOrder(request):

    id = request.POST['id']
    product = Product.objects.get(id=id)
    order = Order(user=request.user,product=product,note='test')
    order.save()
    return render(request, "order.html", {'order': order})
