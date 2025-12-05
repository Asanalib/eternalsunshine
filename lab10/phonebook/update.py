import psycopg2
from config import load_config


def update_contact(contact_id, contact_name, contact_number):
    """ Update contact name based on the contact id """

    updated_row_count = 0

    sql = """ UPDATE phonebook
                SET contact_name = %s, contact_number = %s
                WHERE contact_id = %s"""

    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:

                # execute the UPDATE statement
                cur.execute(sql, (contact_name, contact_id, contact_number))
                updated_row_count = cur.rowcount

            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return updated_row_count

if __name__ == '__main__':
    update_contact(int(input()), input(), input())