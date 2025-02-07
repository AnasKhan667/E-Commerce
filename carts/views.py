from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Cart, CartItem
from store.models import Product

def _cart_id(request):
    """Get or create the cart ID from session."""
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

@api_view(['POST'])
def add_cart(request, product_id):
    """API to add a product to the cart."""
    product = get_object_or_404(Product, id=product_id)

    try:
        cart, created = Cart.objects.get_or_create(cart_id=_cart_id(request))

        cart_item, item_created = CartItem.objects.get_or_create(
            product=product,
            cart=cart,
            defaults={'quantity': 1}
        )

        if not item_created:
            cart_item.quantity += 1
            cart_item.save()

        return Response({'message': 'Product added to cart', 'quantity': cart_item.quantity}, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_cart(request):
    """API to retrieve cart details."""
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, is_active=True)

        total = sum(item.product.price * item.quantity for item in cart_items)
        quantity = sum(item.quantity for item in cart_items)

        cart_data = {
            'total': total,
            'quantity': quantity,
            'cart_items': [
                {
                    'product': item.product.name,
                    'price': item.product.price,
                    'quantity': item.quantity
                }
                for item in cart_items
            ]
        }
        return Response(cart_data, status=status.HTTP_200_OK)

    except Cart.DoesNotExist:
        return Response({'message': 'Cart is empty'}, status=status.HTTP_404_NOT_FOUND)


# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from store.models import Product
# from .models import Cart, CartItem
# from django.core.exceptions import ObjectDoesNotExist

# # Create your views here.
# def _cart_id(request): #_cart_id = private function 
#     cart = request.session.session_key
#     if not cart:
#         cart = request.session.create()
#     return cart

# def add_cart(request, product_id):
#     product = Product.objects.get(id=product_id) #get the product
#     try:
#         cart = Cart.objects.get(cart_id=_cart_id(request)) # get the cart_id present in the session 
#     except Cart.DoesNotExist:
#         cart = Cart.objects.create(
#             cart_id =_cart_id(request)
#         )
#     cart.save()

#     try:
#         cart_item = CartItem.objects.get(product=product, cart=cart)
#         cart_item.quantity += 1
#         cart_item.save()
#     except CartItem.DoesNotExist:
#         cart_item = CartItem.objects.create(
#             product=product,
#             quantity=1,
#             cart=cart,
#         )
#     cart_item.save()
#     return redirect('cart')
#     # return HttpResponse(cart_item.quantity)
#     # exit()

# def cart(request, total=0, quantity=0, cart_items=None):
#     try:
#         # cart = Cart.objects.get(cart_id=_cart_id(request))
#         cart = Cart.objects.get(cart_id=_cart_id(request))
#         cart_items = CartItem.objects.filter(cart=cart, is_active=True)
#         for cart_item in cart_items:
#             total += (cart_item.product.price * cart_item.quantity)
#             quantity += cart_item.quantity
#     except ObjectDoesNotExist:
#         pass
#             # cart_items = []  # If no cart exists, set cart_items to an empty list


#     context = {
#         'total' : total,
#         'quantity' : quantity,
#         'cart_items' : cart_items,
#     } 
#     return render(request, 'store/cart.html', context)
