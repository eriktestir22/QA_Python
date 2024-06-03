import pymysql
import pymysql.cursors
from main_config_base import host,user,password,db_name

try:
    connection = pymysql.connect(
    host=host,
    port=3309,
    user=user,
    password=password,
    database=db_name,
    cursorclass=pymysql.cursors.DictCursor
    )
    print('succsess')
    print('#' * 30)
    try:
        with connection.cursor() as cursor:
            #тут пишем запросы
            q = """
            SELECT id, user_id,status_id,
            DATE_FORMAT(creation_date, '%Y') AS yer_on
            FROM `order`
            WHERE status_id IN (2,4)
            """

            cursor.execute(q)
            rows = cursor.fetchall()

            for i in rows:
                print(i)



    except Exception as e:
        print('An error ')
        print(e)        
            
    finally:
        connection.close()
except Exception as ex:
    print('Connection rufus')
    print(ex)