import discord
from discord.ext import commands
import os
import asyncio
import random
import urllib
from bs4 import BeautifulSoup
from urllib.request import Request
from urllib import parse
import bs4
import time

client = discord.Client()

@client.event
async def on_ready():
    print('봇이 로그인 하였습니다.')
    print(' ')
    print('닉네임 : {}'.format(client.user.name))
    print('아이디 : {}'.format(client.user.id))

@client.event
async def on_member_join(member):
    try:
        syscha = member.guild.system_channel
        await syscha.send(f"{member.mention}님 안녕하세요. ")
    except:
        pass

@client.event
async def on_message(message):
    if message.content == '>Oahwid 0420':
        syscha = message.channel
        embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
        embed.add_field(name="잠시만 기다리세요...", value="가입 진행중", inline=True)
        embed.set_footer(text=f"{message.author}, 회원으로 인증됨", icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)
        time.sleep(8)
        await message.delete()
        embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
        await syscha.send(f"{message.author.mention} 님은 OA게임 참가자 역할이 지급되었습니다.")
        role = discord.utils.get(message.author.guild.roles, name='OA참가자')
        await message.author.add_roles(role)

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)