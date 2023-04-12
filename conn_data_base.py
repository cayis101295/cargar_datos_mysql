
import mysql.connector as mysql
from mysql.connector import Error

def connect_data_base():
    try:
        conn = mysql.connect(host='localhost', user='root',  
                            password='PASSWORD')#give ur username, password
        if conn.is_connected():
             print("Base de datos conectada")
             return conn
    except Error as e:
        print("Error while connecting to MySQL", e)

def create_data_base():
    try:
        conn = mysql.connect(host='localhost', database='text_analysis', user='root', password='jisell123')
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE text_analysis")
        print("Database is created")
    except Error as e:
        print(e)

def load_data_amazon(data):
    try:
        conn = mysql.connect(host='localhost', database='text_analysis', user='root', password='jisell123')
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
            cursor.execute('DROP TABLE IF EXISTS AmazonReviews;')
            print('Creating table....')
    # in the below line please pass the create table statement which you want #to create
            cursor.execute("CREATE TABLE AmazonReviews(reviewerName varchar(255),overall varchar(255),reviewTextsort BLOB,reviewTimesort varchar(255))")
            print("Table is created....")
            #loop through the data frame
            for i,row in data.iterrows():
                #here %S means string values 
                sql = "INSERT INTO text_analysis.AmazonReviews VALUES (%s,%s,%s,%s)"
                cursor.execute(sql, tuple(row))
                print("Record inserted")
                # the connection is not auto committed by default, so we must commit to save our changes
                conn.commit()
    except Error as e:
                print("Error while connecting to MySQL", e)

def load_data_ufo(data):
    try:
        conn = mysql.connect(host='localhost', database='text_analysis', user='root', password='jisell123')
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
            cursor.execute('DROP TABLE IF EXISTS UFO;')
            print('Creating table....')
    # in the below line please pass the create table statement which you want #to create
            cursor.execute("CREATE TABLE UFO(level_0 INT,index INT,stats BLOB)")
            print("Table is created....")
            #loop through the data frame
            for i,row in data.iterrows():
                #here %S means string values 
                sql = "INSERT INTO text_analysis.UFO VALUES (%s,%s,%s)"
                cursor.execute(sql, tuple(row))
                print("Record inserted")
                # the connection is not auto committed by default, so we must commit to save our changes
                conn.commit()
    except Error as e:
                print("Error while connecting to MySQL", e)
    