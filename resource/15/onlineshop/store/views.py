from math import prod
from re import L
from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.mixins import ListModelMixin
from store.serializers import ProductSerializer
from store.models import Product


__all__ = (
    'product_list', 
    'product_details',
    'product_details2',
    'ProductList',
    'ProductDetails',
    'ProductListCreateAPIView',
    'ProductViewSet'
)


class ProductViewSet(ModelViewSet):
    queryset =  Product.objects.select_related("collection")
    # queryset =  Product.objects.select_related("collection").order_by("-created_at").all()[:10]
    serializer_class = ProductSerializer

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

