import psycopg2
from config import load_config


def delete_contact(contact_id):
    """ Delete contact by contact id """

    rows_deleted  = 0
    sql = 'DELETE FROM phonebook WHERE contact_id = %s'
    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                # execute the UPDATE statement
                cur.execute(sql, (contact_id,))
                rows_deleted = cur.rowcount

            # commit the changes to the database
            conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        return rows_deleted

if __name__ == '__main__':
    deleted_rows = delete_contact(int(input()))
    print('The number of deleted rows: ', deleted_rows)