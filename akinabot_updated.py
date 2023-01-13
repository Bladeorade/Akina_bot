
import discord
import random
import discord.ext
from discord.ext import commands
from easy_pil import Editor, load_image_async, Font
from discord import File
import giphy_client
from giphy_client.rest import ApiException


intent = discord.Intents.all()
client = commands.Bot(command_prefix=';', intents=discord.Intents.all())
akina_kick = 'akinakick.gif'
akina_ban = 'akinachop.gif'


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}!')


@client.command()
async def gif(ctx, *, q='Akina'):
    api_key = 'insert your own key'
    api_instance = giphy_client.DefaultApi()

    try:
        api_response = api_instance.gifs_search_get(
            api_key, q, limit=5, rating='g')
        lst = list(api_response.data)
        giff = random.choice(lst)

        embed = discord.Embed(title=q)
        embed.set_image(
            url=f'https://media.giphy.com/media/{giff.id}/giphy.gif')
        await ctx.channel.send(embed=embed)
    except ApiException as r:
        print('Exception for the api')

client.remove_command('help')

# embedded help command.


@client.command()
async def help(ctx):
    embed = discord.Embed(title='AkinaBot Commands!',
                          description='Welcome to our help section! here are all the commands for AkinaBot.',
                          color=discord.Colour.orange())
    embed.set_thumbnail(
        url='https://i.pinimg.com/736x/b3/cf/1c/b3cf1c632b41d490131eaa75a3cfe95c.jpg')
    embed.add_field(
        name=';help', value='Lists all commands AkinaBot can use.', inline=False)
    embed.add_field(
        name=';akina smile', value='Sends random gif of Akina smiling.', inline=False)
    embed.add_field(
        name=';akina fact', value='Gives a random fact abut Akina Nakamori.', inline=False)
    embed.add_field(
        name=';kick', value='Kicks a member from the server (given you have privledges to do so)', inline=False
    )
    embed.add_field(
        name=';ban', value='Bans a member from the server (given you have privledges to do so)', inline=False
    )
    embed.add_field(
        name=';gif [any word]', value='sends a gif from giphy API related to any keyword put after ;gif', inline=False
    )
    embed.add_field(
        name=';akina shoot', value='Akina shoots gun gif', inline=False
    )
    embed.add_field(name=';akina best',
                    value='Sends best of Akina Nakamori music playlist.', inline=False)
    embed.add_field(name=';akina random',
                    value='Sends a random Akina Nakamori song.', inline=False)
    await ctx.channel.send(embed=embed)


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    if reason == None:
        reason = 'no reason provided'
    await ctx.guild.kick(member)
    await ctx.send(f'User {member.mention} has been kicked for {reason}')
    await ctx.channel.send(file=discord.File(akina_kick))

# ban command


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    if reason == None:
        reason = 'no reason provided'
    await ctx.guild.ban(member)
    await ctx.send(f'User {member.mention} has been banned for {reason}')
    await ctx.channel.send(file=discord.File(akina_ban))


@client.event
async def on_member_join(member):
    channel = member.guild.system_channel
    background = Editor('akina_new.jpg')
    profile_image = await load_image_async(str(member.avatar.url))
    profile = Editor(profile_image).resize((150, 150)).circle_image()
    poppins = Font.poppins(size=50, variant='bold')
    poppins_small = Font.poppins(size=20, variant='light')

    background.paste(profile, (325, 90))
    background.ellipse((325, 90), 150, 150, outline='white', stroke_width=5)

    background.text(
        (400, 260), f'Welcome To {member.guild.name}!', color='white', font=poppins, align='center')
    background.text((400, 325), f'{member.name}#{member.discriminator}',
                    color='white', font=poppins_small, align='center')

    file = File(fp=background.image_bytes, filename='akina_new.jpg')
    await channel.send(f'Hello {member.mention}! Welcome to **{member.guild.name}!** Please view #rules to get started!')
    await channel.send(file=file)


