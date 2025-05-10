from data_loader import fetch_country_data
from db_handler import create_connection, create_database, insert_data
from analyzer import analyze_data

def main():
    countries = fetch_country_data()
    conn = create_connection()
    create_database(conn)
    insert_data(conn, countries)
    analyze_data(conn)
    conn.close()

if __name__ == "__main__":
    main()
