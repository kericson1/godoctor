import pymysql


def symptomes():
    connect = pymysql.connect(host='127.0.0.1', user='root', password='', db='godoctor', charset='utf8mb4')
    cur = connect.cursor()
    cur.execute("SELECT DISTINCT symptom FROM symptoms")
    symptom = cur.fetchall()
    result = []
    for elem in symptom:
        result.append(elem[0])
    print(result)

symptomes()
