import discord
from discord.ext import commands, tasks
import web , apen
import threading
import time
import asyncio
import os





intents = discord.Intents.default()
intents.typing = False
intents.presences = False





#set the bot
bot = commands.Bot(command_prefix='!', intents=intents)





@bot.event
async def on_ready():
    print('Bot is ready.')

    

   
async def send_message_to_user(user_id, message, number):
    user = await bot.fetch_user(user_id)
    await user.send(message)

    def check_response(response_message):
        return response_message.author == user

    try:
        response = await bot.wait_for('message', check=check_response)  # wait indefinitely for a response
    except asyncio.TimeoutError:
        await user.send('You did not respond in time!')
    else:
        with open('data/' + number + 'd.txt', 'w') as file:  # replace 'response_file.txt' with your actual file name
            file.write(response.content)  # store the user's response in the file
        await asyncio.sleep(15)
                



@tasks.loop()
async def file_check(number):
    print("checking")
    with open('data/'+number+'d.txt', 'r') as file:
        content = file.read().strip()
        if content!="":
            await send_message_to_user(986531455918288969, content, number)
    await asyncio.sleep(15)

@file_check.before_loop
async def before_file_check():
    global should_continue
    should_continue = True

@file_check.after_loop
async def after_file_check():
    global should_continue
    if not should_continue:
        file_check.stop()




"""
@bot.command()
async def chat(ctx, *, message):
    response = a.chat(message)
    f.write(response+"\n"+message)
    await ctx.send(response)
"""



#fix this




    
@bot.command()
async def start(ctx):
    #t = threading.Timer(500.0, timeout_function)
    #t.start()
    web.start_browser()

    await ctx.send("Please input the phone number of the person")
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    msg = await bot.wait_for('message', check=check)
    number=msg.content

    a=open("data/"+number+".txt","x")
    f=open("data/"+number+".txt","a")

    

    await ctx.send("Please input the who the of the person is to you and I want goals")
    msg = await bot.wait_for('message', check=check)
    person=apen.openinstial(msg.content)
    

    

    await ctx.send("Please input the name of the person to you")
    msg = await bot.wait_for('message', check=check)
    name=msg.content
   

    await ctx.send("Please input the context ")
    msg = await bot.wait_for('message', check=check)
    context=msg.content
    

    await ctx.send("Who am I to this person")
    msg = await bot.wait_for('message', check=check)
    info=msg.content

    await ctx.send("Do you want questions on 1=on")
    msg = await bot.wait_for('message', check=check)
    q1=msg.content

    extra="Please make sure that you will only respond to the message JUST THE REPONSE NOTHING ELSE unless the response back starts with M.. YOU WILL NOT BE PRETENDING TO BE THE OTHER PERSON YOU WILL PERTEND TO BE ME AND YOU ONLY RESPOND AS ME. Please make sure that you start out with the message for the person so please dont aknowlage anything just start."

   

    everything="Person I want you to talk to and goals:"+person+"\nWhat I want to call the person by: "+name+"\nContext of the person you are talking to:"+context+"\nWho I am to this person:"+info+"\n"+extra


    e=apen.openinstial(everything)

    while True:
        await ctx.send("Please enter 1 to exit:"+e)
        msg = await bot.wait_for('message', check=check)
        das=msg.content
        if das=="1":
            break
        e=apen.openinstial(das) 
  

    with open("data/"+number+".txt", 'w', encoding='utf-8') as f:
        f.write(number+"\n<")
        f.write(everything+"\n<")
        f.write(e+"\n<")
    
    file_check.start(number)
    start_thread(e , number, name,q1)
    #please also add the name to the person
    #please change this a little bit
    



def timeout_function():
    print("Timeout!")
    raise SystemExit

class StoppableThread(threading.Thread):
    def __init__(self, target, args):
        super().__init__(target=target, args=args)
        self._stop_flag = threading.Event()

    def stop(self):
        self._stop_flag.set()

    def run(self):
        while not self._stop_flag.is_set():
            super().run()
            time.sleep(1)


stoppable_thread = None


should_continue = True

def start_thread(e, number, name,q1):
    global stoppable_thread
    stoppable_thread = StoppableThread(target=web.typethis, args=(e, number, name, q1))
    stoppable_thread.start()


def stop_thread():
    global stoppable_thread
    if stoppable_thread:
        stoppable_thread.stop()
#the thread does not work




"""
@bot.command()
async def end(ctx):
    await ctx.send("ending the conversation")
    #do a better job then this

    web.quit_browser()
    web.start_browser()
"""

@bot.command()
async def stop(ctx, message):
    await ctx.send("ending the conversation")
    with open("data/"+message+"e.txt", "w") as f:
        f.write("1")
    file_check.cancel()


#change
@bot.command()
async def sum(ctx):
    await ctx.send("summerizing the conversation")
    await ctx.send("Please input the phone number of the person")
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    msg = await bot.wait_for('message', check=check)
    number=msg.content
    data=apen.opensum(number)
    await ctx.send(data)





@bot.command()
async def end(ctx):
    await ctx.send("Stopping the bot...")
    web.quit_browser()
    await bot.close()


bot.run('MTEyNzQ3MTQxNjMzMDE3NDUzNQ.GYwgmX.JoPdg2h70WajmDif45NVTqOsM5OW5za3cR8o4I')


