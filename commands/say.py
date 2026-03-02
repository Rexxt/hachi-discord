async def say(commands, bot, conf, message, rm):
    what_to_say = rm.group(1)

    await message.channel.send(what_to_say)
    await message.delete()

command = {
    'example': 'say <something> [stealthily/anonymously]',
    'help_text': 'repeats what you tell me to',
    'regex': 'say +(.+)',
    'function': say
}