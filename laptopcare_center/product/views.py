from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category
from django.conf import settings
from .forms import OrderForm

def product(request):
    products = Product.objects.filter(is_sold=False)
    categories = Category.objects.all()
    return render(request, 'product/product.html', {
        'categories': categories,
        'products': products,
    })

def detail(request, pk):
    product =  get_object_or_404(Product, pk=pk)
    related_product = Product.objects.filter(is_sold=False, category=product.category).exclude(pk=pk)

    return render(request, 'product/detail.html', {
        'product': product,
        'related_product': related_product
    })

def order(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.save()
            return redirect('core:success')
    else:
        form = OrderForm()

    context = {
        'product': product,
        'form': form
    }
    return render(request, 'product/order.html', context)
