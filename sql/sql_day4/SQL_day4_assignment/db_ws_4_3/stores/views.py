from django.shortcuts import render, redirect
from .models import Store
from .forms import StoreForm, ProductForm
from django.contrib.auth.decorators import login_required

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
