import discord
from discord.ext import commands
import openai

# Replace 'YOUR_BOT_TOKEN' and 'YOUR_OPENAI_API_KEY' with your actual tokens
TOKEN = 'YOUR_BOT_TOKEN'
OPENAI_API_KEY = 'YOUR_OPENAI_API_KEY'

# Define intents
intents = discord.Intents.default()
intents.message_content = True  # Make sure to enable this to read message content

# Set up the bot with a command prefix and intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Change the BASE_URL with the oficial openai base url or with a proxy
openai.api_key = OPENAI_API_KEY
openai.api_base = "BASE_URL"  # Corrected base URL

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

@bot.command()
async def chat(ctx, *, message: str):
    """
    This command lets you chat with a version of chatgpt
    """

    # Interact with OpenAI's API, Change the MODEL into the model of the ChatGPT/Roleplay AI that you will be using if you are using a proxy try to mess araund with it if the tutorial does not say what to do
    try:
        completion = openai.ChatCompletion.create(
            model="MODEL",  # Example model, update if needed
            messages=[
                {"role": "user", "content": (message)},
            ],
        )

        # Send the OpenAI response back to the user
        response = completion.choices[0].message['content']
        await ctx.send(response)
    except Exception as e:
        await ctx.send(f"Error: {str(e)}")

# Run the bot
bot.run(TOKEN)
