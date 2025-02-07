from django.urls import path
from .views import add_cart, get_cart

urlpatterns = [
    path('cart/', get_cart, name='get_cart_api'),
    path('cart/add/<int:product_id>/', add_cart, name='add_cart_api'),
]


# from django.urls import path
# from .import views


# urlpatterns = [
#     path('', views.cart, name='cart'),
#     path('add_cart/<int:product_id>/', views.add_cart, name='add_cart'),

# ]
