from telethon import TelegramClient, events
import telebot
import re

api_id = 7579425
api_hash = '1a408061ca6bd91023fca3ba39451111'
client = TelegramClient('dk', api_id, api_hash)
TOKEN ='2080552138:AAGZ_hghChvoCnA17vutzgMK0viVEsRutms'
bot = telebot.TeleBot(TOKEN)
from_channel = '@Fancodefastline'
to_channel = '@kokoihbh'


print("Connected")
def join_list(aid, atext):
    for item in ms:
        if item['txt'] == atext:
            item['toid'] = aid
        
#Variables
ms = []
t=0

print("Running...")
@client.on(events.NewMessage(chats=from_channel))
async def forwardhandler(event):
    txt = event.text
    txt = re.sub(r'^https?:\/\/.*[\r\n]*', '', re.sub(' +', ' ',txt), flags=re.MULTILINE)
    txt = '*'+txt+'*'
    bot.send_message(to_channel, '{}'.format(txt), parse_mode= "Markdown")
    ms.append({'txt':txt.strip('*'), 'fromid':event.message.id})


@client.on(events.NewMessage(chats=to_channel))
async def forwardhandler(event):
    global ms, t
    if t == 20:
        ms = []
        t = 0
    txt = event.text
    join_list(event.message.id, txt.strip('**'))
    t += 1

@client.on(events.MessageDeleted(chats=from_channel))
async def delete(message):
    for item in ms:
        if int(item['fromid'])==message.deleted_id:
            bot.delete_message(to_channel, int(item['toid']))

@client.on(events.MessageEdited(chats=from_channel))
async def edit(event):
    for item in ms:
        if event.message.id in item.values():
            txt = re.sub(' +', ' ',event.message.message)
            await client.edit_message(to_channel, int(item['toid']) ,"**{}**".format(txt, item['fromid']), parse_mode= "Markdown")


client.start()
client.run_until_disconnected()