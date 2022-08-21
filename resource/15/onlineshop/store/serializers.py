from rest_framework import serializers
from store.models import Product, Collection
from decimal import Decimal

__all__ = ("ProductSerializer", )


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
        print("----------------------")
        print(f"title: {title}")
        print("----------------------")

        if title.startswith('Asghar'):
            raise serializers.ValidationError('You can not start title with Asghar, Asghar is mine, mine alone.')

        # Do not try this at home
        # return title + '_asghar'
        return title

    def validate(self, data):
        # 2
        print("----------------------")
        print(f"data: {data}")
        print("----------------------")
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
