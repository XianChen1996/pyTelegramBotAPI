import telebot
import os
import random
import requests

token = input("Please enter your bot token: ")

picture_directory = r"C:\Users\10598\Desktop\pictures\老婆"

bot = telebot.TeleBot(token, parse_mode=None)  # You can set parse_mode by default. HTML or MARKDOWN


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "主人你好")


@bot.message_handler(regexp='我不会写程序')
def send_welcome(message):
    mention = "@godmt333 "  # Replace with the username of the user you want to mention
    message_text = f"{mention},救救孩子"
    bot.send_message(message.chat.id, message_text)


@bot.message_handler(commands=['jk'])
def send_welcome(message):
    # Get a list of all the files in the picture directory
    picture_files = os.listdir(picture_directory)
    picture_exists = False
    while not picture_exists and picture_files:
        # Choose a random picture file from the list
        picture_file = random.choice(picture_files)
        picture_number = os.path.splitext(picture_file)[0].split("_")[0]
        picture_url = f"https://www.pixiv.net/artworks/{picture_number}"
        response = requests.head(picture_url)
        if response.status_code == 200:
            picture_exists = True
        else:
            # Remove the chosen picture file from the list
            picture_files.remove(picture_file)

    if picture_exists:
        bot.send_message(message.chat.id, picture_url)
    else:
        bot.send_message(message.chat.id, "Sorry, no picture found.")


# Handles all text messages that contains the commands '/start' or '/help'.
@bot.message_handler(commands=['Go'])
def handle_start_help(message):
    bot.reply_to(message, "Go 语言怎么你了！")

@bot.message_handler(commands=['go'])
def handle_start_help(message):
    bot.reply_to(message, "要学go直接找zbh,https://github.com/hackroid")

@bot.message_handler(commands=['java'])
def handle_start_help(message):
    bot.reply_to(message, "要学java直接找gs,https://github.com/MGMCN")

@bot.message_handler(commands=['pytorch'])
def handle_start_help(message):
    bot.reply_to(message, "要学java直接找gy")

@bot.message_handler(regexp='色图')
def send_welcome(message):
    # Get a list of all the files in the picture directory
    picture_files = os.listdir(picture_directory)
    picture_exists = False
    while not picture_exists and picture_files:
        # Choose a random picture file from the list
        picture_file = random.choice(picture_files)
        picture_number = os.path.splitext(picture_file)[0].split("_")[0]
        picture_url = f"https://www.pixiv.net/artworks/{picture_number}"
        response = requests.head(picture_url)
        if response.status_code == 200:
            picture_exists = True
        else:
            # Remove the chosen picture file from the list
            picture_files.remove(picture_file)

    if picture_exists:
        bot.send_message(message.chat.id, picture_url)
    else:
        bot.send_message(message.chat.id, "Sorry, no picture found.")


@bot.message_handler(regexp="78")
def handle_message(message):
    bot.reply_to(message, "给我舔舔")


@bot.message_handler(func=lambda m: True)
def echo(message):
    if random.random() <= 0.1: # execute the function with 10% probability
        bot.reply_to(message, message.text + '我超市你')


if bot.get_me():
    print(f"Bot connected successfully! @{bot.get_me().username}")

else:
    print("Bot failed to connect. Please check your bot token.")

bot.polling()
