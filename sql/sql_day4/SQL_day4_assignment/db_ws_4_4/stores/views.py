from django.shortcuts import render, redirect
from .models import Store, Product
from .forms import StoreForm, ProductForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST

def index(request):
    stores = Store.objects.all()
    context = {
        'stores': stores,
    }
    return render(request, 'stores/index.html', context)

def detail(request, pk):
    store = Store.objects.get(pk=pk)
    product_form = ProductForm()
    context = {
        'store': store,
        'product_form': product_form,
    }
    return render(request, 'stores/detail.html', context)

@require_http_methods(['GET', 'POST'])
@login_required
def create(request):
    if request.method == 'POST':
        form = StoreForm(request.POST)
        if form.is_valid():
            store = form.save()
            return redirect('stores:detail', store.pk)
    else:
        form = StoreForm()
    context = {
        'form': form,
    }
    return render(request, 'stores/create.html', context)

@require_POST
def create_product(request, pk):
    store = Store.objects.get(pk=pk)

    if not request.user.is_superuser:
        return redirect('stores:detail', store.pk)
    
    form = ProductForm(request.POST)
    if form.is_valid():
        product = form.save(commit=False)
        product.store = store
        product.user = request.user
        form.save()
        return redirect('stores:detail', store.pk)

@require_POST
def delete_product(request, store_pk, prod_pk):
    product = Product.objects.get(pk=prod_pk)
    if request.user == product.user:
        product.delete()
    return redirect('stores:detail', store_pk)