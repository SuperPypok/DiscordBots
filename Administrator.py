import disnake, datetime
from disnake.ext import commands

report_channel = 0
muted_role_id = 0
bot = commands.Bot(command_prefix="!", help_command=None, intents=disnake.Intents.all(), test_guilds=None)  #In "test_guilds", None only if you want to make a public bot. If not, make a list consisting of the id of the servers the bot should run on ( `[id, id]` ).

@bot.event
async def on_ready():
    server_list = []
    for guild in bot.guilds:
        server_list.append(guild.name)
    print('Bot {0.user}'.format(bot), 'successfully launched!')
    print("List of servers the bot is added to: {}".format(", ".join(server_list)))

# Set report channel
@bot.slash_command(name="src", description="Какой канал должен хранить жалобы")
@commands.has_permissions(administrator=True)
async def set_report_channel(ctx, channel: disnake.TextChannel = commands.Param(description='Выберите канал в котором будут публиковаться жалобы')):
    global report_channel
    if not ctx.author.guild_permissions.administrator:
        return await ctx.send("У вас нет прав на выполнение этой команды.")
    report_channel = channel.id
    await ctx.send(f"Канал для репортов установлен на {channel.mention}.")

# Report command
@bot.slash_command(name='report', description="Пожалуйся на любого гондона")
async def report(ctx, *, reason: str = commands.Param(description='Причина жалобы'),
                 perpetrator: disnake.Member = commands.Param(description='Участник, на которого подается жалоба')):
    global report_channel
    if not report_channel:
        await ctx.send("Канал для жалоб не выбран. Используйте /src")
        return
    channel = bot.get_channel(report_channel)
    await channel.send(f"Новая жалоба от {ctx.author.display_name} на {perpetrator.display_name}: {reason}")
    await ctx.send(f"Жалоба отправлена на рассмотрение.")

# ban command
@bot.slash_command(name="ban", description="Забанить участника")
@commands.has_permissions(administrator=True)
async def ban(ctx, user: disnake.Member, *, reason: str = commands.Param(description="Причина бана:")):
    await user.ban(reason=reason)
    await ctx.send(f"{user} заблокирован по причине: {reason}")

# kick command
@bot.slash_command(name="kick", description="Кикнуть участника")
@commands.has_permissions(administrator=True)
async def kick(ctx, user: disnake.Member, *, reason: str = commands.Param(description="Причина кика:")):
    await user.kick(reason=reason)
    await ctx.send(f"{user} кикнут по причине: {reason}")

# select muted role
@bot.slash_command(name="select_mr", description="Выбрать роль за мута")
@commands.has_permissions(administrator=True)
async def select_mr(ctx, role: disnake.Role = commands.Param(description="Выберите роль, которая будет мутить пользователя")):
    global muted_role_id
    muted_role_id = role.id
    await ctx.send(f"Назначенная роль для мута: {role.mention}")

# mute command
@bot.slash_command(name="mute", description="Замутить пользователя")
@commands.has_permissions(administrator=True)
async def mute(ctx, member: disnake.Member = commands.Param(description="Выберите участника сервера"),
               reason: str = commands.Param(description="Укажите причину мута")):
    global muted_role_id
    if not muted_role_id:
        await ctx.send("Роль для мута не была выбрана. Используйте /select_mr.")
        return
    await member.add_roles(ctx.guild.get_role(muted_role_id))
    await ctx.send(f"{member.mention} был замучен. Причина: {reason}")

# unmute command
@bot.slash_command(name="unmute", description="Размутить пользователя")
@commands.has_permissions(administrator=True)
async def unmute(ctx, member: disnake.Member = commands.Param(description="Пользователь, которого нужно размутить")):
    await member.remove_roles(ctx.guild.get_role(muted_role_id))
    await ctx.send(f"{member.mention} был размучен.")

# timeout command
@bot.slash_command(name="timeout", description="Выдать тайм-аут участнику")
@commands.has_permissions(administrator=True)
async def timeout(ctx, reason, member: disnake.Member = commands.Param(description="Выберите участника сервера"),
                  time: str = commands.Param(description="Время в минутах")):
    time = datetime.datetime.now() + datetime.timedelta(minutes=int(time))
    await member.timeout(reason=reason, until=time)
    await ctx.send(f"Тайм-аут для {member.mention} на {time} по причине {reason}")#, ephemeral=True)

# untimeout command
@bot.slash_command(name="untimeout", description="Снять тайм-аут пользователю")
@commands.has_permissions(administrator=True)
async def untimeout(ctx, member: disnake.Member = commands.Param(description="Выберите пользователя, с которого нужно снять тайм-аут")):
    await member.timeout(reason=None, until=None)
    await ctx.send(f"{member.mention} был снят с тайм-аута", ephemeral=True)



bot.run("token")
