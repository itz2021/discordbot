import discord
from captcha.image import ImageCaptcha
import random
import time
import asyncio

client = discord.Client()
token = 'ODUxODc2Njc0MDU1ODMxNjEz.YL-p-g.Sc0EspFXDAs5U0DxYqQumauZ0F4'
gaming = '문의 : 이츠#2900'
channel = '852582542502264893'

@client.event
async def on_ready():
    print("discord : 이츠#2900")
    game = discord.Game(gaming)
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("!인증"):    #명령어 !인증
        if not message.channel.id == int(channel):
            return
        a = ""
        Captcha_img = ImageCaptcha()
        for i in range(6):
            a += str(random.randint(0, 9))

        name = str(message.author. id) + ".png"
        Captcha_img.write(a, name)

        await message.channel.send(f"""{message.author.mention} 아래 숫자를 10초 안에 입력해주세요 """)
        await message.channel.send(file=discord.File(name))

        def check(msg):
            return msg.author == message.author and msg.channel == message.channel

        try:
            msg = await client.wait_for("message", timeout=10, check=check) # 제한시간 10초
        except:
            await message.channel.purge(limit=3)
            tjdrhdEmbed = discord.Embed(title='등업실패', color=0xfcfcfc)
            tjdrhdEmbed.add_field(name='닉네임', value=message.author, inline=False)
            tjdrhdEmbed.add_field(name='사유', value='시간초과', inline=False)
            tjdrhdEmbed.set_thumbnail(url=message.author.avatar_url)
            await message.channel.send(embed=tjdrhdEmbed)
            print(f'{message.author} 님이 시간초과로 인해 등업을 실패함.')
            return

        if msg.content == a:
            role = discord.utils.get(message.guild.roles, name="짱짱고수")
            await message.channel.purge(limit=4)
            tjdrhdEmbed = discord.Embed(title='인증성공', color=0xfcfcfc)
            tjdrhdEmbed.add_field(name='닉네임', value=message.author, inline=False)
            tjdrhdEmbed.add_field(name='3초후 인증역할이 부여됩니다.', value='** **', inline=False)
            tjdrhdEmbed.set_thumbnail(url=message.author.avatar_url)
            await message.channel.send(embed=tjdrhdEmbed)
            print(f'{message.author} 님이 등업을 성공함.')
            await asyncio.sleep(3)
            await message.author.add_roles(role)
        else:
            await message.channel.purge(limit=3)
            tjdrhdEmbed = discord.Embed(title='등업실패', color=0xfcfcfc)
            tjdrhdEmbed.add_field(name='닉네임', value=message.author, inline=False)
            tjdrhdEmbed.add_field(name='사유', value='틀린숫자', inline=False)
            tjdrhdEmbed.set_thumbnail(url=message.author.avatar_url)
            await message.channel.send(embed=tjdrhdEmbed)
            print(f'{message.author} 님이 틀린숫자로 인해 등업을 실패함.')

client.run(token)