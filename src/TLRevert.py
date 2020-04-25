#!/usr/bin/python3
import sqlite3, os
from sys import exit
from telethon.sync import TelegramClient
from getpass import getpass
from telethon.utils import get_peer_id

__version__ = '1.0'
api_id = YOUR_API_ID_HERE
api_hash = 'YOUR_API_HASH_HERE'
TLdevice_model = 'Desktop device'
TLsystem_version = 'Console'
TLapp_version = '- TLRevert ' + __version__
TLlang_code = 'en'
TLsystem_lang_code = 'en'
SelfUser1 = None
message_ids = []
target_dialog = None
target_id = None

client1 = TelegramClient('User1', api_id, api_hash, device_model=TLdevice_model, system_version=TLsystem_version, app_version=TLapp_version, lang_code=TLlang_code, system_lang_code=TLsystem_lang_code)

class InvalidUser(Exception):
    pass

def StartClient1():
    global client1, SelfUser1
    try:
        client1.connect()
        if not client1.is_user_authorized():
            client1.start(force_sms=False)
        SelfUser1 = client1.get_me()
    except:
        if not client1.is_connected():
            getpass("You are not connected to the internet or the phone was given in the incorrect format. Check your connection and press ENTER to try again: ")
        StartClient1()
    return

def extractData(filepath):
    global target_id
    try:
        user_number1 = None
        nameuser1 = None
        nameuser2 = None
        connection = sqlite3.connect(filepath)
        cur = connection.cursor()
        cur.execute("SELECT * FROM Statistics LIMIT 1")
        for row in cur:
            nameuser1 = row[2]
            nameuser2 = row[3]
            if SelfUser1.id == row[0]:
                user_number1 = True
                target_id = row[1]
            elif SelfUser1.id == row[1]:
                user_number1 = False
                target_id = row[0]
            else:
                raise InvalidUser
        cur.execute("SELECT * FROM SentMessagesIDs")
        for row in cur:
            if user_number1 and row[0] is not None:
                message_ids.append(row[0])
            elif not user_number1 and row[1] is not None:
                message_ids.append(row[1])
        cur.execute("SELECT * FROM version LIMIT 1")
        for row in cur:
            appname = row[0]
            creation_date = row[2]
        cur.close()
        connection.close()
        del nameuser1, nameuser2, user_number1
        return appname, creation_date
    except InvalidUser:
        print("\nYou logged in with an account that wasn't involved in the data present in this database. " + \
            "Maybe you ran the tools multiple times and you mixed up the databases and the accounts?")
        print("These are the users involved in this database:")
        print("· " + nameuser1)
        print("· " + nameuser2)
        getpass("\nTLRevert will close (so you can start again from scratch) and will log out the Telegram session is using" +\
            ", so you can log in with the appropiate account. Press ENTER: ")
        client1.log_out()
        exit(1)
    except:
        getpass("\nThis database is not valid. TLRevert will exit now. Press ENTER: ")
        exit(1)

def get_target_chat():
    global target_dialog, target_id
    dialogs = client1.get_dialogs(limit=None)
    for dialog in dialogs:
        if get_peer_id(dialog.entity) == target_id:
            target_dialog = dialog.entity

print("WELCOME TO TLREVERT!")
print("This script is going to help you in undo any action made by 'TLImporter' and 'TLMerger'. It will erase all the messages "+\
    "that are product of the merging or the importing of chats.")
getpass("\nNow, you need to log in to Telegram. Press ENTER to continue: ")
StartClient1()
print("\nYou are logged in as " + SelfUser1.first_name + "!")
print("\n\nNow, find the database that was created by the tool you used back in the day. " +\
    "It might be in 'Saved Messages' if you decided to save it there back in the day.")
while True:
    filepath = input("Path of the file: ")
    filepath = filepath.replace("\\", "/").replace("'", "").replace('"', '')
    if not os.path.isfile(filepath):
        print("No file was found in this path. Please, try again\n\n")
    else:
        break
print("\n\nVerifying that this is a valid database and fetching data...")
appname, creation_date = extractData(filepath)
print("\nEverything was correct. Doing the finishing touches...")
get_target_chat()
try:
    getpass("\n\nEverything is ready to undo the operations made by " + appname + " on " + creation_date + ". Press ENTER to confirm (CTRL + C to exit): ")
    print("\n\nDeleting messages...")
    client1.delete_messages(target_dialog, message_ids, revoke=True)
except KeyboardInterrupt:
    exit(0)
getpass("\nDone! Thank you very much for using TLRevert -ferferga.\n\nPress ENTER to log you out and exit: ")
client1.log_out()
