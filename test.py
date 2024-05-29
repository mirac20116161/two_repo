import discord
from discord.ext import commands
import random
import os
import requests


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('help'):
        await message.channel.send('çevre kirliliğini nasıl önleriz?,çevre kirliliği nedir?,çevre kirliliği en çok hangi ülkelerde var?,çevre kirliliği devam ederse dünyada neler olur?,gibi şeyler sorabilirsin')

    if message.content.startswith('çevre kirliliğini nasıl önleriz?'):
        await message.channel.send('yerlere,sulara çöp atmassak önleriz ')
 
    if message.content.startswith('çevre kirliliği nedir?'):
        await message.channel.send('Çevrenin canlı ve cansız öğelerini olumsuz yönde etkileyen, üzerinde yapısal zararlar meydana getiren ve niteliklerini bozan yabancı maddelerin hava, su ve toprağa yoğun bir şekilde karışması olayına “çevre kirliliği” adı verilmektedir. Çevrenin doğal olmayan bir şekilde insan eliyle bozulmasıdır.')

    if message.content.startswith('çevre kirliliği en çok hangi ülkelerde var?'):
        await message.channel.send('Dünyanın havası en kirli ülkeleri arasında ilk beşi Çad, Irak, Pakistan, Bahreyn ve Bangladeş oluşturdu.')

    if message.content.startswith('çevre kirliliği devam ederse dünyada neler olur?'):
        await message.channel.send('Bunlara bağlı olarak enerji kıtlığı,beslenme sorunları, canlı çeşitliliğinin azalması, toprakların kaybı, sağlık problemleri de gelişerek canlı yaşamının devamlılğını tehdit eder. Sadece insanlar için değil birçok kara ve deniz canlısı için de yaşam alanlarının daralmasına sebep olabilmekte.!')

