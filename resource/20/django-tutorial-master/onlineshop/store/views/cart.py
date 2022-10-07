from rest_framework.viewsets import ModelViewSet
from .base import CreateRetrieveDestroy

from store.models import Cart, CartItem
from store.serializers import *

__all__ = (
    'CartViewSet',
    'CartItemViewSet'
)


class CartViewSet(CreateRetrieveDestroy):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartItemViewSet(ModelViewSet):

    http_method_names = [
        "get",
        "post",
        "patch",
        "delete",
    ]
    serializer_classes = {
        'create': AddCartItemSerializer,
        'list': CartItemSerializer,
        'partial_update': UpdateCartItemSerializer
        # 'retrieve': CartItemSerializer,
    }
    default_serializer = CartItemSerializer

    def get_serializer_context(self):
        return {
            'cart_id': self.kwargs.get('cart_pk'),
            'cart_item_id': self.kwargs.get('pk')
        }

    def get_serializer_class(self):
        print(f"self.action: {self.action}" )
        return self.serializer_classes.get(self.action, self.default_serializer)

    def get_queryset(self):
        return CartItem.objects.select_related('product').filter(cart_id=self.kwargs['cart_pk'])