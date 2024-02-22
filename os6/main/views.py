from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from main.forms import *
from main.models import StoreProductModel,CategoryProductModel,ProductModel,ProductPriceModel

def index(request):
    return render(request,'main/index.html',{'title':'Главная страница'})

def store_print(request):
    store = StoreProductModel.objects.all()
    return render(request,'main/store.html',{'store':store,'title':'Вывод статей'})

def category_print(request):
    category = CategoryProductModel.objects.all()
    return render(request,'main/category_product.html',{'category':category,'title':'Вывод статей категории'})

def price_print(request):
    price = ProductPriceModel.objects.all()
    return render(request,'main/price.html',{'price':price,'title':'Вывод статей цены'})

def product_print(request):
    product = ProductPriceModel.objects.all()
    return render(request, 'main/product.html', {'product': product, 'title': 'Вывод статей продуктов'})

def create_store(request):
    if request.method == 'POST':
        form = StoreProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StoreProductForm()
    return render(request, 'main/create_store.html', {'form': form})

def create_category(request):
    if request.method == 'POST':
        form = CategoryProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoryProductForm()
    return render(request, 'main/create_category.html', {'form': form})

def create_price(request):
    if request.method == 'POST':
        form = ProductPriceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductPriceForm()
    return render(request, 'main/create_price.html', {'form': form})

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()
    return render(request, 'main/create_product.html', {'form': form})

def edit_store(request, id):
    store = get_object_or_404(StoreProductModel, id=id)
    if request.method == 'POST':
        form = StoreProductForm(request.POST, instance=store)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StoreProductForm(instance=store)
    return render(request, 'main/edit_store.html', {'form': form, 'store': store})

def edit_category(request, id):
    category = get_object_or_404(CategoryProductModel, id=id)
    if request.method == 'POST':
        form = StoreProductForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StoreProductForm(instance=category)
    return render(request, 'main/edit_category.html', {'form': form, 'store': category})

def edit_price(request, id):
    price = get_object_or_404(ProductPriceModel, id=id)
    if request.method == 'POST':
        form = ProductPriceForm(request.POST, instance=price)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductPriceForm(instance=price)
    return render(request, 'main/edit_category.html', {'form': form, 'price': price})

def edit_product(request, id):
    product = get_object_or_404(ProductModel, id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm(instance=product)
    return render(request, 'main/edit_product.html', {'form': form, 'product': product})

def delete_store(request, id):
    store = get_object_or_404(StoreProductModel, id=id)
    store.delete()
    return redirect('home')

def delete_price(request, id):
    price = get_object_or_404(ProductPriceModel, id=id)
    price.delete()
    return redirect('home')

def delete_category(request, id):
    category = get_object_or_404(CategoryProductModel, id=id)
    category.delete()
    return redirect('home')

def delete_product(request, id):
    product = get_object_or_404(ProductModel, id=id)
    product.delete()
    return redirect('home')

'''
class AddCategory(CreateView):
    form_class = CategoryProductForm
    template_name = 'main/create_category.html'
    success_url = reverse_lazy('category_print')

class AddStore(CreateView):
    form_class = StoreProductForm
    template_name = 'main/create_store.html'
    success_url = reverse_lazy('store')

class AddPrice(CreateView):
    form_class = ProductPriceModel
    template_name = 'main/create_price.html'
    success_url = reverse_lazy('price')

'''
