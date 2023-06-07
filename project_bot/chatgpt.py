from telethon import events
from .. import bot,openai_key
import telethon 
import asyncio
import openai

from telethon.tl.custom import Button


openai.api_key = openai_key
model_engine="gpt-3.5-turbo"

k_board = [[Button.inline("stop and reset", b"stopgpt")]]




@bot.on(events.NewMessage(incoming = True, pattern = "(?i)/ask"))
async def _gpt(event):
  sender_id = event.sender_id
  gpt_msg= "Hello! I am GaBBaR Ai that can answer most of your questions."
  try:
    await bot.send_message(sender_id, gpt_msg)
    async with bot.conversation(await event.get_chat(), exclusive= True, timeout=600) as conv:
      history= []
      
      while True:
        gpt_msg = "send your question "
        u_input = await send_recive(gpt_msg,conv, k_board)
        if u_input is None:
          gpt_msg = "Conversation reset. Type /ask to start a new one  "
          await bot.send_message(sender_id, gpt_msg)
          break
        else:
          gpt_msg = "I got your message wait for a sec.."
          ab = await bot.send_message(sender_id,gpt_msg)
          history.append({"role": "user", "content": u_input})
          c_comp = openai.chatcompletion.create(model= model_engine,
            messages = history, 
            max_token = 100,
            n=1,
            temperature = 0.100
            )
          response = c_comp.choices[0].message.content
          history.append({"role":"assistant","content": response})
          await ab.delete()
          await bot.send_message(sender_id, response, parse_mode="Markdown")
  except asyncio.TimeoutError:
    await bot.send_message(sender_id, "conversation ended due to no response")
    return 
  except telethon.errors.AlredyInConversationError:
    pass
  except Exception as e:
    print(e)
    await bot.send_message(sender_id, " conversation ended . something went wrong")
    return
  
  
  
async def send_recive(gpt_msg, conv, keyboard):
    msg = await conv.send_message(gpt_msg, buttons = keyboard)
    done, _ = await asyncio.wait({conv.wait_event(events.CallbackQuery()), conv.get_response()}, return_when = asyncio.FIRST_COMPLETED)
    result = done.pop().result()
    await message.delete()
    
    if isinstance(result,events.CallbackQuery.Event):
      return None
    else: 
      return result.message.strip()