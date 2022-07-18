import os
import discord
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
my_secret = os.environ['Token']
from keep_alive import keep_alive
client = discord.Client()

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

@client.event
async def on_ready():

  print('We have logged in as {0.user}'.format(client))

  @client.event
  async def on_message(message):
    if message.author == client.user:
      return

    if message.content.startswith('!wiki'):
      name = message.content
      name = name.replace("!wiki", "")

      driver = webdriver.Chrome(options=chrome_options)
      driver.get("https://en.wikipedia.org/wiki/Main_Page")


      searchbutton =driver.find_element(By.NAME,'search')
      searchbutton.send_keys(name)

      loginbutton = driver.find_element(By.NAME, 'go')
      loginbutton.click()

      link = (driver.current_url)
      await message.channel.send(link)


keep_alive()
client.run(my_secret)