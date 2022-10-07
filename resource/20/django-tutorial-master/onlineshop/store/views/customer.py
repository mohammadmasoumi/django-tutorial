from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin 
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from store.models import Customer
from store.serializers import CustomerSerializer

# Create your views here.
__all__ = ('CustomerViewSet', )


class CustomerViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    # /list -> store/customers/me
    # /details -> store/customers/1/me
    #  
    @action(detail=False)
    def me(self, request, methods=['GET', 'PUT']):
        customer = Customer.objects.get(user_id=request.user.id)
        serializer = CustomerSerializer(customer)

        return Response(serializer.data)