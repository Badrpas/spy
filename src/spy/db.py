__author__ = 'Badrpas'

import mysql.connector
from mysql.connector import errorcode


connect_config = {'user': 'root', 'password': '123123',
                  'host': '127.0.0.1'}

cnx = mysql.connector.connect(**connect_config)
cursor = cnx.cursor()


def use_db():
    db_name = 'vk'
    try:
        cnx.database = db_name
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            cursor.execute('CREATE DATABASE '+db_name+' DEFAULT CHARACTER SET \'utf8\'')
            cnx.database = db_name
        else:
            print(err)
            exit(1)

def table_exists(table_name):
    cursor.execute('SHOW TABLES')
    tables = cursor.fetchall()
    if (table_name,) in tables:
        return True
    return False

table_name = 'online_history'

def create_online_history_table():
    table = (
        "CREATE TABLE "+table_name+" ("
        "  id                   int         NOT NULL     AUTO_INCREMENT,"
        "  user_id              int         NOT NULL,"
        "  online_status_change int         NOT NULL,"
        "  ondate               DATETIME            ,"
        "  PRIMARY KEY (id)"
        ")")
    if not table_exists(table_name):
        for item in cursor.execute(table, multi=True):
            print(item)
        print('Created table '+table_name)
    else:
        print('Table '+table_name+' already exists')


def add_online_status(user_id, online, date):

    add_post = ("INSERT INTO " + table_name+ " "
                "(user_id, online_status_change, ondate)"
                "VALUES (%s, %s, %s)")

    data_post= (user_id, online, date)
    try:
        cursor.execute(add_post, data_post)
    except mysql.connector.Error as e:
        if e.errno == 1062:
            print('Such entry is already exists')



def init():
    use_db()
    create_online_history_table()

def finalize():
    cnx.commit()
    cnx.close()
