from .. import tgbot,openai_key
from telethon import events
import asyncio 
import openai

openai.my_api_key = openai_key

@tgbot.on(events.NewMessage(incoming = True, pattern="/start")) 
async def start(event):
  await event.reply("Hello! GaBBaR this side. How can I help you?")


@tgbot.on(events.NewMessage(incoming = True, pattern="/get")) 

async def start(event):
  a=await event.reply("get command is started")
  await asyncio.sleep(9)
  await a.edit("This is edited message ")



@tgbot.on(events.NewMessage(incoming = True, pattern="/eval")) 

async def start(event):

  await event.reply("eval cammand is started")
    
    
 
    
    
    