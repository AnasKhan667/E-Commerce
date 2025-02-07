# store/urls.py
from django.urls import path
from .views import store_api, product_detail_api

urlpatterns = [
    # API endpoint for getting all products OR filtering by category
    path('products/', store_api, name='store'),  
    path('products/<slug:category_slug>/', store_api, name='products_by_category'),  
    
    # API endpoint for getting details of a specific product
    path('products/<slug:category_slug>/<slug:product_slug>/', product_detail_api, name='product_detail'),
]


# from django.urls import path
# from .import views

# urlpatterns = [
#     path('', views.store, name='store'),
#     path('<slug:category_slug>/', views.store, name='products_by_category'),
#     path('<slug:category_slug>/<slug:product_slug>', views.product_detail, name='product_detail')
# ]


