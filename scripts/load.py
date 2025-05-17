import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

def load(transformed_data):
    conn = mysql.connector.connect(
        host='host.docker.internal', 
        user=os.getenv('USER'),
        password=os.getenv('PASSWORD'),
        database=os.getenv('DATABASE'),
        port=os.getenv('PORT')
    )
    cursor = conn.cursor()

    insert_query = """
    INSERT INTO location_search (location_id, location_name, province, keyword)
    VALUES (%s, %s, %s, %s);
    """

    cursor.executemany(insert_query, transformed_data)

    conn.commit()
    cursor.close()
    conn.close()
