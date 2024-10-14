import telebot
from connection import *
from io import BytesIO


def create_db_user():
    conn = open_connection()
    cur = conn.cursor()
    cur.execute(f""" create table if not exists users(
                id serial primary key,
                telegram_id numeric,
                username varchar(100),
                created_at date default current_date);""")
    conn.commit()
    close_connection(conn,cur)

def create_db_product():
    conn = open_connection()
    cur= conn.cursor()
    cur.execute(f""" create table if not exists product(
                id serial primary key,
                name varchar(100),
                description varchar(255),
                price numeric(10,2),
                quantity int,
                image bytea,
                created_at date default current_date);""")
    conn.commit()
    close_connection(conn,cur)


def create_db_cart():
    conn = open_connection()
    cur = conn.cursor()
    cur.execute(f""" create table if not exists cart(
                id serial primary key,
                user_id int references users(id),
                product_id int references product(id),
                quantity int,
                created_at date default current_date);""")
    conn.commit()
    close_connection(conn,cur)


def create_db_order():
    conn = open_connection()
    cur = conn.cursor()
    cur.execute(f""" create table if not exists orders(
                id serial primary key,
                user_id int references users(id),
                total_amount numeric(10,2),
                status varchar(20) default 'v obrabotke',
                craeted_at date default current_date);""")
    conn.commit()
    close_connection(conn,cur)