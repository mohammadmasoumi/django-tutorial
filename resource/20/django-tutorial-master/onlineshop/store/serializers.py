from rest_framework import serializers
from store.models import Product, Collection, Review, Cart, CartItem, Customer
from decimal import Decimal

__all__ = (
    "ProductSerializer", 
    "ReviewSerializer", 
    'CartSerializer',
    'CartItemSerializer',
    'AddCartItemSerializer',
    'UpdateCartItemSerializer',
    'CustomerSerializer'
)


class CollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collection
        fields = ['id', 'title']


class ProductSerializer(serializers.ModelSerializer):
    price_with_tax = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'unit_price', 'collection', 'price_with_tax']
        # fields = '__all__'

    # id = serializers.IntegerField()
    # title = serializers.CharField(max_length=255)
    # unit_price = serializers.DecimalField(max_digits=6, decimal_places=2)
    # price = serializers.DecimalField(max_digits=6, decimal_places=2, source="unit_price")
    # collection_id = serializers.IntegerField(write_only=True)
    # collection = serializers.StringRelatedField()
    # collection = CollectionSerializer()
    
    # Validations
    #   serializer fields validation 
    #   model validation
    #   serializer validation - validate_`field`

    def get_price_with_tax(self, instance):
        return instance.unit_price * Decimal(1.09)

    # validate_{$field_name}
    def validate_title(self, title):
        # 1
        if title.startswith('Asghar'):
            raise serializers.ValidationError('You can not start title with Asghar, Asghar is mine, mine alone.')

        # Do not try this at home
        # return title + '_asghar'
        return title

    def validate(self, data):
        # 2
        # if data['password'] != data['confirm_password']:
        #     serializers.ValidationError('password and confirm password does not match!')

        return data

    def create(self, validated_data):
        # request = self.context.get('request')
        validated_data.update(id=3001)
        validated_data.update(slug=validated_data.get("title"))
        validated_data.update(inventory=10)
        validated_data.update(collection=Collection.objects.get(
            title=validated_data.pop("collection"))
        )
        product = Product.objects.create(**validated_data)
        return product

    def update(self, instance, validated_data):
        collection_id = validated_data.pop('collection', None)
        if collection_id:
            coll = Collection.objects.get(id=collection_id)
            instance.collection = coll

        for key ,value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance


class ReviewSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()

    class Meta:
        model = Review
        fields = ('id', 'name', 'description', 'product', 'date')

    def create(self, validated_data): 
        return super().create({
            "product_id":self.context['product_id'],**validated_data
        })


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity']
        

class AddCartItemSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    product_id = serializers.IntegerField()

    class Meta:
        model = CartItem
        fields = ['id', 'product_id', 'quantity']

    def save(self, **kwargs):
        cart_id = self.context.get('cart_id')
        product_id = self.validated_data.get('product_id')
        quantity = self.validated_data.get('quantity')

        try:
            cart_item = CartItem.objects.get(product_id=product_id, cart_id=cart_id)
            cart_item.quantity += quantity
            cart_item.save()
        
        except CartItem.DoesNotExist:
            cart_item = self.create({'cart_id':cart_id, **self.validated_data})

        self.instance = cart_item
        return self.instance


class UpdateCartItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = ['quantity']

    def save(self, **kwargs):
        cart_item_id = self.context.get('cart_item_id')

        try:
            instance = CartItem.objects.get(pk=cart_item_id) 
            self.instance = self.update(instance=instance, validated_data=self.validated_data)
        except CartItem.DoesNotExist:
            serializers.ValidationError("CartItem not found.")

        return self.instance
    

class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'items']


class CustomerSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()

    class Meta:
        model = Customer
        fields = ['id', 'phone', 'membership', 'birth_date', 'user_id']