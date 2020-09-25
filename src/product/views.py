from django.shortcuts import render 
from django.core.paginator import Paginator
# Create your views here. , get_object_or_404
from .models import Product




def product_list(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list, 2) 

    page = request.GET.get('page')
    product_list = paginator.get_page(page)
    return render(request,'product/product_list.html',{'product_list':product_list})




def product_detail(request,slug):
    product_detail = Product.objects.get(PRDSLug=slug)

    return render(request,'product/product_detail.html',{'product_detail':product_detail})
