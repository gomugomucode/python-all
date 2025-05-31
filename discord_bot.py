# DICORD CODE FOR AI CHAT BOT


import discord
import random
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()  # Loads from .env file
token = os.getenv("DISCORD_TOKEN")

if not token:
    raise ValueError("DISCORD_TOKEN not found in environment variables")


# Setup intents to allow reading messages
intents = discord.Intents.default()
intents.message_content = True

# Initialize the bot with '!' as the command prefix
bot = commands.Bot(command_prefix="!", intents=intents)

jokes = [
    "Why don’t scientists trust atoms? Because they make up everything!",
    "I told my computer I needed a break, and it said: 'No problem, I’ll go to sleep.'",
    "Why was the math book sad? It had too many problems."
]

helpful_links = [
    ("Python Docs", "https://docs.python.org/3/"),
    ("W3Schools", "https://www.w3schools.com/"),
    ("Stack Overflow", "https://stackoverflow.com/"),
    ("GeeksforGeeks", "https://www.geeksforgeeks.org/"),
    ("freeCodeCamp", "https://www.freecodecamp.org/"),
]


quotes = [
    "“The best way to get started is to quit talking and begin doing.” – Walt Disney",
    "“Success is not final; failure is not fatal: It is the courage to continue that counts.” – Winston Churchill",
    "“Believe you can and you’re halfway there.” – Theodore Roosevelt"
]

motivations = [
    "You got this! Keep going 💪",
    "Push through the pain — success is near!",
    "Every expert was once a beginner. Keep learning 🔥"
]


@bot.event
async def on_ready():
    print(f"Bot is ready. Logged in as {bot.user}")


@bot.command()
async def joke(ctx):
    """Tells a random joke."""
    await ctx.send(random.choice(jokes))

@bot.command()
async def helpme(ctx):
    """Sends helpful programming resources."""
    # discord.embed = use to send the message 
    embed = discord.Embed(
        title="💡 Helpful Programming Resources",
        description="Here are some links that can guide your coding journey:",
        color=0x3498db
    )

    for name, url in helpful_links:
        embed.add_field(name=name, value=f"[Click here]({url})", inline=False)

    embed.set_footer(text="Happy coding, Genius")  
    await ctx.send(embed=embed)


@bot.command()
async def quote(ctx):
    """Sends a random inspirational quote."""
    await ctx.send(random.choice(quotes))

@bot.command()
async def motivate(ctx):
    """Sends a short motivational message."""
    await ctx.send(random.choice(motivations))

@bot.command()
async def about(ctx):
    """Describes the bot and its creator."""
    embed = discord.Embed(
        title="About This Bot",
        description="A helpful and humorous bot built by Anupam!",
        color=0x2ecc71
    )
    embed.add_field(name="Features", value="Jokes, Motivation, Learning Resources, Quotes", inline=False)
    embed.set_footer(text="Made with  Python")
    await ctx.send(embed=embed)





# bot.run(os.getenv("DISCORD_TOKEN"))


bot.run(token)

