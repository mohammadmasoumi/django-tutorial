from random import randint
from store.models import *

import pandas as pd

# pip install pandas
# pip insatll openpyxl
# python manage.py shell
# from store.dataset import create_excel
# crate_excel()

def create_excel():
    data = []
    for product in Product.objects.filter():
        data.append([
            product.title,
            product.slug,
            str(product.created_at) 
        ])
    columns = ['Title', 'Slug', 'CreatedAt']

    df = pd.DataFrame(data=data, columns=columns)
    df.to_excel("data.xlsx")

# def generate():
#     for i in range(100):
#         if i % 10 == 0:
#             collection = Collection.objects.create(title=f'collection-{i}')
#             print(f"Create collection {collection}")

#         product = Product.objects.create(
#             title = f'product-{i}',
#             description = f'description-{i}',
#             price = float(randint(0, 1000)),
#             invetory = i + 10,
#             collection = collection
#         )

#         # p = Product(
#         #     title = f'product-{i}',
#         #     description = f'description-{i}',
#         #     price = float(randint(0, 1000)),
#         #     invetory = i + 10, 
#         #     collection = collection
#         # )
#         # p.save()
#         print(f"Create product {product}")

        
    