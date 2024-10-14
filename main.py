from context import *
from connection import *
from telebot import types
from telebot.types import InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardMarkup

create_db_user()
create_db_product()
create_db_cart()
create_db_order()



@bot.message_handler(commands = ['start'])
def welcome(message):
    global btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15, btn16, btn17, btn18, btn19, btn20
    btn1 = types.InlineKeyboardButton("u_add")
    btn2 = types.InlineKeyboardButton("u_show")
    btn3 = types.InlineKeyboardButton("u_upd")
    btn4 = types.InlineKeyboardButton("u_del")
    btn5 = types.InlineKeyboardButton("p_add")
    btn6 = types.InlineKeyboardButton("p_show")
    btn7 = types.InlineKeyboardButton("p_upd")
    btn8 = types.InlineKeyboardButton("p_del")
    btn9 = types.InlineKeyboardButton("c_add")
    btn10 = types.InlineKeyboardButton("c_show")
    btn11 = types.InlineKeyboardButton("c_upd")
    btn12 = types.InlineKeyboardButton("c_del")
    btn13 = types.InlineKeyboardButton("o_add")
    btn14 = types.InlineKeyboardButton("o_show")
    btn15 = types.InlineKeyboardButton("o_upd")
    btn16 = types.InlineKeyboardButton("o_del")
    btn17 = types.InlineKeyboardButton("user")
    btn18 = types.InlineKeyboardButton("product")
    btn19 = types.InlineKeyboardButton("cart")
    btn20 = types.InlineKeyboardButton("order")
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(btn17,btn18,btn19,btn20)
    bot.send_message(message.chat.id, "Welcome to online Farmacy!", reply_markup=markup)
    bot.register_next_step_handler(message,handler)
def handler(message):
    if message.text == "user":
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
        markup.add(btn1,btn2,btn3,btn4)
        bot.send_message(message.chat.id, "Here is user CRUD", reply_markup=markup)
        bot.register_next_step_handler(message,message_handler)
    elif message.text == "product":
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
        markup.add(btn5,btn6,btn7,btn8)
        bot.send_message(message.chat.id, "Here is product CRUD", reply_markup=markup)
        bot.register_next_step_handler(message,message_handler)    
    elif message.text == "cart":
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
        markup.add(btn9,btn10,btn11,btn12)
        bot.send_message(message.chat.id, "Here is cart CRUD", reply_markup=markup)
        bot.register_next_step_handler(message,message_handler)    
    elif message.text == "order":
        markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
        markup.add(btn13,btn14,btn15,btn16)
        bot.send_message(message.chat.id, "Here is order CRUD", reply_markup=markup)
        bot.register_next_step_handler(message,message_handler)

