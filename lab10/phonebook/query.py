import psycopg2
from config import load_config

def get_contacts():
    """ Retrieve data from the contacts table """
    config  = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM phonebook ORDER BY contact_name")
                print("\nThe number of contacts:", cur.rowcount,"\n")
                row = cur.fetchone()

                while row is not None:
                    print(row)
                    row = cur.fetchone()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    get_contacts()