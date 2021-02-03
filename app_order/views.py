from django.views.generic import DetailView
from .models import Cart, Order, OrderItem
from django.shortcuts import redirect


class CartDetail(DetailView):
    model = Cart
    context_object_name = 'cart'
    template_name = 'order/cart.html'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
        return queryset.get()

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


def submit_order(request):
    cart_items = request.user.cart.cart_item.all_unique()
    order = Order.objects.create(cart=request.user.cart)
    for cart_item in cart_items:
        OrderItem.objects.create(order=order, shop_product=cart_item.shop_product,
                                 price=cart_item.shop_product.price,
                                 count=cart_item.count_same.count())
    request.user.cart.cart_item.all().delete()
    return redirect('account:user_profile')
