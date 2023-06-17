import os

import aiohttp
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

# Set up the Discord bot
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="/", intents=intents, heartbeat_timeout=60)
TOKEN = os.getenv('DISCORD_TOKEN')  # Loads Discord bot token from env

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"{bot.user} aka {bot.user.name} has connected to Discord!")
    invite_link = discord.utils.oauth_url(
        bot.user.id,
        permissions=discord.Permissions(),
        scopes=("bot", "applications.commands")
    )
    print(f"Invite link: {invite_link}")
    await bot.change_presence(activity=discord.Activity(
        type=discord.ActivityType.PLAYING,
        name="Neko neko niki")
    )

@bot.hybrid_command(name="ping", description="Pings the bot! and returns the latency.")
async def ping(ctx):
    await ctx.send(f"Pong! {round(bot.latency * 1000)}ms")

@bot.hybrid_command(name="traceanime", description="Trace anime from screenshot")
async def get_attachments(ctx, attachment: discord.Attachment):
    await ctx.defer()
    async with aiohttp.ClientSession() as session:
        url = f"https://api.trace.moe/search?url={attachment.url}"
        async with session.get(url) as response:
            data = await response.json()
            
    embed = discord.Embed(title="Results")
    results = data.get('result', [])
    if results:
        for i, result in enumerate(results, start=1):
            similarity = result['similarity']
            if similarity >= 1:
                embed.add_field(name=f"# Result {i}", value="\u200b", inline=False)
                embed.add_field(name="Filename", value=result['filename'], inline=False)
                embed.add_field(name="Episode", value=result['episode'], inline=True)
                embed.add_field(name="Similarity", value=similarity, inline=True)
                embed.add_field(name="Video URL", value=result['video'], inline=False)
                embed.add_field(name="Image URL", value=result['image'], inline=False)
                embed.add_field(name="\u200b", value="\u200b", inline=False)
    else:
        embed.add_field(name="No Results", value="No results found.", inline=False)
        embed.add_field(name="\u200b", value="\u200b", inline=False)
    
bot.remove_command("help")

@bot.hybrid_command(name="help", description="Show all other commands")
async def help(ctx):
    embed = discord.Embed(title="Bot Commands", color=0x03a64b)
    embed.set_thumbnail(url=bot.user.avatar.url)
    command_tree = bot.commands
    for command in command_tree:
        if command.hidden:
            continue
        command_description = command.description or "No description available"
        embed.add_field(name=command.name,
                        value=command_description, inline=False)

    embed.set_footer(text=f"Made with love ♥️")

    await ctx.send(embed=embed)
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.author.mention} You do not have permission to use this command.")
    elif isinstance(error, commands.NotOwner):
        await ctx.send(f"{ctx.author.mention} Only the owner of the bot can use this command.")
        
bot.run(TOKEN)
