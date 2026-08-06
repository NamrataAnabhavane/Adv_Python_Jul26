from sqlalchemy import (
    create_engine, Table, Column, Integer, String, Float, DateTime, MetaData, select,
    and_,or_,text
)
from sqlalchemy.sql import func

from datetime import datetime

engine = create_engine('sqlite:///advpy2.db', echo=True)

metadata = MetaData()
users_table = Table('users',metadata,
                    Column('id',Integer,primary_key=True, autoincrement=True),
                    Column('name', String(100), nullable=False),
                    Column('age', Integer),
                    Column('city',String(50)),
                    Column('created_at',DateTime,default=datetime.now)
                    )

products_table = Table('products',metadata,
                    Column('id',Integer,primary_key=True, autoincrement=True),
                    Column('name', String(100), nullable=False),
                    Column('price', Float),
                    Column('stock',Integer,default=0),
                    Column('category',String(50))
                   )

metadata.create_all(engine)

def insert_data_core():
    with engine.connect() as conn:
        result = conn.execute(
            users_table.insert().values(
            name='Namrata',
            age = 20,
            city='Mumbai'
            )
        )
        user_id = result.inserted_primary_key[0]

        conn.execute(
            users_table.insert(),
            [
                {'name':'Aadhya','age':25,'city':'Bengaluru'},
                {'name':'Purva','age':19,'city':'Devgad'},
                {'name':'Kasish','age':22,'city':'Kolkata'},
            ]
        )
        conn.commit()
        print(f"Inserted user with ID: {user_id} ")
insert_data_core()
print("Insert complete")
def query_data_core():
    with engine.connect() as conn:
        result = conn.execute(select(users_table))
        print("All users:")
        for row in result:
            print(f"{row}")

        result = conn.execute(
            select(users_table.c.name,users_table.c.city)
        )

        print("\nNames & cities")
        for row in result:
            print(f"{row}")

        result = conn.execute(
            select(
                func.count(users_table.c.id).label('count'),
                users_table.c.city
            ).group_by(users_table.c.city)
        )
        print("\nUser count by city")
        for row in result:
            print(f"{row.city}:{row.count}")

def update_delete_core():
    with engine.connect() as conn:
        result = conn.execute(
            users_table.update().where(users_table.c.id == 2).values(age = 50, city='Delhi')
        )
        print(f"Updated {result.rowcount} row(s)")

        result = conn.execute(
            users_table.delete().where(users_table.c.id == 1)
        )
        print(f"Deleted {result.rowcount} row(s)")
        conn.commit()
update_delete_core()