def message_handler(message):
    if message.text == "u_add":
        conn = open_connection()
        cur = conn.cursor()
        cur.execute(f"insert into users(telegram_id,username) values({message.chat.id},'{message.chat.username}')")
        conn.commit()
        close_connection(conn,cur)
        bot.send_message(message.chat.id, "Your acc has been added!")
        bot.register_next_step_handler(message,message_handler)
    elif message.text == "u_show":
        conn = open_connection()
        cur = conn.cursor()
        cur.execute(f"select * from users where telegram_id = {message.chat.id}")
        user = cur.fetchone()
        close_connection(conn,cur)
        bot.send_message(message.chat.id, f"Your information in db is: {str(user)}")
        bot.register_next_step_handler(message,message_handler)    
    elif message.text == "u_upd":
        bot.send_message(message.chat.id, "Enter new username you want to be in db")
        bot.register_next_step_handler(message,user_up)
    elif message.text == "u_del":
        conn = open_connection()
        cur = conn.cursor()
        cur.execute(f"delete from users where telegram_id = {message.chat.id}")
        conn.commit()
        close_connection(conn,cur)
        bot.send_message(message.chat.id, "Your profile deleted!")
        bot.register_next_step_handler(message,message_handler)
    elif message.text == "p_add":
        if message.chat.id == 1077938369:
            bot.send_message(message.chat.id,"Enter product name: ")
            bot.register_next_step_handler(message,pr_name)
        else:
            bot.send_message(message.chat.id, "You don`t have admin rights!")
            bot.register_next_step_handler(message,message_handler)
    elif message.text == "p_show":
        conn = open_connection()
        cur = conn.cursor()
        cur.execute("select * from product")
        pr = cur.fetchall()
        close_connection(conn,cur)
        bot.send_message(message.chat.id, str(pr))
        bot.register_next_step_handler(message,message_handler)
    elif message.text == "p_upd":
        if message.chat.id == 1077938369:
            bot.send_message(message.chat.id, "Enter product name to change price")
            bot.register_next_step_handler(message,updater)
        else:
            bot.send_message(message.chat.id, "You dont have admin rights")
            bot.register_next_step_handler(message,message_handler)
    elif message.text == "p_del":
        if message.chat.id == 1077938369:
            bot.send_message(message.chat.id, "enter product name to del")
            bot.register_next_step_handler(message,deleter)
        else:
            bot.send_message(message.chat.id, "You dont have admin rights")
            bot.register_next_step_handler(message,message_handler)
    elif message.text == "c_add":
        bot.send_message(message.chat.id,"Enter product name: ")
        bot.register_next_step_handler(message,adder)
    elif message.text == "c_show":
        conn = open_connection()
        cur = conn.cursor()
        cur.execute(f"""select * from cart where user_id = {message.chat.id}""")
        alle = cur.fetchall()
        close_connection(conn,cur)
        bot.send_message(message.chat.id, str(alle))
        bot.register_next_step_handler(message,message_handler)
    elif message.text == "c_upd":
        bot.send_message(message.chat.id,"Enter id of cart")
        bot.register_next_step_handler(message,updetere)
    elif message.text == "c_del":
        bot.send_message(message.chat.id,"Enter id of cart to delete")
        bot.register_next_step_handler(message,deler)
    elif message.text == "o_add":
        conn = open_connection()
        cur = conn.cursor()
        cur.execute(f"""insert into orders(user_id) values((select id from users where telegram_id = {message.chat.id}))""")
        conn.commit()
        close_connection(conn,cur)
        bot.send_message(message.chat.id,"added order")
        bot.register_next_step_handler(message,message_handler)
    elif message.text == "o_show":
        if message.chat.id == 1077938369:
            conn = open_connection()
            cur = conn.cursor()
            cur.execute(f"select * from orders")
            close_connection(conn,cur)
            bot.register_next_step_handler(message,message_handler)
        else:
            conn = open_connection()
            cur = conn.cursor()
            cur.execute(f"""select * from orders where user_id = (select id from users where telegram_id = {message.chat.id})""")
            olle = cur.fetchall()
            close_connection(conn,cur)
            bot.send_message(message.chat.id,str(olle))
            bot.register_next_step_handler(message,message_handler)
    elif message.text == "o_upd":
        if message.chat.id == 1077938369:
            bot.send_message(message.chat.id, "Enter order id to update")
            bot.register_next_step_handler(message,up_or)
        else:
            bot.send_message(message.chat.id,"You do not have admin rights!")
            bot.register_next_step_handler(message,message_handler)
    elif message.text == "o_del":
        bot.send_message(message.chat.id, "Enter order id to refuse")
        bot.register_next_step_handler(message,del_ord)

def del_ord(message):
    orde = message.text
    conn = open_connection()
    cur = conn.cursor()
    cur.execute(f"""delete from orders where id = {orde}""")
    conn.commit()
    close_connection(conn,cur)
    bot.send_message(message.chat.id,"refused the order")
    bot.register_next_step_handler(message,message_handler)


def up_or(message):
    global the_id
    the_id = message.text
    bot.send_message(message.chat.id,"Enter status")
    bot.register_next_step_handler(message,statuser)
def statuser(message):
    status = message.text
    conn = open_connection()
    cur = conn.cursor()
    cur.execute(f"""update orders set status = '{status}' where id = {the_id}""")
    conn.commit()
    close_connection(conn,cur)
    bot.send_message(message.chat.id,"status_updated")
    bot.register_next_step_handler(message,message_handler)





