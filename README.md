# DiscordBots

<details>
<summary>DiscordSpamer</summary> 

  https://github.com/SuperPypok/DiscordBots/blob/main/DiscordSpamer.py
  
## !WARNING!
This tool is just for improve your programming knowledge, so nothing abuse of this program is not related to the developer!

## About:
This bot simply spams into a user-defined channel.
  
## Custom code elements:
  
Enter the token of your discard bot here. `line 4`
```py
token = "token"
```

Specify here the Id of the channel where the spam should start. `line 9`
```py
channel = client.get_channel(id)
```

Enter the text the bot should spam here. `line 11`
```py
await channel.send("text")
```

#### Run the code and the spam bot is activated.

</details>

<details>
<summary>logger</summary> 

  https://github.com/SuperPypok/DiscordBots/blob/main/logger.py
  
![](https://media.discordapp.net/attachments/1014200166473023540/1097838882537611325/2023-04-18_151032.png)

![](https://media.discordapp.net/attachments/1014200166473023540/1097838882290151424/2023-04-18_151133.png)

![](https://media.discordapp.net/attachments/1014200166473023540/1097838882818637854/2023-04-18_151312.png)
![](https://cdn.discordapp.com/attachments/1014200166473023540/1097843975647395910/2023-04-18_174906.png)
  
## About:
A bot that receives information about each message the user sends and sends it to a separate channel.
  
## Custom code elements:  

Enter the token of your discard bot here. `line 7`
```py
token = "token"
```

Specify the channel ID of the channel in which you want to record logs. `line 21, 27, 33`
```py
channel = bot.get_channel(id)
```

Also in your bot's settings, enable these settings.
![](https://cdn.discordapp.com/attachments/1014200166473023540/1097855958333526026/2023-04-18_190721.png) 
 
</details>


<details>
<summary>DiscordRaider (Spamer 2.0)</summary> 
  
  https://github.com/SuperPypok/DiscordBots/blob/main/DiscordRaider.py
  
## !WARNING!
This tool is just for improve your programming knowledge, so nothing abuse of this program is not related to the developer!

## About:
A bot that spams text that the user has given it in a given channel. The bot also endlessly creates new text channels, the name can also be set to your own. <br/> Video: https://youtu.be/NC9CW0VwpEY

## IMPORTANT:
Enable these settings in your bot before running the code.
![](https://cdn.discordapp.com/attachments/1014200166473023540/1097855958333526026/2023-04-18_190721.png)
  
## Code: 
  
Specify the channel ID of the channel where the spam should start. `line 10`
```py
channel = bot.get_channel(id)
```

Insert the required values into these lines. `line 15 and 16`
```py
await channel.send("text")
await guild.create_text_channel("channel_name")
```
  
Enter the token of your discard bot here. `line 18`
```py
bot.run("YOUR TOKEN")
```  

</details
