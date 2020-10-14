import discord
from discord.ext import commands
from discord.ext.commands import BucketType
from discord.ext.commands import cooldown
import mysql.connector
import random

client = commands.Bot(command_prefix = "", case_insensitive=True)
client.remove_command("help")

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd='test',
    database="userlevels"
)

def generateXP():
    return random.randint(1, 10)

@client.event
async def on_ready():
    print("sql.py Logged in as: " + client.user.name + "\n")
    print(mydb)
    print("")

@client.event
async def on_message(message):
    if message.author.bot:
        return
    else:
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM bag WHERE client_id = " + str(message.author.id))
        result = cursor.fetchall()
        if(len(result) == 0):
            cursor.execute("INSERT INTO bag VALUES(" + str(message.author.id) + ", 0, 0, 0, 0)")
            mydb.commit()
        cursor.execute("SELECT * FROM vault WHERE client_id = " + str(message.author.id))
        result = cursor.fetchall()
        if(len(result) == 0):
            cursor.execute("INSERT INTO vault VALUES(" + str(message.author.id) + ", 0, 0, 0, 0)")
            mydb.commit()
        cursor.execute("SELECT * FROM equipment WHERE client_id = " + str(message.author.id))
        result = cursor.fetchall()
        if(len(result) == 0):
            cursor.execute("INSERT INTO equipment (client_id) VALUES(" + str(message.author.id) + ")")
            mydb.commit()
        xp = generateXP()
        cursor.execute("SELECT user_xp, user_level FROM users WHERE client_id = " + str(message.author.id))
        result = cursor.fetchall()
        if(len(result) == 0):
            cursor.execute("INSERT INTO users VALUES(" + str(message.author.id) + "," + str(xp) + ", 1, 0, 0)")
            mydb.commit()
            em = discord.Embed(title = f"{message.author.name} gained " + str(xp) + "xp!",color = discord.Color.red())
            await message.channel.send(embed = em)
            await client.process_commands(message)
            return
        else:
            newXP = result[0][0] + xp
            currentLevel = result[0][1]
            flag = False
            if newXP < 83:
                currentLevel = 1
            elif newXP >= 83 and newXP < 174:
                if currentLevel != 2:
                    flag = True
                currentLevel = 2
            elif newXP >= 174 and newXP < 276:
                if currentLevel != 3:
                    flag = True
                currentLevel = 3
            elif newXP >= 276 and newXP < 388:
                if currentLevel != 4:
                    flag = True
                currentLevel = 4
            elif newXP >= 388 and newXP < 512:
                if currentLevel != 5:
                    flag = True
                currentLevel = 5
            elif newXP >= 512 and newXP < 650:
                if currentLevel != 6:
                    flag = True
                currentLevel = 6
            elif newXP >= 650 and newXP < 801:
                if currentLevel != 7:
                    flag = True
                currentLevel = 7
            elif newXP >= 801 and newXP < 969:
                if currentLevel != 8:
                    flag = True
                currentLevel = 8
            elif newXP >= 969 and newXP < 1154:
                if currentLevel != 9:
                    flag = True
                currentLevel = 9
            elif newXP >= 1154 and newXP < 1358:
                if currentLevel != 10:
                    flag = True
                currentLevel = 10
            elif newXP >= 1358 and newXP < 1584:
                if currentLevel != 11:
                    flag = True
                currentLevel = 11
            elif newXP >= 1584 and newXP < 1833:
                if currentLevel != 12:
                    flag = True
                currentLevel = 12
            elif newXP >= 1833 and newXP < 2107:
                if currentLevel != 13:
                    flag = True
                currentLevel = 13
            elif newXP >= 2107 and newXP < 2411:
                if currentLevel != 14:
                    flag = True
                currentLevel = 14
            elif newXP >= 2411 and newXP < 2746:
                if currentLevel != 15:
                    flag = True
                currentLevel = 15
            elif newXP >= 2746 and newXP < 3115:
                if currentLevel != 16:
                    flag = True
                currentLevel = 16
            elif newXP >= 3115 and newXP < 3523:
                if currentLevel != 17:
                    flag = True
                currentLevel = 17
            elif newXP >= 3523 and newXP < 3973:
                if currentLevel != 18:
                    flag = True
                currentLevel = 18
            elif newXP >= 3973 and newXP < 4470:
                if currentLevel != 19:
                    flag = True
                currentLevel = 19
            elif newXP >= 4470 and newXP < 5018:
                if currentLevel != 20:
                    flag = True
                currentLevel = 20
            elif newXP >= 5018 and newXP < 5624:
                if currentLevel != 21:
                    flag = True
                currentLevel = 21
            elif newXP >= 5624 and newXP < 6291:
                if currentLevel != 22:
                    flag = True
                currentLevel = 22
            elif newXP >= 6291 and newXP < 7028:
                if currentLevel != 23:
                    flag = True
                currentLevel = 23
            elif newXP >= 7028 and newXP < 7842:
                if currentLevel != 24:
                    flag = True
                currentLevel = 24
            elif newXP >= 7842 and newXP < 8740:
                if currentLevel != 25:
                    flag = True
                currentLevel = 25
            elif newXP >= 8740 and newXP < 9730:
                if currentLevel != 26:
                    flag = True
                currentLevel = 26
            elif newXP >= 9730 and newXP < 10824:
                if currentLevel != 27:
                    flag = True
                currentLevel = 27
            elif newXP >= 10824 and newXP < 12031:
                if currentLevel != 28:
                    flag = True
                currentLevel = 28
            elif newXP >= 12031 and newXP < 13363:
                if currentLevel != 29:
                    flag = True
                currentLevel = 29
            elif newXP >= 13363 and newXP < 14833:
                if currentLevel != 30:
                    flag = True
                currentLevel = 30
            elif newXP >= 14833 and newXP < 16456:
                if currentLevel != 31:
                    flag = True
                currentLevel = 31
            elif newXP >= 16456 and newXP < 18247:
                if currentLevel != 32:
                    flag = True
                currentLevel = 32
            elif newXP >= 18247 and newXP < 20224:
                if currentLevel != 33:
                    flag = True
                currentLevel = 33
            elif newXP >= 20224:
                if currentLevel != 34:
                    flag = True
                currentLevel = 34
            else:
                currentLevel = 0
            cursor.execute("UPDATE users SET user_xp = " + str(newXP) + ", user_level = " + str(currentLevel) + " WHERE client_id = " + str(message.author.id))
            mydb.commit()
            em = discord.Embed(title = f"{message.author.name} gained " + str(xp) + "xp!",color = discord.Color.red())
            await message.channel.send(embed = em)
            if flag:
                em = discord.Embed(title = f"{message.author.name} leveled up to " + str(currentLevel) + "!",color = discord.Color.red())
                await message.channel.send(embed = em)
        await client.process_commands(message)

