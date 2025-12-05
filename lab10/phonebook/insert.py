import psycopg2
from config import load_config


def insert_contact(contact_name, contact_number):
    """ Insert a new contact into the contacts table """

    sql = """INSERT INTO phonebook(contact_name, contact_number)
             VALUES(%s, %s) RETURNING contact_id;"""

    contact_id = None
    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the INSERT statement
                cur.execute(sql, (contact_name, contact_number))

                # get the generated id back
                rows = cur.fetchone()
                if rows:
                    contact_id = rows[0]

                # commit the changes to the database
                conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return contact_id


if __name__ == '__main__':
    insert_contact(input(), input())