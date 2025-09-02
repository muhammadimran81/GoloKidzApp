from django.shortcuts import render,get_object_or_404, redirect
from django.db.models import Q
from .models import Product, Category, ContactMessage
from .forms import ContactForm, ProductFilterForm
from django.contrib import messages
from django.http import HttpResponse

# Create your views here.
def home(request):
    products = Product.objects.filter(is_active=True)
    categories = Category.objects.all()

    form = ProductFilterForm(request.GET or None)
    if form.is_valid():
        q = form.cleaned_data.get('q')
        category = form.cleaned_data.get('category')
        gender = form.cleaned_data.get('gender')
        size = form.cleaned_data.get('size')
        price_min = form.cleaned_data.get('price_min')
        price_max = form.cleaned_data.get('price_max')


        if q:
            products = products.filter(
            Q(name__icontains=q) | Q(description__icontains=q) | Q(brand__icontains=q)
        )
 
        if category:
            products = products.filter(category__slug=category)
        if gender:
            products = products.filter(gender=gender)
        if size:
            products = products.filter(size=size)
        if price_min is not None:
            products = products.filter(price__gte=price_min)
        if price_max is not None:
            products = products.filter(price__lte=price_max)

   
    return render(request, 'store/home.html', {'products': products, 'categories': categories, 'form': form})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, 'store/product_detail.html', {'product': product})

def about(request):
    return render(request, 'store/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactMessage.objects.create(**form.cleaned_data)
            messages.success(request, 'Thank you! Your message has been received.')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'store/contact.html', {'form': form})