mainshop_buy = [{"name":"Pickaxe", "price":250,"description":"Equip it to start mining"},
                {"name":"Blacksmith Hammer", "price":1000,"description":"Equip it to start crafting"}]

mainshop_sell = [{"name":"Stone", "price":10,"description":"It's a rock what more needs to be said?"},
                 {"name":"Ore", "price":125,"description":"This can be refined into Iron Bar"},
                 {"name":"Pickaxe", "price":250,"description":"Equip it to start mining"},
                 {"name":"Iron Bar", "price":500,"description":"A great crafting material"},
                 {"name":"Blacksmith Hammer", "price":1000,"description":"Equip it to start crafting"},
                 {"name":"Iron Sword", "price":2000,"description":"Equip it to start combat"},
                 {"name":"Iron Armour", "price":10000,"description":"Equip it to survive combat"}]

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        em = discord.Embed(title = "Please pass in all required arguments:",color = discord.Color.red())
        await ctx.send(embed = em)
        em = discord.Embed(title = str(error),color = discord.Color.red())
        await ctx.send(embed = em)
        print(error)
    elif isinstance(error, commands.CommandNotFound):
        print(error)
#        await ctx.send("Invalid Command Used:")
#        await ctx.send(error)
#        print(error)
    elif isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title = f"That command is on cooldown. Try again in {error.retry_after:,.2f} seconds.",color = discord.Color.red())
        await ctx.send(embed = em)
        print(error)
    elif isinstance(error, commands.TooManyArguments):
        em = discord.Embed(title = "To many arguments:",color = discord.Color.red())
        await ctx.send(embed = em)
        em = discord.Embed(title = str(error),color = discord.Color.red())
        await ctx.send(embed = em)
        print(error)
    else:
        em = discord.Embed(title = "An error occured:",color = discord.Color.red())
        await ctx.send(embed = em)
        em = discord.Embed(title = str(error),color = discord.Color.red())
        await ctx.send(embed = em)
        print(error)

@client.command()
@cooldown(1, 5, BucketType.user)
async def help(ctx):
    em = discord.Embed(title = "Help:",color = discord.Color.red())
    em.add_field(name = "Help", value = "Shows you all of the commands and what they do")
    em.add_field(name = "Syntax", value = "Shows you general syntax tips and then the syntax for every command")
    em.add_field(name = "Overview", value = "Shows you an overview of the game, the progression path and planned features")
    em.add_field(name = "Level", value = "Shows you your current total xp and level")
    em.add_field(name = "Balance", value = "Shows you your amount of money in the bank and wallet")
    em.add_field(name = "Beg", value = "You beg for money and get between 0-4 added to your wallet each time")
    em.add_field(name = "Buy", value = "You buy an item from the shop with money in your wallet and the item is added to your bag")
    em.add_field(name = "Sell", value = "You sell an item to the shop thats in your bag and the money is added to your wallet")
    em.add_field(name = "Deposit", value = "You deposit money from your wallet to your bank")
    em.add_field(name = "Withdraw", value = "You withdraw money from your bank to your wallet")
    em.add_field(name = "Send", value = "You send money from your bank to another persons bank")
    em.add_field(name = "Slots", value = "Gambling you have a chance you win 8 times your orginal amount")
    em.add_field(name = "Leaderboard", value = "Shows you a leaderboard of the money of everyone in the database")
    em.add_field(name = "Shop", value = "Shows you what you can buy and sell at the shop")
    em.add_field(name = "Bag", value = "Shows you your items in your bag")
    em.add_field(name = "Vault", value = "Shows you your items in your vault")
    em.add_field(name = "Equipment", value = "Shows you your current equipment")
    em.add_field(name = "Equip", value = "You equip an item from your bag")
    em.add_field(name = "Unequip", value = "You unequip an item the item is returned to your bag")
    em.add_field(name = "Mine", value = "Requires a Pickaxe equipped for you to mine. Mining a 2/10 chance for nothing, a 7/10 chance for Stone, and a 1/10 chance for Ore")
    em.add_field(name = "Stow", value = "You stow an item from your bag to your vault")
    em.add_field(name = "Unstow", value = "You unstow an item from your vault to your bag")
    em.add_field(name = "Ship", value = "You send an item from your vault to another persons vault")
    em.add_field(name = "Recipes", value = "Shows what you can craft and the requirements")
    em.add_field(name = "Craft", value = "Requires a Blacksmith Hammer equipped to craft")
    await ctx.send(embed = em)
    em = discord.Embed(title = "Help Part 2:",color = discord.Color.red())
    em.add_field(name = "Stats", value = "Combines the level, balance, bag, vault, and equipment command")
    await ctx.send(embed = em)

@client.command()
@cooldown(1, 5, BucketType.user)
async def syntax(ctx):
    em = discord.Embed(title = "General Syntax:",color = discord.Color.red())
    em.add_field(name = "Tip 1", value = "There is no command prefix so you can just type the command")
    em.add_field(name = "Tip 2", value = "{item} always comes before {amount}")
    em.add_field(name = "Tip 3", value = "if {amount} comes after {item} you will have to use quotes around the item if it is longer then one word")
    em.add_field(name = "Tip 4", value = "If you can't figure out the syntax after a few min of trying reach out to Nate#5359 on discord")
    await ctx.send(embed = em)
    em = discord.Embed(title = "Command Syntax:",color = discord.Color.red())
    em.add_field(name = "Help", value = "Just the command")
    em.add_field(name = "Syntax", value = "Just the command")
    em.add_field(name = "Overview", value = "Just the command")
    em.add_field(name = "Level", value = "Just the command")
    em.add_field(name = "Balance", value = "Just the command")
    em.add_field(name = "Beg", value = "Just the command")
    em.add_field(name = "Buy", value = "buy {item} {amount} if the item has a space use quotes around it")
    em.add_field(name = "Sell", value = "sell {item} {amount} if the item has a space use quotes around it")
    em.add_field(name = "Deposit", value = "deposit {amount}")
    em.add_field(name = "Withdraw", value = "withdraw {amount}")
    em.add_field(name = "Send", value = "send {@person} {amount}")
    em.add_field(name = "Slots", value = "Just the command")
    em.add_field(name = "Leaderboard", value = "Just the command you can also use lb instead of leaderboard")
    em.add_field(name = "Shop", value = "Just the command you can also use store instead of shop")
    em.add_field(name = "Bag", value = "Just the command")
    em.add_field(name = "Vault", value = "Just the command")
    em.add_field(name = "Equipment", value = "Just the command")
    em.add_field(name = "Equip", value = "equip {item}")
    em.add_field(name = "Unequip", value = "unequip {item}")
    em.add_field(name = "Mine", value = "Just the command")
    em.add_field(name = "Stow", value = "stow {item} {amount} if item has a space use all lowercase and an underscore instead of a space")
    em.add_field(name = "Unstow", value = "unstow {item} {amount} if item has a space use all lowercase and an underscore instead of a space")
    em.add_field(name = "Ship", value = "ship {@person} {item} {amount}")
    em.add_field(name = "Recipes", value = "Just the command")
    em.add_field(name = "Craft", value = "craft {item} {amount}")
    await ctx.send(embed = em)
    em = discord.Embed(title = "Command Syntax Part 2:",color = discord.Color.red())
    em.add_field(name = "Stats", value = "Just the command")
    await ctx.send(embed = em)


