from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category


# Create your views here.
# store/views.py
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from .models import Product, Category
from .serializers import ProductSerializer

@api_view(['GET'])
def store_api(request, category_slug=None):
    """Fetch all products or products by category"""
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category, is_available=True)
    else:
        products = Product.objects.filter(is_available=True)
    
    serializer = ProductSerializer(products, many=True)
    return Response({"products": serializer.data, "product_count": products.count()})

@api_view(['GET'])
def product_detail_api(request, category_slug, product_slug):
    """Fetch details of a single product"""
    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)
    serializer = ProductSerializer(product)
    return Response(serializer.data)


# def store(request, category_slug=None):
#     categories = None
#     products = None

#     if category_slug !=None:
#         categories = get_object_or_404(Category, slug=category_slug)
#         products = Product.objects.filter(category=categories, is_available=True)
#         product_count = products.count()
#     else:
#         products = Product.objects.all().filter(is_available=True)
#         product_count = products.count()

#     context = {
#         'products': products,
#         'product_count' : product_count,
#     }
#     return render(request, 'store/store.html', context)

# def product_detail(request, category_slug, product_slug):
#     try:
#         single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
#     except Exception as e:
#         raise e
    
#     context = {
#         'single_product': single_product,
#     }
#     return render(request, 'store/product_detail.html', context)