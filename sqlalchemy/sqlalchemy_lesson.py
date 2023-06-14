import sqlalchemy as db
from sqlalchemy import Table, Column, MetaData, Integer, Computed, create_engine,update

"""orm"""


engine = create_engine("sqlite:///test_table-sqlalchemy.db")


connection = engine.connect()


metadata = db.MetaData()


"""create simple table"""
test_table = db.Table(
    "test_table",
    metadata,
    db.Column("test_table_id", db.Integer, primary_key=True),
    db.Column("product_name", db.Text),
    db.Column("supplier_name", db.Text),
    db.Column("price", db.Integer)
)

metadata.create_all(engine)

"""filling the table"""

insertion_query = test_table.insert().values(
    [
        {"product_name": "Apple", "supplier_name": "Fruits of Jamaica", "price": 570},
        {"product_name": "Pineapple", "supplier_name": "Fruits of Cuba", "price": 890},
        {
            "product_name": "Watermelon",
            "supplier_name": "Fruits of Ecuador",
            "price": 260
        }
    ]
)


connection.execute(insertion_query)

"""selection"""
#select_all_query = db.select(test_table)
#select_all_result = connection.execute(select_all_query)


#print(select_all_result.fetchall())





select_price_query = db.select(test_table).where(test_table.columns.price==260)
select_price_result = connection.execute(select_price_query)
#print(select_price_result.fetchall())




'''UPDATE'''


update_query = db.update(test_table).where(test_table.columns.supplier_name == "Fruits of Cuba").values(supplier_name = "Fruits of Brazil")
update_all_result=connection.execute(update_query)

select_all_query = db.select(test_table)
select_all_result = connection.execute(select_all_query)


#print(select_all_result.fetchall())


'''DeLETE'''


delete_query = db.delete(test_table).where(test_table.columns.supplier_name == "Fruits of Jamaica")
delete_query_res = connection.execute(delete_query)

select_all_query = db.select(test_table)
select_all_result = connection.execute(select_all_query)


print(select_all_result.fetchall())