from typing import Final
import os
from discord import Intents, Client, Message, User
from dotenv import load_dotenv
from bot_response import get_bot_response


TARGET_USER: Final[str] = "wonoppa_"

load_dotenv()
TOKEN: Final[str] = os.getenv("DISCORD_TOKEN")

intents: Intents = Intents.default()
intents.message_content = True # NOQA
# intents.messages = True
# intents.guilds = True
# intents.members = True
client: Client = Client(intents=intents)

async def send_message(message: Message, user_message: str) -> None:
    if message.author.name == TARGET_USER:
        if not user_message:
            print("(Message was empty because intents were not enabled)")
            return

        if is_private := user_message[0] == "?":
            user_message = user_message[1:]
        
        try:
            response: str = get_bot_response(user_message=user_message)
            response = f"{message.author.mention} {response}"
            await message.author.send(response) if is_private else await message.channel.send(response)
        except Exception as ex:
            print(ex)
            
@client.event
async def on_ready() -> None:
    print(f"{client.user} is now running!")
    
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)
    
    print(f"[{channel}] {username}: {user_message}")
    await send_message(message=message, user_message=user_message)

def main() -> None:
    client.run(token=TOKEN)
    
if __name__ == '__main__':
    main()