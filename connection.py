import psycopg2
from secret import *
import telebot

bot = telebot.TeleBot(API_KEY)

def open_connection():
    conn = psycopg2.connect(database = 'exambot',
                            user = 'postgres',
                            host = 'localhost',
                            password = password1,
                            port = 5432)
    return conn

def close_connection(conn,cur):
    conn.close()
    cur.close()
