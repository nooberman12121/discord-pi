import os
from dotenv.main import load_dotenv
from nextcord.ext import commands


def main():
    client = commands.Bot(command_prefix="%")

    load_dotenv()

    @client.event
    async def on_ready():
        print(f"{client.user.name} has connected to discord.")

    for folder in os.listdir("cogs"):
        if os.path.exists(os.path.join("cogs", folder, "cog.py")):
            client.load_extension(f"cogs.{folder}.cog")




    client.run(os.getenv("DISCORD_TOKEN"))

if __name__ == "__main__":
    main()