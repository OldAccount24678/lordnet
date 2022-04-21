from helper import module, Message, db

from pyrogram import filters

#¯\_(ツ)_/¯

@module(commands="russia", args=["on/off"], desc="заменяет буквы З и В на Z & V в тексте")
async def russia(_, message: Message):
	try:
		ZV = message.command[1]
		db.set(f"Z", ZV)
		await message.edit("[<b>RUSSIA</b>] Успешно!")
	except IndexError:
		await message.edit("[<b>RUSSIA</b>] Введите значения on/off!")

@module(filters.me)
async def russiaZ(_, message: Message):
	val = db.get("Z")
	if val == "on":
		text = message.text.replace("з", "Z").replace("в", "V").replace("З", "Z").replace("В", "V")
		await message.edit(text)
	else:
		pass

made_by = "@lordnet_modules | @AmokDev"