@client.command()
@cooldown(1, 5, BucketType.user)
async def overview(ctx):
    em = discord.Embed(title = "Overview:",color = discord.Color.red())
    em.add_field(name = "Progression Path", value = "You beg until you have 250 in your wallet then you buy a pickaxe and start mining. You sell all of the stone you have and once you have 1000 in your wallet you buy a Blacksmith Hammer. Then you craft the Ore you mined into Iron Bars and then craft the Iron Bars into Iron Swords and Iron Armour and then you are ready for combat.")
    em.add_field(name = "Planned Features", value = "Solo PVE Combat, Group PVE Combat, PVP Combat, Player Economy Trading Hub")
    await ctx.send(embed = em)

@client.command()
@cooldown(1, 5, BucketType.user)
async def level(ctx):
    cursor = mydb.cursor()
    cursor.execute("SELECT user_xp, user_level FROM users WHERE client_id = " + str(ctx.author.id))
    result = cursor.fetchall()
    if(len(result) == 0):
        em = discord.Embed(title = "Error your not in the database yet",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    else:
        currentxp = result[0][0]
        currentLevel = result[0][1]
        em = discord.Embed(title = f"{ctx.author.name}'s level:",color = discord.Color.red())
        em.add_field(name = "Total xp",value = currentxp)
        em.add_field(name = "Level",value = currentLevel)
        await ctx.send(embed = em)

@client.command()
@cooldown(1, 5, BucketType.user)
async def balance(ctx):
    cursor = mydb.cursor()
    cursor.execute("SELECT user_wallet, user_bank FROM users WHERE client_id = " + str(ctx.author.id))
    result = cursor.fetchall()
    if(len(result) == 0):
        em = discord.Embed(title = "Error your not in the database yet",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    else:
        currentwallet = result[0][0]
        currentbank = result[0][1]
        em = discord.Embed(title = f"{ctx.author.name}'s balance",color = discord.Color.red())
        em.add_field(name = "Wallet",value = currentwallet)
        em.add_field(name = "Bank",value = currentbank)
        await ctx.send(embed = em)

@client.command()
@cooldown(1, 5, BucketType.user)
async def beg(ctx):
    cursor = mydb.cursor()
    cursor.execute("SELECT user_wallet FROM users WHERE client_id = " + str(ctx.author.id))
    result = cursor.fetchall()
    if(len(result) == 0):
        em = discord.Embed(title = "Error your not in the database yet",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    else:
        earnings = random.randint(0, 4)
        if earnings == 0:
            em = discord.Embed(title = f"Someone spit on {ctx.author.name} in disgust",color = discord.Color.red())
            await ctx.send(embed = em)
        else:
            newwallet = result[0][0] + earnings
            cursor.execute("UPDATE users SET user_wallet = " + str(newwallet) + " WHERE client_id = " + str(ctx.author.id))
            mydb.commit()
            em = discord.Embed(title = f"Someone gave {ctx.author.name} {earnings} coins!",color = discord.Color.red())
            await ctx.send(embed = em)

@client.command()
@cooldown(1, 5, BucketType.user)
async def buy(ctx, item, amount = 1):
    if amount <= 0:
        return
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM bag WHERE client_id = " + str(ctx.author.id))
    result = cursor.fetchall()
    if(len(result) == 0):
        em = discord.Embed(title = "Error your not in the database yet",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    res = await buy_this(ctx,item,amount)
    if not res[0]:
        if res[1]==1:
            em = discord.Embed(title = "The store doesn't sell that!",color = discord.Color.red())
            await ctx.send(embed = em)
            return
        if res[1]==2:
            em = discord.Embed(title = "Error your not in the database yet",color = discord.Color.red())
            await ctx.send(embed = em)
            return
        if res[1]==3:
            em = discord.Embed(title = f"{ctx.author.name} doesn't have enough money in their wallet to buy {amount} {item}!",color = discord.Color.red())
            await ctx.send(embed = em)
            return
    em = discord.Embed(title = f"{ctx.author.name} just bought {amount} {item}!",color = discord.Color.red())
    await ctx.send(embed = em)

async def buy_this(ctx,item_name,amount):
    item_name = item_name
    name_ = None
    for item in mainshop_buy:
        name = item["name"]
        if name == item_name:
            name_ = name
            price = item["price"]
            break
    if name_ == None:
        return [False,1]
    cost = price*amount
    cursor = mydb.cursor()
    cursor.execute("SELECT user_wallet FROM users WHERE client_id = " + str(ctx.author.id))
    result = cursor.fetchall()
    if(len(result) == 0):
        return [False,2]
    old_wallet = result[0][0]
    if old_wallet < cost:
        return [False,3]
    cursor.execute("SELECT " + str(item_name.lower()) + " FROM bag WHERE client_id = " + str(ctx.author.id))
    result = cursor.fetchall()
    old_bag = result[0][0]
    new_bag = old_bag + amount
    new_wallet = old_wallet - cost
    cursor.execute("UPDATE bag SET " + str(item_name.lower()) + " = " + str(new_bag) + "  WHERE client_id = " + str(ctx.author.id))
    mydb.commit()
    cursor.execute("UPDATE users SET user_wallet = " + str(new_wallet) + " WHERE client_id = " + str(ctx.author.id))
    mydb.commit()
    return [True,"Worked"]

@client.command()
@cooldown(1, 5, BucketType.user)
async def sell(ctx,item,amount = 1):
    if amount <= 0:
        return
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM bag WHERE client_id = " + str(ctx.author.id))
    result = cursor.fetchall()
    if(len(result) == 0):
        em = discord.Embed(title = "Error your not in the database yet",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    res = await sell_this(ctx,item,amount)
    if not res[0]:
        if res[1]==1:
            em = discord.Embed(title = "The store doesn't buy that!",color = discord.Color.red())
            await ctx.send(embed = em)
            return
        if res[1]==2:
            em = discord.Embed(title = "Error your not in the database yet",color = discord.Color.red())
            await ctx.send(embed = em)
        if res[1]==3:
            em = discord.Embed(title = f"{ctx.author.name} doesn't have {amount} {item} in their bag!",color = discord.Color.red())
            await ctx.send(embed = em)
            return
    em = discord.Embed(title = f"{ctx.author.name} just sold {amount} {item}!",color = discord.Color.red())
    await ctx.send(embed = em)

async def sell_this(ctx,item_name,amount,price = None):
    name_ = None
    for item in mainshop_sell:
        name = item["name"]
        if name == item_name:
            name_ = name
            if price==None:
                price = item["price"]
            break
    if name_ == None:
        return [False,1]
    cost = price*amount
    cursor = mydb.cursor()
    cursor.execute("SELECT user_wallet FROM users WHERE client_id = " + str(ctx.author.id))
    result = cursor.fetchall()
    if(len(result) == 0):
        return [False,2]
    old_wallet = result[0][0]
    new_wallet = old_wallet + cost
    cursor.execute("SELECT " + str(item_name.lower()) + " FROM bag WHERE client_id = " + str(ctx.author.id))
    result = cursor.fetchall()
    old_bag = result[0][0]
    new_bag = old_bag - amount
    if new_bag < 0:
        return [False,3]
    cursor.execute("UPDATE bag SET " + str(item_name.lower()) + " = " + str(new_bag) + " WHERE client_id = " + str(ctx.author.id))
    mydb.commit()
    cursor.execute("UPDATE users SET user_wallet = " + str(new_wallet) + " WHERE client_id = " + str(ctx.author.id))
    mydb.commit()
    return [True,"Worked"]

@client.command()
@cooldown(1, 5, BucketType.user)
async def deposit(ctx,amount = None):
    if amount == None:
        em = discord.Embed(title = "Please enter the amount",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    cursor = mydb.cursor()
    cursor.execute("SELECT user_wallet, user_bank FROM users WHERE client_id = " + str(ctx.author.id))
    result = cursor.fetchall()
    if(len(result) == 0):
        em = discord.Embed(title = "Error your not in the database yet",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    else:
        old_wallet = result[0][0]
        old_bank = result[0][1]
        amount = int(amount)
        if amount>old_wallet:
            em = discord.Embed(title = "You don't have that much money!",color = discord.Color.red())
            await ctx.send(embed = em)
            return
        if amount<0:
            em = discord.Embed(title = "Amount must be positive!",color = discord.Color.red())
            await ctx.send(embed = em)
            return
        new_wallet = old_wallet - amount
        new_bank = old_bank + amount
        cursor.execute("UPDATE users SET user_wallet = " + str(new_wallet) + ", user_bank = " + str(new_bank) + " WHERE client_id = " + str(ctx.author.id))
        mydb.commit()
        em = discord.Embed(title = f"{ctx.author.name} deposited " + str(amount) + " coins!",color = discord.Color.red())
        await ctx.send(embed = em)

@client.command()
@cooldown(1, 5, BucketType.user)
async def withdraw(ctx,amount = None):
    if amount == None:
        em = discord.Embed(title = "Please enter the amount",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    cursor = mydb.cursor()
    cursor.execute("SELECT user_wallet, user_bank FROM users WHERE client_id = " + str(ctx.author.id))
    result = cursor.fetchall()
    if(len(result) == 0):
        em = discord.Embed(title = "Error your not in the database yet",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    else:
        old_wallet = result[0][0]
        old_bank = result[0][1]
        amount = int(amount)
        if amount>old_bank:
            em = discord.Embed(title = "You don't have that much money!",color = discord.Color.red())
            await ctx.send(embed = em)
            return
        if amount<0:
            em = discord.Embed(title = "Amount must be positive!",color = discord.Color.red())
            await ctx.send(embed = em)
            return
        new_wallet = old_wallet + amount
        new_bank = old_bank - amount
        cursor.execute("UPDATE users SET user_wallet = " + str(new_wallet) + ", user_bank = " + str(new_bank) + " WHERE client_id = " + str(ctx.author.id))
        mydb.commit()
        em = discord.Embed(title = f"{ctx.author.name} withdrew " + str(amount) + " coins!",color = discord.Color.red())
        await ctx.send(embed = em)

@client.command()
@cooldown(1, 5, BucketType.user)
async def send(ctx,member:discord.Member,amount = None):
    if amount == None:
        em = discord.Embed(title = "Please enter the amount",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    cursor = mydb.cursor()
    cursor.execute("SELECT user_bank FROM users WHERE client_id = " + str(ctx.author.id))
    result = cursor.fetchall()
    old_bank = result[0][0]
    if(len(result) == 0):
        em = discord.Embed(title = "Error your not in the database yet",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    cursor.execute("SELECT user_bank FROM users WHERE client_id = " + str(member.id))
    result2 = cursor.fetchall()
    if(len(result2) == 0):
        em = discord.Embed(title = "Error the person you are trying to send to isn't in the database yet",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    old_bank = result[0][0]
    old_bank2 = result2[0][0]
    amount = int(amount)
    if amount>old_bank:
        em = discord.Embed(title = "You don't have that much money!",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    if amount<0:
        em = discord.Embed(title = "Amount must be positive!",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    new_bank = old_bank - amount
    new_bank2 = old_bank2 + amount
    cursor.execute("UPDATE users SET user_bank = " + str(new_bank) + " WHERE client_id = " + str(ctx.author.id))
    mydb.commit()
    cursor.execute("UPDATE users SET user_bank = " + str(new_bank2) + " WHERE client_id = " + str(member.id))
    mydb.commit()
    em = discord.Embed(title = f"{ctx.author.name} sent {member} {amount} coins!",color = discord.Color.red())
    await ctx.send(embed = em)

@client.command()
@cooldown(1, 5, BucketType.user)
async def slots(ctx,amount = None):
    if amount == None:
        em = discord.Embed(title = "Please enter the amount",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    cursor = mydb.cursor()
    cursor.execute("SELECT user_wallet FROM users WHERE client_id = " + str(ctx.author.id))
    result = cursor.fetchall()
    if(len(result) == 0):
        em = discord.Embed(title = "Error your not in the database yet",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    old_wallet = result[0][0]
    amount = int(amount)
    if amount>old_wallet:
        em = discord.Embed(title = "You don't have that much money!",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    if amount<0:
        em = discord.Embed(title = "Amount must be positive!",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    final = []
    for i in range(3):
        a = random.choice(["A", "B", "C"])
        final.append(a)
    em = discord.Embed(title = str(final),color = discord.Color.red())
    await ctx.send(embed = em)
    if final[0] == final[1] and final[1] == final [2]:
        prize = amount * 8
        new_wallet = old_wallet + prize
        cursor.execute("UPDATE users SET user_wallet = " + str(new_wallet) + " WHERE client_id = " + str(ctx.author.id))
        mydb.commit()
        em = discord.Embed(title = f"{ctx.author.name} won and made {8*amount} coins! 8 Times your original amount of {amount} coins!",color = discord.Color.red())
        await ctx.send(embed = em)
    else:
        new_wallet = old_wallet - amount
        cursor.execute("UPDATE users SET user_wallet = " + str(new_wallet) + " WHERE client_id = " + str(ctx.author.id))
        mydb.commit()
        em = discord.Embed(title = f"{ctx.author.name} lost {amount} coins! One more spin? You can't lose another time, right?",color = discord.Color.red())
        await ctx.send(embed = em)

@client.command(aliases = ["lb"])
@cooldown(1, 5, BucketType.user)
async def leaderboard(ctx):
    cursor = mydb.cursor()
    cursor.execute("SELECT client_id, user_wallet, user_bank FROM users;")
    result = cursor.fetchall()
    leader_board={}
    total = []
    num = 0
    for x in result:
        client_id = result[(num)][0]
        wallet = result[(num)][1]
        bank = result[(num)][2]
        total_amount = wallet + bank
        leader_board[total_amount] = client_id
        total.append(total_amount)
        num += 1
    total = sorted(total,reverse=True)
    em = discord.Embed(title = f"Top {num} Richest People" , description = "This is decided on the basis of raw money in the bank and wallet",color = discord.Color.red())
    index = 1
    for amt in total:
        id_ = leader_board[amt]
        member = client.get_user(id_)
        name = member.name
        em.add_field(name = f"{index}. {name}" , value = f"{amt}", inline = False)
        if index == x:
            break
        else:
            index += 1
    await ctx.send(embed = em)

@client.command(aliases = ["store"])
@cooldown(1, 5, BucketType.user)
async def shop(ctx):
    em = discord.Embed(title = "Item's you can buy from the shop:",color = discord.Color.red())
    for item in mainshop_buy:
        name = item["name"]
        price = item["price"]
        description = item["description"]
        em.add_field(name = name, value = f"${price} | {description}")
    await ctx.send(embed = em)
    em = discord.Embed(title = "Item's you can sell to the shop:",color = discord.Color.red())
    for item in mainshop_sell:
        name = item["name"]
        price = item["price"]
        description = item["description"]
        em.add_field(name = name, value = f"${price} | {description}")
    await ctx.send(embed = em)

@client.command()
@cooldown(1, 5, BucketType.user)
async def bag(ctx):
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM bag WHERE client_id = " + str(ctx.author.id))
    result = cursor.fetchall()
    if(len(result) == 0):
        em = discord.Embed(title = "Error your not in the database yet",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    em = discord.Embed(title = f"{ctx.author.name}'s Bag",color = discord.Color.red())
    stone = result[0][1]
    pickaxe = result[0][2]
    ore = result[0][3]
    iron_bar = result[0][4]
    blacksmith_hammer = result[0][5]
    iron_sword = result[0][6]
    iron_armour = result[0][7]
    if stone > 0:
        em.add_field(name = "Stone", value = str(stone))
    if ore > 0:
        em.add_field(name = "Ore", value = str(ore))
    if pickaxe > 0:
        em.add_field(name = "Pickaxe", value = str(pickaxe))
    if iron_bar > 0:
        em.add_field(name = "Iron Bar", value = str(iron_bar))
    if blacksmith_hammer > 0:
        em.add_field(name = "Blacksmith Hammer", value = str(blacksmith_hammer))
    if iron_sword > 0:
        em.add_field(name = "Iron Sword", value = str(iron_sword))
    if iron_armour > 0:
        em.add_field(name = "Iron Armour", value = str(iron_armour))
    await ctx.send(embed = em)

@client.command()
@cooldown(1, 5, BucketType.user)
async def vault(ctx):
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM vault WHERE client_id = " + str(ctx.author.id))
    result = cursor.fetchall()
    if(len(result) == 0):
        em = discord.Embed(title = "Error your not in the database yet",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    em = discord.Embed(title = f"{ctx.author.name}'s Vault",color = discord.Color.red())
    stone = result[0][1]
    pickaxe = result[0][2]
    ore = result[0][3]
    iron_bar = result[0][4]
    blacksmith_hammer = result[0][5]
    iron_sword = result[0][6]
    iron_armour = result[0][7]
    if stone > 0:
        em.add_field(name = "Stone", value = str(stone))
    if ore > 0:
        em.add_field(name = "Ore", value = str(ore))
    if pickaxe > 0:
        em.add_field(name = "Pickaxe", value = str(pickaxe))
    if iron_bar > 0:
        em.add_field(name = "Iron Bar", value = str(iron_bar))
    if blacksmith_hammer > 0:
        em.add_field(name = "Blacksmith Hammer", value = str(blacksmith_hammer))
    if iron_sword > 0:
        em.add_field(name = "Iron Sword", value = str(iron_sword))
    if iron_armour > 0:
        em.add_field(name = "Iron Armour", value = str(iron_armour))
    await ctx.send(embed = em)

@client.command()
@cooldown(1, 5, BucketType.user)
async def equipment(ctx):
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM equipment WHERE client_id = " + str(ctx.author.id))
    result = cursor.fetchall()
    if(len(result) == 0):
        em = discord.Embed(title = "Error your not in the database yet",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    equipped_weapon = result[0][1]
    equipped_armour = result[0][2]
    em = discord.Embed(title = f"{ctx.author.name}'s Equipment",color = discord.Color.red())
    if equipped_weapon != None:
        em.add_field(name = "Weapon", value = str(equipped_weapon))
    if equipped_armour != None:
        em.add_field(name = "Armour", value = str(equipped_armour))
    await ctx.send(embed = em)

@client.command()
@cooldown(1, 5, BucketType.user)
async def equip(ctx, *, item: str):
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM equipment WHERE client_id = " + str(ctx.author.id))
    result = cursor.fetchall()
    if(len(result) == 0):
        em = discord.Embed(title = "Error your not in the database yet",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    cursor.execute("SELECT * FROM bag WHERE client_id = " + str(ctx.author.id))
    result = cursor.fetchall()
    if(len(result) == 0):
        em = discord.Embed(title = "Error your not in the database yet",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    if item == "Pickaxe" or item == "pickaxe":
        old_bag = result[0][2]
        new_bag = old_bag - 1
        if new_bag<0:
            em = discord.Embed(title = f"{ctx.author.name} doesn't have {item} in their bag",color = discord.Color.red())
            await ctx.send(embed = em)
            return
        cursor.execute("SELECT equipped_weapon FROM equipment WHERE client_id = " + str(ctx.author.id))
        result = cursor.fetchall()
        old_equipped = result[0][0]
        if old_equipped != None:
            em = discord.Embed(title = f"{ctx.author.name} can't equip {item} because they already have something in that slot",color = discord.Color.red())
            await ctx.send(embed = em)
            return
        cursor.execute("UPDATE bag SET pickaxe = " + str(new_bag) + " WHERE client_id = " + str(ctx.author.id))
        mydb.commit()
        cursor.execute("UPDATE equipment SET equipped_weapon = 'Pickaxe' WHERE client_id = " + str(ctx.author.id))
        mydb.commit()
        em = discord.Embed(title = f"{ctx.author.name} equipped {item} in the weapon slot from their bag",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    elif item == "Blacksmith Hammer" or item == "blacksmith hammer":
        old_bag = result[0][5]
        new_bag = old_bag - 1
        if new_bag<0:
            em = discord.Embed(title = f"{ctx.author.name} doesn't have {item} in their bag",color = discord.Color.red())
            await ctx.send(embed = em)
            return
        cursor.execute("SELECT equipped_weapon FROM equipment WHERE client_id = " + str(ctx.author.id))
        result = cursor.fetchall()
        old_equipped = result[0][0]
        if old_equipped != None:
            em = discord.Embed(title = f"{ctx.author.name} can't equip {item} because they already have something in that slot",color = discord.Color.red())
            await ctx.send(embed = em)
            return
        cursor.execute("UPDATE bag SET blacksmith_hammer = " + str(new_bag) + " WHERE client_id = " + str(ctx.author.id))
        mydb.commit()
        cursor.execute("UPDATE equipment SET equipped_weapon = 'Blacksmith Hammer' WHERE client_id = " + str(ctx.author.id))
        mydb.commit()
        em = discord.Embed(title = f"{ctx.author.name} equipped {item} in the weapon slot from their bag",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    elif item == "Iron Sword" or item == "iron sword":
        old_bag = result[0][6]
        new_bag = old_bag - 1
        if new_bag<0:
            em = discord.Embed(title = f"{ctx.author.name} doesn't have {item} in their bag",color = discord.Color.red())
            await ctx.send(embed = em)
            return
        cursor.execute("SELECT equipped_weapon FROM equipment WHERE client_id = " + str(ctx.author.id))
        result = cursor.fetchall()
        old_equipped = result[0][0]
        if old_equipped != None:
            em = discord.Embed(title = f"{ctx.author.name} can't equip {item} because they already have something in that slot",color = discord.Color.red())
            await ctx.send(embed = em)
            return
        cursor.execute("UPDATE bag SET iron_sword = " + str(new_bag) + " WHERE client_id = " + str(ctx.author.id))
        mydb.commit()
        cursor.execute("UPDATE equipment SET equipped_weapon = 'Iron Sword' WHERE client_id = " + str(ctx.author.id))
        mydb.commit()
        em = discord.Embed(title = f"{ctx.author.name} equipped {item} in the weapon slot from their bag",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    elif item == "Iron Armour" or item == "iron armour":
        old_bag = result[0][7]
        new_bag = old_bag - 1
        if new_bag<0:
            em = discord.Embed(title = f"{ctx.author.name} doesn't have {item} in their bag",color = discord.Color.red())
            await ctx.send(embed = em)
            return
        cursor.execute("SELECT equipped_armour FROM equipment WHERE client_id = " + str(ctx.author.id))
        result = cursor.fetchall()
        old_equipped = result[0][0]
        if old_equipped != None:
            em = discord.Embed(title = f"{ctx.author.name} can't equip {item} because they already have something in that slot",color = discord.Color.red())
            await ctx.send(embed = em)
            return
        cursor.execute("UPDATE bag SET iron_armour = " + str(new_bag) + " WHERE client_id = " + str(ctx.author.id))
        mydb.commit()
        cursor.execute("UPDATE equipment SET equipped_armour = 'Iron Armour' WHERE client_id = " + str(ctx.author.id))
        mydb.commit()
        em = discord.Embed(title = f"{ctx.author.name} equipped {item} in the armour slot from their bag",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    else:
        em = discord.Embed(title = f"{ctx.author.name} you can't equip {item}",color = discord.Color.red())
        await ctx.send(embed = em)

@client.command()
@cooldown(1, 5, BucketType.user)
async def unequip(ctx, *, item: str):
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM equipment WHERE client_id = " + str(ctx.author.id))
    result = cursor.fetchall()
    if(len(result) == 0):
        em = discord.Embed(title = "Error your not in the database yet",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    cursor.execute("SELECT * FROM bag WHERE client_id = " + str(ctx.author.id))
    result = cursor.fetchall()
    if(len(result) == 0):
        em = discord.Embed(title = "Error your not in the database yet",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    if item == "Pickaxe" or item == "pickaxe":
        cursor.execute("SELECT equipped_weapon FROM equipment WHERE client_id = " + str(ctx.author.id))
        result = cursor.fetchall()
        weapon = result[0][0]
        if weapon != "Pickaxe":
            em = discord.Embed(title = f"{ctx.author.name} doesn't have {item} equipped",color = discord.Color.red())
            await ctx.send(embed = em)
            return
        if weapon == "Pickaxe":
            cursor.execute("UPDATE equipment SET equipped_weapon = NULL WHERE client_id = " + str(ctx.author.id))
            mydb.commit()
            cursor.execute("SELECT pickaxe FROM bag WHERE client_id = " + str(ctx.author.id))
            result = cursor.fetchall()
            old_amt = result[0][0]
            new_amt = old_amt + 1
            cursor.execute("UPDATE bag SET pickaxe = " + str(new_amt) + " WHERE client_id = " + str(ctx.author.id))
            mydb.commit()
            em = discord.Embed(title = f"{ctx.author.name} unequipped {item} and it was added to their bag",color = discord.Color.red())
            await ctx.send(embed = em)
            return
    elif item == "Blacksmith Hammer" or item == "blacksmith hammer":
        cursor.execute("SELECT equipped_weapon FROM equipment WHERE client_id = " + str(ctx.author.id))
        result = cursor.fetchall()
        weapon = result[0][0]
        if weapon != "Blacksmith Hammer":
            em = discord.Embed(title = f"{ctx.author.name} doesn't have {item} equipped",color = discord.Color.red())
            await ctx.send(embed = em)
            return
        if weapon == "Blacksmith Hammer":
            cursor.execute("UPDATE equipment SET equipped_weapon = NULL WHERE client_id = " + str(ctx.author.id))
            mydb.commit()
            cursor.execute("SELECT blacksmith_hammer FROM bag WHERE client_id = " + str(ctx.author.id))
            result = cursor.fetchall()
            old_amt = result[0][0]
            new_amt = old_amt + 1
            cursor.execute("UPDATE bag SET blacksmith_hammer = " + str(new_amt) + " WHERE client_id = " + str(ctx.author.id))
            mydb.commit()
            em = discord.Embed(title = f"{ctx.author.name} unequipped {item} and it was added to their bag",color = discord.Color.red())
            await ctx.send(embed = em)
            return
    elif item == "Iron Sword" or item == "iron sword":
        cursor.execute("SELECT equipped_weapon FROM equipment WHERE client_id = " + str(ctx.author.id))
        result = cursor.fetchall()
        weapon = result[0][0]
        if weapon != "Iron Sword":
            em = discord.Embed(title = f"{ctx.author.name} doesn't have {item} equipped",color = discord.Color.red())
            await ctx.send(embed = em)
            return
        if weapon == "Iron Sword":
            cursor.execute("UPDATE equipment SET equipped_weapon = NULL WHERE client_id = " + str(ctx.author.id))
            mydb.commit()
            cursor.execute("SELECT iron_sword FROM bag WHERE client_id = " + str(ctx.author.id))
            result = cursor.fetchall()
            old_amt = result[0][0]
            new_amt = old_amt + 1
            cursor.execute("UPDATE bag SET iron_sword = " + str(new_amt) + " WHERE client_id = " + str(ctx.author.id))
            mydb.commit()
            em = discord.Embed(title = f"{ctx.author.name} unequipped {item} and it was added to their bag",color = discord.Color.red())
            await ctx.send(embed = em)
            return
    elif item == "Iron Armour" or item == "iron armour":
        cursor.execute("SELECT equipped_armour FROM equipment WHERE client_id = " + str(ctx.author.id))
        result = cursor.fetchall()
        armour = result[0][0]
        if armour != "Iron Armour":
            em = discord.Embed(title = f"{ctx.author.name} doesn't have {item} equipped",color = discord.Color.red())
            await ctx.send(embed = em)
            return
        if armour == "Iron Armour":
            cursor.execute("UPDATE equipment SET equipped_armour = NULL WHERE client_id = " + str(ctx.author.id))
            mydb.commit()
            cursor.execute("SELECT iron_armour FROM bag WHERE client_id = " + str(ctx.author.id))
            result = cursor.fetchall()
            old_amt = result[0][0]
            new_amt = old_amt + 1
            cursor.execute("UPDATE bag SET iron_armour = " + str(new_amt) + " WHERE client_id = " + str(ctx.author.id))
            mydb.commit()
            em = discord.Embed(title = f"{ctx.author.name} unequipped {item} and it was added to their bag",color = discord.Color.red())
            await ctx.send(embed = em)
            return
    else:
        em = discord.Embed(title = f"{ctx.author.name} you can't unequip {item}",color = discord.Color.red())
        await ctx.send(embed = em)

@client.command()
@cooldown(1, 5, BucketType.user)
async def mine(ctx):
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM bag WHERE client_id = " + str(ctx.author.id))
    result = cursor.fetchall()
    if(len(result) == 0):
        em = discord.Embed(title = "Error your not in the database yet",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    cursor.execute("SELECT * FROM equipment WHERE client_id = " + str(ctx.author.id))
    result = cursor.fetchall()
    if(len(result) == 0):
        em = discord.Embed(title = "Error your not in the database yet",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    weapon = result[0][1]
    if weapon != "Pickaxe":
        em = discord.Embed(title = "You need a pickaxe equipped to start mining. You can buy one from the shop for 250.",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    for i in range(1):
        mine_rng = random.choice(["Nothing", "Nothing", "Stone", "Stone", "Stone", "Stone", "Stone", "Stone", "Stone", "Ore"])
        if mine_rng == "Nothing":
            em = discord.Embed(title = "You mined nothing, better luck next time",color = discord.Color.red())
            await ctx.send(embed = em)
            return
        cursor.execute("SELECT " + str(mine_rng.lower()) + " FROM bag WHERE client_id = " + str(ctx.author.id))
        result = cursor.fetchall()
        old_bag = result[0][0]
        new_bag = old_bag + 1
        cursor.execute("UPDATE bag SET " + str(mine_rng.lower()) + " = " + str(new_bag) + " WHERE client_id = " + str(ctx.author.id))
        mydb.commit()
        em = discord.Embed(title = f"{ctx.author.name} mined 1 {mine_rng}!",color = discord.Color.red())
        await ctx.send(embed = em)

@client.command()
@cooldown(1, 5, BucketType.user)
async def stow(ctx, item, amount = None):
    if amount == None:
        em = discord.Embed(title = "Please enter the amount",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    if int(amount)<0:
        em = discord.Embed(title = "Amount must be positive!",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    cursor = mydb.cursor()
    try:
        cursor.execute("SELECT " + str(item.lower()) + " FROM bag WHERE client_id = " + str(ctx.author.id))
    except:
        em = discord.Embed(title = "Error the item your trying to stow isn't in the database yet",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    result = cursor.fetchall()
    if(len(result) == 0):
        em = discord.Embed(title = "Error you aren't in the database yet",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    old_bag = result[0][0]
    try:
        cursor.execute("SELECT " + str(item.lower()) + " FROM vault WHERE client_id = " + str(ctx.author.id))
    except:
        em = discord.Embed(title = "Error the item your trying to stow isn't in the database yet",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    result = cursor.fetchall()
    if(len(result) == 0):
        em = discord.Embed(title = "Error you aren't in the database yet",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    old_vault = result[0][0]
    amount = int(amount)
    if amount>old_bag:
        em = discord.Embed(title = f"You don't have {amount} {item} in your bag!",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    new_bag = old_bag - amount
    new_vault = old_vault + amount
    cursor.execute("UPDATE bag SET " + str(item.lower()) + " = " + str(new_bag) + " WHERE client_id = " + str(ctx.author.id))
    mydb.commit()
    cursor.execute("UPDATE vault SET " + str(item.lower()) + " = " + str(new_vault) + " WHERE client_id = " + str(ctx.author.id))
    mydb.commit()
    em = discord.Embed(title = f"{ctx.author.name} stowwed {amount} {item}!",color = discord.Color.red())
    await ctx.send(embed = em)

@client.command()
@cooldown(1, 5, BucketType.user)
async def unstow(ctx, item, amount = None):
    if amount == None:
        em = discord.Embed(title = "Please enter the amount",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    if int(amount)<0:
        em = discord.Embed(title = "Amount must be positive!",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    cursor = mydb.cursor()
    try:
        cursor.execute("SELECT " + str(item.lower()) + " FROM vault WHERE client_id = " + str(ctx.author.id))
    except:
        em = discord.Embed(title = "Error the item your trying to unstow isn't in the database yet",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    result = cursor.fetchall()
    if(len(result) == 0):
        em = discord.Embed(title = "Error you aren't in the database yet",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    old_vault = result[0][0]
    try:
        cursor.execute("SELECT " + str(item.lower()) + " FROM bag WHERE client_id = " + str(ctx.author.id))
    except:
        em = discord.Embed(title = "Error the item your trying to unstow isn't in the database yet",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    result = cursor.fetchall()
    if(len(result) == 0):
        em = discord.Embed(title = "Error you aren't in the database yet",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    old_bag = result[0][0]
    amount = int(amount)
    if amount>old_vault:
        em = discord.Embed(title = f"You don't have {amount} {item} in your vault!",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    new_bag = old_bag + amount
    new_vault = old_vault - amount
    cursor.execute("UPDATE bag SET " + str(item.lower()) + " = " + str(new_bag) + " WHERE client_id = " + str(ctx.author.id))
    mydb.commit()
    cursor.execute("UPDATE vault SET " + str(item.lower()) + " = " + str(new_vault) + " WHERE client_id = " + str(ctx.author.id))
    mydb.commit()
    em = discord.Embed(title = f"{ctx.author.name} unstowwed {amount} {item}!",color = discord.Color.red())
    await ctx.send(embed = em)

@client.command()
@cooldown(1, 5, BucketType.user)
async def ship(ctx,member:discord.Member,item,amount = None):
    if amount == None:
        em = discord.Embed(title = "Please enter the amount",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    if int(amount)<0:
        em = discord.Embed(title = "Amount must be positive!",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    cursor = mydb.cursor()
    try:
        cursor.execute("SELECT " + str(item.lower()) + " FROM vault WHERE client_id = " + str(ctx.author.id))
    except:
        em = discord.Embed(title = "Error the item your trying to ship isn't in the database yet",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    result = cursor.fetchall()
    if(len(result) == 0):
        em = discord.Embed(title = "Error you aren't in the database yet",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    old_vault1 = result[0][0]
    amount = int(amount)
    if amount>old_vault1:
        em = discord.Embed(title = f"You don't have {amount} {item} in your vault!",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    try:
        cursor.execute("SELECT " + str(item.lower()) + " FROM vault WHERE client_id = " + str(member.id))
    except:
        em = discord.Embed(title = "Error the item your trying to ship isn't in the database yet",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    result2 = cursor.fetchall()
    if(len(result2) == 0):
        em = discord.Embed(title = "Error the person you are trying to ship to isn't in the database yet",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    old_vault2 = result2[0][0]
    new_vault1 = old_vault1 - amount
    new_vault2 = old_vault2 + amount
    cursor.execute("UPDATE vault SET " + str(item.lower()) + " = " + str(new_vault1) + " WHERE client_id = " + str(ctx.author.id))
    mydb.commit()
    cursor.execute("UPDATE vault SET " + str(item.lower()) + " = " + str(new_vault2) + " WHERE client_id = " + str(member.id))
    mydb.commit()
    em = discord.Embed(title = f"{ctx.author.name} sent {member} {amount} {item}!",color = discord.Color.red())
    await ctx.send(embed = em)

@client.command()
@cooldown(1, 5, BucketType.user)
async def recipes(ctx):
    em = discord.Embed(title = f"{ctx.author.name}'s Recipes",color = discord.Color.red())
    em.add_field(name = "Iron Bar", value = "Costs 3 Ore")
    em.add_field(name = "Iron Sword", value = "Costs 5 Iron Bar")
    em.add_field(name = "Iron Armour", value = "Costs 20 Iron Bar")
    await ctx.send(embed = em)

@client.command()
@cooldown(1, 5, BucketType.user)
async def craft(ctx, item, amount = 1):
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM equipment WHERE client_id = " + str(ctx.author.id))
    result = cursor.fetchall()
    if(len(result) == 0):
        em = discord.Embed(title = "Error your not in the database yet",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    weapon = result[0][1]
    if weapon != "Blacksmith Hammer":
        em = discord.Embed(title = "You need a blacksmith hammer equipped to start crafting. You can buy one from the shop for 1000.",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    if amount <= 0:
        em = discord.Embed(title = "Please enter the amount",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    cursor.execute("SELECT * FROM bag WHERE client_id = " + str(ctx.author.id))
    result = cursor.fetchall()
    if(len(result) == 0):
        em = discord.Embed(title = "Error your not in the database yet",color = discord.Color.red())
        await ctx.send(embed = em)
        return
    if item == "Iron Bar":
        old_ore = result[0][3]
        old_iron_bar = result[0][4]
        cost = amount * 3
        new_ore = old_ore - cost
        new_iron_bar = old_iron_bar + amount
        if int(new_ore) < 0:
            em = discord.Embed(title = f"{ctx.author.name} doesn't have enough Ore to craft {amount} {item}",color = discord.Color.red())
            await ctx.send(embed = em)
            return
        cursor.execute("UPDATE bag SET ore = " + str(new_ore) + " WHERE client_id = " + str(ctx.author.id))
        mydb.commit()
        cursor.execute("UPDATE bag SET iron_bar = " + str(new_iron_bar) + " WHERE client_id = " + str(ctx.author.id))
        mydb.commit()
        em = discord.Embed(title = f"{ctx.author.name} used {cost} ore to craft {amount} {item}!",color = discord.Color.red())
        await ctx.send(embed = em)
    elif item == "Iron Sword":
        old_iron_bar = result[0][4]
        old_iron_sword = result[0][6]
        cost = amount * 5
        new_iron_bar = old_iron_bar - cost
        new_iron_sword = old_iron_sword + amount
        if int(new_iron_bar) < 0:
            em = discord.Embed(title = f"{ctx.author.name} doesn't have enough iron bars to craft {amount} {item}",color = discord.Color.red())
            await ctx.send(embed = em)
            return
        cursor.execute("UPDATE bag SET iron_bar = " + str(new_iron_bar) + " WHERE client_id = " + str(ctx.author.id))
        mydb.commit()
        cursor.execute("UPDATE bag SET iron_sword = " + str(new_iron_sword) + " WHERE client_id = " + str(ctx.author.id))
        mydb.commit()
        em = discord.Embed(title = f"{ctx.author.name} used {cost} iron bars to craft {amount} {item}!",color = discord.Color.red())
        await ctx.send(embed = em)
    elif item == "Iron Armour":
        old_iron_bar = result[0][4]
        old_iron_armour = result[0][7]
        cost = amount * 20
        new_iron_bar = old_iron_bar - cost
        new_iron_armour = old_iron_armour + amount
        if int(new_iron_bar) < 0:
            em = discord.Embed(title = f"{ctx.author.name} doesn't have enough iron bars to craft {amount} {item}",color = discord.Color.red())
            await ctx.send(embed = em)
            return
        cursor.execute("UPDATE bag SET iron_bar = " + str(new_iron_bar) + " WHERE client_id = " + str(ctx.author.id))
        mydb.commit()
        cursor.execute("UPDATE bag SET iron_armour = " + str(new_iron_armour) + " WHERE client_id = " + str(ctx.author.id))
        mydb.commit()
        em = discord.Embed(title = f"{ctx.author.name} used {cost} iron bars to craft {amount} {item}!",color = discord.Color.red())
        await ctx.send(embed = em)
    else:
        em = discord.Embed(title = f"You can't craft {item}!",color = discord.Color.red())
        await ctx.send(embed = em)

@client.command()
@cooldown(1, 5, BucketType.user)
async def stats(ctx):
    await level(ctx)
    await balance(ctx)
    await bag(ctx)
    await vault(ctx)
    await equipment(ctx)

client.run("NzQ5Mjk1MDM1MzI5MTUxMDA3.X0p5YQ.Nl9N2nzS5ysRzsWjk-tZGvGe13o")
