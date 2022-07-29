from random import randint
from store.models import *


def generate():
    for i in range(100):
        if i % 10 == 0:
            collection = Collection.objects.create(title=f'collection-{i}')
            print(f"Create collection {collection}")

        product = Product.objects.create(
            title = f'product-{i}',
            description = f'description-{i}',
            price = float(randint(0, 1000)),
            invetory = i + 10,
            collection = collection
        )
        print(f"Create product {product}")

        
    