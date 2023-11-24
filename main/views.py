from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse
from . models import Main

from .forms import *


def homepage(request):
    return render(request, 'accounts/home.html')



def admin_product_list(request):
    product = Product.objects.all()
    return render(request, 'accounts/product_list.html', context={'product': product})


def menu(request, slug=None):
    if slug:
        category = Category.objects.get(slug=slug)
        product = Product.objects.filter(cat=category)
    else:
        product = Product.objects.all()
    context={'category': Category.objects.all(), 'product': product}
    return render(request, 'accounts/menu.html', context=context)


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def registration(request):
    if request.method == 'POST':

        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:login'))

    else:
        form = UserRegistrationForm()
    context = {'form' : form}
    return  render(request, template_name='accounts/register.html', context=context)

def mainpage(request):
    main = Main.objects.all()
    context={
        'main':main
    }
    return render(request, 'accounts/main.html', context)

def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:main'))
    else:
        form = ProductForm()
    context = {'form': form}
    return render(request,'accounts/products_add.html', context)


def update_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = ProductChangeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('main:menu'))
    else:
        form = ProductChangeForm(instance=Product.objects.get(id=product_id))
    return render(request,'accounts/update_product.html', {'form': form, 'product': product})


# @login_required
# def profile(request):
#     if request.method ==  'POST':
#         form = UserProfileForm(data=request.POST, instance=request.user, files=request.FILES)
#         if form.is_valid():
