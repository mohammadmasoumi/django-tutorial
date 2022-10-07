from django.shortcuts import render, get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework import status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.views import APIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
# from rest_framework.mixins import ListModelMixin
from store.serializers import ProductSerializer, ReviewSerializer, CartSerializer
from store.models import Product, Review
from store.filters import ProductFilter
from store.pagination import DefaultPageNumberPagination
from django.views.generic import ListView

__all__ = (
    'product_list', 
    'product_details',
    'product_details2',
    'ProductList',
    'ProductDetails',
    'ProductListCreateAPIView',
    'ProductViewSet',
    'ReviewViewSet'
)


"""
class NotificationViewSet(ModelViewSet):
    pass

    AndroidNotificationSerializer
    IOSNotificationSerializer
    WebNotificationSerializer

    def get_serializer_class(self):
        return {
            'android': AndroidNotificationSerializer,
            'ios': IOSNotificationSerializer,
            'web': WebNotificationSerializer
        }.get(self.query_param.get('device'))

class AndroidNotificationViewSet(NotificationViewSet):
    pass

/notifications/ query_param: android -> NotificationViewSet

/notifications/android/  -> AndroidNotificationViewSet
notifications/ios/
notifications/web/
"""

class ReviewViewSet(ModelViewSet):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['description', 'name']

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs.get('product_pk'))

    def get_serializer_context(self):
        product_id = self.kwargs.get('product_pk')
        return {'product_id': product_id, **super().get_serializer_context()}


class ProductViewSet(ModelViewSet):
    queryset =  Product.objects.select_related("collection")
    # queryset =  Product.objects.select_related("collection").order_by("-created_at").all()[:10]
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    # http://127.0.0.1:8000/store/products/?collection_id=4&unit_price=88.2
    # filterset_fields = ['collection_id', 'unit_price']
    filterset_class = ProductFilter
    search_fields = ['title', 'description', 'collection__title', 'unit_price']
    ordering_fields = ['unit_price', 'last_update']
    # pagination_class = PageNumberPagination
    pagination_class = DefaultPageNumberPagination

    # query params
    # http://127.0.0.1:8000/store/products?collection_id=10
    # def get_queryset(self):
    #     queryset =  Product.objects.select_related("collection")
    #     collection_id = self.request.query_params.get('collection_id')
    #     # print(f"collection_id: {collection_id}, {type(collection_id)}")

    #     if collection_id is not None:
    #         queryset = queryset.filter(collection_id=collection_id)

    #     return queryset

    def destroy(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs.get("pk"))

        if product.orderitems.count() > 0:
             Response({'error': 'You cant delete product with orders'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    # @action(detail=True, methods=['post'])
    # def send_email(self, request, id):
    #     pass

    # def get(self, request):
    #     queryset = Product.objects.select_related("collection").order_by("-created_at").all()[:10]
    #     serializer = ProductSerializer(queryset, many=True, context={'request': request})
    #     return Response({"data": serializer.data}) # Django restframework restponse

    # def post(self, request):
    #     serializer = ProductSerializer(data=request.data)
        
    #     # raise_exception=True
    #     if serializer.is_valid():
    #         serializer.save()  # instance = serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

class ProductListCreateAPIView(ListCreateAPIView):
    queryset =  Product.objects.select_related("collection").order_by("-created_at").all()[:10]
    serializer_class = ProductSerializer
    
    # def get(self, request):
    #     queryset = Product.objects.select_related("collection").order_by("-created_at").all()[:10]
    #     serializer = ProductSerializer(queryset, many=True, context={'request': request})
    #     return Response({"data": serializer.data}) # Django restframework restponse

    # def post(self, request):
    #     serializer = ProductSerializer(data=request.data)
        
    #     # raise_exception=True
    #     if serializer.is_valid():
    #         serializer.save()  # instance = serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

class ProductList(APIView):

    def get(self, request):
        queryset = Product.objects.select_related("collection").order_by("-created_at").all()[:10]
        serializer = ProductSerializer(queryset, many=True, context={'request': request})
        return Response({"data": serializer.data}) # Django restframework restponse

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        
        # raise_exception=True
        if serializer.is_valid():
            serializer.save()  # instance = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
            
class ProductDetails(RetrieveUpdateDestroyAPIView):

    def get(self, request, id):
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        product = get_object_or_404(Product, pk=id)

        if product.orderitems.count() > 0:
            Response({'error': 'You cant delete product with orders'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, id):
        product = get_object_or_404(Product, pk=id)

        serializer = ProductSerializer(product, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

    def patch(self, request, id):
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializer(product, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


@api_view(["GET", "POST"])
def product_list(request):
    method = request.method
    match method:
        case "GET":
            queryset = Product.objects.select_related("collection").order_by("-created_at").all()[:10]
            serializer = ProductSerializer(queryset, many=True, context={'request': request})
            return Response({"data": serializer.data}) # Django restframework restponse
        
        case "POST":
            serializer = ProductSerializer(data=request.data)
            
            # raise_exception=True
            if serializer.is_valid():
                serializer.save()  # instance = serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
            
            # queryset = Product.objects.all()
            # serializer = ProductSerializer(queryset, many=True)
            # return Response({"data": serializer.data}) # Django restframework restponse

    # return render(request, 'empty.html') # Django response


# ["GET", "OPTIONS"]
@api_view(["GET", "DELETE", "PUT", "PATCH"])
def product_details(request, id):
    method = request.method
    product = get_object_or_404(Product, pk=id)

    match method:
        case "GET":
            serializer = ProductSerializer(product)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        case "DELETE":
            # product.product_sets.count()
            if product.orderitems.count() > 0:
                Response({'error': 'You cant delete product with orders'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                product.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)

        # update
        case "PUT":
            serializer = ProductSerializer(product, data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

        # partial: update some special key
        case "PATCH":
            serializer = ProductSerializer(product, data=request.data, partial=True)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


@api_view()
def product_details2(request, id):
    return Response({"data": id})

