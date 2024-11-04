import psycopg2
def get_db_connection(db_name, user, password, host='localhost', port='5432'):
    # Kết nối đến cơ sở dữ liệu và trả về kết nối
    conn = psycopg2.connect(
        dbname=db_name,
        user=user,
        password=password,
        host=host,
        port=port
    )
    return conn