def deler(message):
    id_of_t = message.text
    conn = open_connection()
    cur = conn.cursor()
    cur.execute(f"delete from cart where id = {id_of_t}")
    conn.commit()
    close_connection(conn,cur)
    bot.send_message(message.chat.id,"deleted!")
    bot.register_next_step_handler(message,message_handler)

def updetere(message):
    global id_of
    id_of = message.text
    bot.send_message(message.chat.id,"Enter new quantity")
    bot.register_next_step_handler(message,uper1)

def uper1(message):
    new = message.text
    conn = open_connection()
    cur = conn.cursor()
    cur.execute(f"""update cart set quantity = {new} where id = {id_of}""")
    conn.commit()
    close_connection(conn,cur)
    bot.send_message(message.chat.id,"updated")
    bot.register_next_step_handler(message,message_handler)

def adder(message):
    global product
    product = message.text
    bot.send_message(message.chat.id,"Enter quantity")
    bot.register_next_step_handler(message,adder1)
def adder1(message):
    quant = message.text
    conn = open_connection()
    cur = conn.cursor()
    cur.execute(f"""insert into cart(user_id,product_id,quantity) values(
                    (select id from users where telegram_id = {message.chat.id}),
                    (select id from product where name = '{product}'),
                    {quant})""")
    conn.commit()
    close_connection(conn,cur)
    bot.send_message(message.chat.id, "added to cart")
    bot.register_next_step_handler(message,message_handler)


def deleter(message):
    prod = message.text
    conn = open_connection()
    cur = conn.cursor()
    cur.execute(f"""delete from product where name = '{prod}'""")
    conn.commit()
    close_connection(conn,cur)
    bot.send_message(message.chat.id,"deleted!")
    bot.register_next_step_handler(message,message_handler)

def updater(message):
    global new_name
    new_name = message.text
    bot.send_message(message.chat.id,"Enter new price")
    bot.register_next_step_handler(message,pricer)

def pricer(message):
    n_price = message.text
    conn = open_connection()
    cur = conn.cursor()
    cur.execute(f"""update product
                set price = {n_price} where name = '{new_name}'""")
    conn.commit()
    close_connection(conn,cur)
    bot.send_message(message.chat.id, "updated successfully!")
    bot.register_next_step_handler(message,message_handler)


def user_up(message):
    new = message.text
    conn = open_connection()
    cur = conn.cursor()
    cur.execute(f"update users set username = '{new}' where telegram_id = {message.chat.id}")
    conn.commit()
    close_connection(conn,cur)
    bot.send_message(message.chat.id, "Your username has been changed!")
    bot.register_next_step_handler(message,message_handler)


def pr_name(message):
    global p_name
    p_name = message.text
    bot.send_message(message.chat.id,"Write description: ")
    bot.register_next_step_handler(message,pr_desc)

def pr_desc(message):
    global p_desc
    p_desc = message.text
    bot.send_message(message.chat.id, "Enter product price: ")
    bot.register_next_step_handler(message,pr_price)

def pr_price(message):
    global p_price
    p_price = message.text
    bot.send_message(message.chat.id,"Enter quantity of product: ")
    bot.register_next_step_handler(message,pr_quantity)

def pr_quantity(message):
    global p_quantity
    p_quantity = message.text
    bot.send_message(message.chat.id, "Send photo of product: ")
    bot.register_next_step_handler(message,pr_image)

def pr_image(message):
    if message.content_type == 'photo':
        file_info = bot.get_file(message.photo[-1].file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        conn = open_connection()
        cur = conn.cursor()
        cur.execute("insert into product(name,description,price,quantity,image) values(%s,%s,%s,%s,%s)",(p_name,p_desc,p_price,p_quantity,psycopg2.Binary(downloaded_file)))
        conn.commit()
        close_connection(conn,cur)
        bot.send_message(message.chat.id,"New product added!")
        bot.register_next_step_handler(message,message_handler)
    else:
        conn = open_connection()
        cur = conn.cursor()
        cur.execute("insert into product(name,description,price,quantity) values(%s,%s,%s,%s)",(p_name,p_desc,p_price,p_quantity))
        conn.commit()
        close_connection(conn,cur)
        bot.send_message(message.chat.id,"New product added without photo!")
        bot.register_next_step_handler(message,message_handler)


bot.infinity_polling()