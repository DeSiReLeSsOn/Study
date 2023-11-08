"""Ваша задача - создать приложение FastAPI, которое обрабатывает запросы, связанные с продуктами (товарами). Приложение должно иметь две конечные точки:

1. Конечная точка для получения информации о продукте:

   - Маршрут: `/product/{product_id}`

   - Метод: GET

   - Параметр пути:

     - `product_id`: идентификатор продукта (целое число)

   - Ответ: Возвращает объект JSON, содержащий информацию о продукте, основанную на предоставленном `product_id`.

2. Конечная точка для поиска товаров:

   - Маршрут: `/products/search`

   - Метод: GET

   - Параметры запроса:

     - `keyword` (строка, обязательна): ключевое слово для поиска товаров.

     - `category` (строка, необязательно): категория для фильтрации товаров.

     - `limit` (целое число, необязательно): максимальное количество товаров для возврата (по умолчанию 10, если не указано иное).

   - Ответ: Возвращает массив JSON, содержащий информацию о продукте, соответствующую критериям поиска.

3. Для примера можете использовать следующие данные с целью последующего направления ответа:

sample_product_1 = {
    "product_id": 123,
    "name": "Smartphone",
    "category": "Electronics",
    "price": 599.99
}

sample_product_2 = {
    "product_id": 456,
    "name": "Phone Case",
    "category": "Accessories",
    "price": 19.99
}

sample_product_3 = {
    "product_id": 789,
    "name": "Iphone",
    "category": "Electronics",
    "price": 1299.99
}

sample_product_4 = {
    "product_id": 101,
    "name": "Headphones",
    "category": "Accessories",
    "price": 99.99
}

sample_product_5 = {
    "product_id": 202,
    "name": "Smartwatch",
    "category": "Electronics",
    "price": 299.99
}

sample_products = [sample_product_1, sample_product_2, sample_product_3, sample_product_4, sample_product_5]
 

Пример:

Запрос GET на `/product/123` должен возвращать:

{
    "product_id": 123,
    "name": "Smartphone",
    "category": "Electronics",
    "price": 599.99
}
В ответ на GET-запрос на `/products/search?keyword=phone&category=Electronics&limit=5` должно вернуться:

[
    {
        "product_id": 123,
        "name": "Smartphone",
        "category": "Electronics",
        "price": 599.99
    },
    {
        "product_id": 789,
        "name": "Iphone",
        "category": "Electronics",
        "price": 1299.99
    },
    ...
]"""
from model2 import sample_products 
from fastapi import FastAPI
from pydantic import BaseModel

class Product(BaseModel):
    product_id: int
    name: str
    category: str 
    price:float 


app = FastAPI(title="PRODUCTS")  

@app.get("/product/search")
def read_product_by_keyword(keyword:str, category:str = None, limit: int = 10):
    if not category:
        return list(filter(lambda x: keyword in x.name , map(lambda item: Product(**item),
                           sample_products)))[:limit]
    else:
        return list(filter(
            lambda x: keyword in x.name and x.category == category, map(
                lambda item: Product(**item), sample_products)))[:limit]
            
        


@app.get("/product/{product_id}")
def read_prod_by_id(product_id: int):
    return list(filter(lambda x: x.product_id == product_id, map(lambda item: Product(**item), sample_products)))[0]






