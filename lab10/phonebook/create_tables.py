# import psycopg2
# from config import load_config

# def create_tables():
#     """ Create tables in the PostgreSQL database"""
#     commands = (
#         """
#         CREATE TABLE phonebook (
#             contact_id SERIAL PRIMARY KEY,
#             contact_name VARCHAR(255), 
#             contact_number VARCHAR (20)
#         )
#         """)
#     try:
#         config = load_config()
#         with psycopg2.connect(**config) as conn:
#             with conn.cursor() as cur:
#                 # execute the CREATE TABLE statement
#                 for command in commands:
#                     cur.execute(command)
#     except (psycopg2.DatabaseError, Exception) as error:
#         print(error)

# if __name__ == '__main__':
#     create_tables()




import psycopg2
from config import load_config

def create_tables():
    """ Create tables in the PostgreSQL database"""
    commands = (
        """
        create table phonebook(
        contact_id serial primary key,
        contact_name varchar (255),
        contact_number varchar (20)
        );
        """,
)
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                # execute the CREATE TABLE statement
                for command in commands:
                    cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    create_tables()