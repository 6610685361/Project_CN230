def analyze_data(conn):
    cursor = conn.cursor()

    print("\n1. จำนวนประเทศในแต่ละภูมิภาค:")
    for row in cursor.execute("SELECT region, COUNT(*) FROM countries GROUP BY region"):
        print(f"- {row[0]}: {row[1]} ประเทศ")

    print("\n2. ค่าเฉลี่ยประชากรในแต่ละภูมิภาค:")
    for row in cursor.execute("SELECT region, ROUND(AVG(population), 2) FROM countries GROUP BY region"):
        print(f"- {row[0]}: {row[1]:,.0f} คน")

    print("\n3. ประเทศที่มีพื้นที่มากที่สุด 5 อันดับแรก:")
    for row in cursor.execute("SELECT name, area FROM countries ORDER BY area DESC LIMIT 5"):
        print(f"- {row[0]}: {row[1]:,.0f} ตร.กม.")

    print("\n4. ประเทศที่มีความหนาแน่นประชากรสูงสุด 5 อันดับ:")
    for row in cursor.execute("""
        SELECT name, ROUND(population / area, 2) AS density
        FROM countries
        WHERE area > 0
        ORDER BY density DESC
        LIMIT 5
    """):
        print(f"- {row[0]}: {row[1]} คน/ตร.กม.")

    print("\n5. ประเทศที่ไม่มีเมืองหลวง:")
    for row in cursor.execute("SELECT name FROM countries WHERE capital IS NULL OR TRIM(capital) = ''"):
        print(f"- {row[0]}")

    print("\n6. ประเทศที่มีพื้นที่มากกว่าค่าเฉลี่ยของทั้งโลก:")
    for row in cursor.execute("""
        SELECT name, area FROM countries
        WHERE area > (SELECT AVG(area) FROM countries)
        ORDER BY area DESC
        LIMIT 5
    """):
        print(f"- {row[0]}: {row[1]:,.0f} ตร.กม.")
