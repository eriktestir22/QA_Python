import mysql.connector


try:
    config = {
    'host' : 'localhost',
    'user' : 'nahekon955',
    'password': 'Admin123',
    'database': 'naheko955'
    }
    print('successfully connected...')
except Exception as ex:
    print('connection refused')
    print(ex)
