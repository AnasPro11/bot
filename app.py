import os

import sys

import time

import telebot

import requests

from telebot import *

from telebot import util

from telebot import types

Tokin = "5246722018:AAEpnGh1DW7N34-klyOCsSGlMjTn9P0xN7U"

bot = telebot.TeleBot(Tokin)

data = dict()

@bot.message_handler(commands=['start'])

def welcome(message):

    Keyboards = types.InlineKeyboardMarkup(row_width = 2)

    Anas = types.InlineKeyboardButton(text=" Anas Pro ", url=f"https://t.me/anas_pro")

    start = types.InlineKeyboardButton(text=" start ", callback_data="Start")

    joker = types.InlineKeyboardButton(text=" MR.JOKER ", url=f"https://t.me/JO_5G")

    Keyboards.add(Anas,joker,start)

    bot.send_message(message.chat.id, text=f"🌹| Hi {message.from_user.first_name} in bot ifa2012 \n🔰| Please Click", reply_to_message_id=(message.message_id), reply_markup=Keyboards)

def Code(message):

    chat_id = str(message.chat.id)

    data[chat_id] = []

    msg = bot.reply_to(message, text="Enter Your Code : ")

    bot.register_next_step_handler(msg, sc)

def sc(message):

    chat_id = str(message.chat.id)

    Code = message.text

    data[chat_id].append(Code)

    msg = bot.reply_to(message, text="Enter Sc_Id : ")

    bot.register_next_step_handler(msg, bd)

def bd(message):

    chat_id = str(message.chat.id)

    Sc_Id = message.text

    data[chat_id].append(Sc_Id)

    msg = bot.reply_to(message, text="Enter Bd_Id : ")

    bot.register_next_step_handler(msg, req)

def req(message):

    chat_id = str(message.chat.id)

    Bd_Id = message.text

    data[chat_id].append(Bd_Id)

    bot.reply_to(message, text=f"Send file in ifa2012.txt ")

    @bot.message_handler(content_types=['document'])

    def save(message):

        file_input = bot.download_file(bot.get_file(message.document.file_id).file_path)

        with open(f"{data[chat_id][0]}.txt", 'wb') as f:

            f.write(file_input)

        file = open(f"{data[chat_id][0]}.txt",'r')

        time_imog = list("⌛⏳⌛⏳⌛⏳⌛")

        messages = bot.send_message(message.chat.id, text=f'📮| Starting ⏳ Please Wait ...', reply_to_message_id=message.message_id)

        for i in range(len(time_imog)):

            bot.edit_message_text(text=f'📮| Starting {time_imog[i]} Please Wait ...', chat_id=int(message.chat.id), message_id=messages.message_id)

        d = 0 

        e = 0 

        l = 0 

        for user in file:

            login = requests.post('https://api.ifa2012.com/login/login',headers={'Host':'api.ifa2012.com','Connection':'keep-alive','Content-Length':'102','lang':'EGY','noToken':'true','User-Agent':'Mozilla/5.0 (Linux; Android 8.1.0; SM-T585 Build/M1AJQ;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Safari/537.36','content-type':'application/x-www-form-urlencoded','Accept':'*/*','Origin':'https://ifa2012.com','X-Requested-With':'mark.via.gp','Sec-Fetch-Site':'same-site','Sec-Fetch-Mode':'cors','Sec-Fetch-Dest':'empty','Referer':'https://ifa2012.com/','Accept-Encoding':'gzip, deflate','Accept-Language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7'},data={'lang':'EGY','username':user,'password':user,'code_value':'','code_key':'939f9965ad12335f246fb0ad9e0e77d8'})

            if "عملية ناجحة" in login.text:

                token = login.json()['data']['token']

                key = login.json()['data']['token_key']

                money = requests.post('https://api.ifa2012.com/my/info',headers={'Host':'api.ifa2012.com','Connection':'keep-alive','Content-Length':'68','lang':'EGY','usertoken':token,'usertokenkey':key,'User-Agent':'Mozilla/5.0 (Linux; Android 8.1.0; SM-T585 Build/M1AJQ;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Safari/537.36','content-type':'application/x-www-form-urlencoded','Accept':'*/*','Origin':'https://ifa2012.com','X-Requested-With':'mark.via.gp','Sec-Fetch-Site':'same-site','Sec-Fetch-Mode':'cors','Sec-Fetch-Dest':'empty','Referer':'https://ifa2012.com/','Accept-Encoding':'gzip, deflate','Accept-Language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7'},data={'lang':'EGY'}).json()['data']['balance1']

                task = requests.post('https://api.ifa2012.com/match/buy',headers={'Host':'api.ifa2012.com','Connection':'keep-alive','Content-Length':'68','lang':'EGY','usertoken':token,'usertokenkey':key,'User-Agent':'Mozilla/5.0 (Linux; Android 8.1.0; SM-T585 Build/M1AJQ;) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 Safari/537.36','content-type':'application/x-www-form-urlencoded','Accept':'*/*','Origin':'https://ifa2012.com','X-Requested-With':'mark.via.gp','Sec-Fetch-Site':'same-site','Sec-Fetch-Mode':'cors','Sec-Fetch-Dest':'empty','Referer':'https://ifa2012.com/','Accept-Encoding':'gzip, deflate','Accept-Language':'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7'},data={'lang':'EGY','sc_id':data[chat_id][1],'bd_id':data[chat_id][2],'zd_type':'2','money':money,'money_type':'1'}).text

                if "عملية ناجحة" in task:

                    d = d + 1

                    bot.send_message(message.chat.id, text=f"Task Completed Successfully {user}")

                else:

                    e = e + 1

            else:

                e = e + 1

            mas = types.InlineKeyboardMarkup(row_width=2)

            Error = types.InlineKeyboardButton(text=f"Error : {e} ", callback_data="Error")

            Done = types.InlineKeyboardButton(text=f"Done : {d} ", callback_data="Done")

            mas.add(Error, Done)

            bot.edit_message_text(text=f'⏳ Please Wait ...', chat_id=int(message.chat.id), message_id=messages.message_id, reply_markup=mas)

        bot.edit_message_text(text=f'End', chat_id=int(message.chat.id), message_id=messages.message_id)

@bot.callback_query_handler(func=lambda call: True)

def callbacks_data(call):

    if call.data == "Start":

        Code(call.message)

while True:

    try:

        print("Done")

        bot.polling(True)

        break

    except Exception as ex:

        print(f"Error polling : {ex}")

        telebot.logger.error(ex)

        continue
