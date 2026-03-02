import datetime, time, random
async def ping(commands, bot, conf, message, rm):
    uptime = str(datetime.timedelta(seconds=int(round(time.time()-bot.start_time))))
    await message.channel.send(f'''my latency is {round(bot.latency*1000)}ms
i've been up for {uptime} (<t:{round(bot.start_time)}>)''')
    if time.time()-bot.start_time > 2*3600:
        await message.channel.send(random.choice(['i should get some sleep', 'i\'m feeling a little sleepy', 'i might doze off for a bit', 'im eepy']))

command = {
    'example': 'ping/how are you doing',
    'help_text': 'shows information about my status',
    'regex': '(ping|how +are +you +doing)',
    'function': ping
}