import sqlite3

def create_connection(db_name="countries.db"):
    return sqlite3.connect(db_name)

def create_database(conn):
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS countries")
    cursor.execute("""
        CREATE TABLE countries (
            name TEXT,
            capital TEXT,
            region TEXT,
            subregion TEXT,
            population INTEGER,
            area REAL
        )
    """)
    conn.commit()

def insert_data(conn, countries):
    cursor = conn.cursor()
    for country in countries:
        name = country.get("name", {}).get("common", "")
        capital = country.get("capital", [""])[0] if country.get("capital") else ""
        region = country.get("region", "")
        subregion = country.get("subregion", "")
        population = country.get("population", 0)
        area = country.get("area", 0.0)
        cursor.execute("""
            INSERT INTO countries (name, capital, region, subregion, population, area)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (name, capital, region, subregion, population, area))
    conn.commit()
