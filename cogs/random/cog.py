from nextcord.ext import commands
import random

class Random(commands.Cog, name="Random"):
    """Random category"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @commands.command()
    async def roll(self, ctx: commands.Context, dice: str):
        """
        Rolls a given amount of dice in the form _d_

        Example: %roll 2d6
        """
        try:
            rolls = ""
            total = 0
            amount, die = dice.split("d")
            for _ in range(int(amount)):
                roll = random.randint(1, int(die))
                total += roll
                rolls += f"{roll} "
            await ctx.send(f"Rolls: {rolls}\nSum: {total}")
        except ValueError:
            await ctx.send("Dice must be in the format of `_d_` (example: `2d6`)")
    
    @commands.command()
    async def choose(self, ctx: commands.Context, *arg):
        """
        Chooses an option
        
        Example: %choose "option1" "option2" "option3"
        """

        
    
        choice = random.choice(arg)
        await ctx.send(f"I choose: {choice}")


def setup(bot: commands.Bot):
    bot.add_cog(Random(bot))