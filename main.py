import discord
import joke
import os

class myClient(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}!")


    async def on_message(self, message):
        if message.author == client.user:
            return
        elif message.content.startswith("!hello") or message.content.startswith("!hi"):
            await message.channel.send("Greetings! Want to hear a joke?")
            
            def check_authors(reply):
                return reply.author == message.author
    
            res = await client.wait_for('message', check = check_authors)
            
            if res.content.lower().startswith("y"):
                the_joke = joke.get_joke()
                await message.channel.send(the_joke)
            else:
                await message.channel.send("Let me know if you change your mind")

        elif message.content.startswith('!joke'):
            the_joke = joke.get_joke()
            await message.channel.send(the_joke)


client = myClient()
client.run(f"{os.getenv('client_key')}")