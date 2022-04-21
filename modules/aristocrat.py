from helper import module, Message, db

from pyrogram import filters

#¯\_(ツ)_/¯

@module(commands="aristocrat", args=["on/off"], desc="заменяет знаки , и . на 、 & 。 и ставит в начале ー (аристократо бейба)")
async def aristocrat(_, message: Message):
	try:
		aristocratos = message.command[1]
		db.set(f"aristocrato", aristocratos)
		await message.edit("[<b>Aristocrat</b>] Успешно!")
	except IndexError:
		await message.edit("[<b>Aristocrat</b>] Введите значения on/off!")

@module(filters.me)
async def aristocrato(_, message: Message):
	val = db.get("aristocrato")
	if val == "on":
		text = message.text.replace(",", "、").replace(".", "。")
		await message.edit(f"ー {text}")
	else:
		pass

made_by = "@lordnet_modules | @AmokDev"