@client.event
async def on_message(message):
    await client.process_commands(message)
    if message.author.name == client.user:
        return
    if message.content.startswith(';akina hello'):
        await message.channel.send('''
        https://tenor.com/view/ミアモーレ-中森明菜-nakamori-akina-アイドル-gif-25981265
        Hello!''')
    elif message.content.startswith(';akina fact'):
        akina_fact = ['Did you know Akina\'s second single "Shōjo A" was nearly banned for it\'s risque lyrics?',
                      'Did you know Akina took balet lessons from the age of 4 to 13?',
                      'Akina\'s favorite flowers are casablanca\'s!',
                      'Akina entered the music industry through a music talent show called "Star Tanjō!"',
                      'Akina does not like using mobile phones and thus, doesn\'t own one',
                      'Akina\'s personal website is: https://nakamoriakina.com',
                      'Akina made her debut in 1982 with the single "Slow Motion." Recorded in Los Angeles, the single was released on 1 May 1982 and sold 174,000 copies, reaching No. 30 on the Oricon charts!',
                      'Akina was born on July 13th, 1965 in Kiyose City, Tokyo, Japan',
                      'Akina\'s hobbies include: Acting, Ballet, Cooking, Photography, Fashion, Knitting, Music, Knitting, Pencil-Sketching, Pottery, Reading, and Travelling!',
                      '']
        await message.channel.send(random.choice(akina_fact))
    elif message.content.startswith(';akina smile'):
        smile_gif = [
            'https://tenor.com/view/akina-nakamori-nakamori-akina-gif-6734098',
            'https://tenor.com/view/v8k00-akina-nakamori-gif-25056690',
            'https://tenor.com/view/akina-nakamori-nakamori-akina-gif-6732624',
            'https://tenor.com/view/jgirlsrock-akina-nakamori-laugh-gif-26497224',
            'https://tenor.com/view/jgirlsrock-akina-nakamori-laugh-gif-26496855',
            'https://tenor.com/view/ザベストテン-少女a-中森明菜-nakamori-akina-アイドル-gif-25626034',
            'https://tenor.com/view/jgirlsrock-akina-nakamori-agree-gif-26497916',
            'https://tenor.com/view/jgirlsrock-akina-nakamori-eat-gif-26496906',
            'https://tenor.com/view/jgirlsrock-akina-nakamori-scared-gif-26496864',
            'https://tenor.com/view/akina-akina-nakamori-中森明菜-gif-24322682',
            'https://tenor.com/view/中森明菜-nakamori-akina-アイドル-gif-25626275',
            'https://tenor.com/view/セカンドラブ-中森明菜-nakamori-akina-ザベストテン-アイドル-gif-26201681',
            'https://tenor.com/view/ミアモーレ-中森明菜-nakamori-akina-アイドル-gif-25981267',
            'https://tenor.com/view/冷たい月-中森明菜-nakamori-akina-アイドル-gif-25834120',
            'https://tenor.com/view/セカンドラブ-中森明菜-nakamori-akina-ザベストテン-アイドル-gif-26201685',
            'https://tenor.com/view/中森明菜-nakamori-akina-アイドル-gif-25834315', ]
        await message.channel.send(random.choice(smile_gif))
    elif message.content.startswith(';akina shoot'):
        await message.channel.send('https://tenor.com/view/akira-nakamori-nakamori-gun-jgirlsrock-pistol-gif-25854398')
    elif message.content.startswith(';akina best'):
        await message.channel.send('https://www.youtube.com/watch?v=q9Ml7hzAq8U')
    elif message.content.startswith(';akina random'):
        akina_songs = ['https://www.youtube.com/watch?v=_uRh3jnZMFM',
                       'https://www.youtube.com/watch?v=c2QJmSpZ5BM',
                       'https://www.youtube.com/watch?v=hTgU11h-2Ik',
                       'https://www.youtube.com/watch?v=qjlvUXWmeyM',
                       'https://www.youtube.com/watch?v=fPu7FatJIPM',
                       'https://www.youtube.com/watch?v=BsBgkv34DuQ',
                       'https://www.youtube.com/watch?v=SZPf872yjGc',
                       'https://www.youtube.com/watch?v=rBoXhJXljPQ',
                       'https://www.youtube.com/watch?v=Ofgy2OIHA1w',
                       'https://www.youtube.com/watch?v=KNkgoq-xBCM',
                       'https://www.youtube.com/watch?v=4VW8K_8PCzg&list=OLAK5uy_kQuWYVkmq45vLEVE1Y-Hilt-TZUY-Rs80',
                       'https://www.youtube.com/watch?v=BihAmkqcGKU&list=OLAK5uy_kQuWYVkmq45vLEVE1Y-Hilt-TZUY-Rs80&index=2]',
                       'https://www.youtube.com/watch?v=c_YwhGOGCMs&list=OLAK5uy_m4XEuMnvJGwnM5U9K6_1sAr4my3GopwzI'
                       ]

        await message.channel.send(random.choice(akina_songs))
client.run(
    'import your bot token.')
