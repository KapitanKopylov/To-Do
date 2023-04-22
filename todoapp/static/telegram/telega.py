from pyrogram import Client
from time import sleep

def telega(a):
    app = Client("my_account")

    def pr(f):
        app.send_message(601766913, f)

    with app:
        pr(a)

telega(input())