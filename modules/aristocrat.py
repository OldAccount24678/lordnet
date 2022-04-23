from helper import module, Message, db

from pyrogram import filters, ContinuePropagation

#¯\_(ツ)_/¯
# ya eпаL piton

@module(commands="aristocrat", args=["on/off"], desc="заменяет знаки , и . на 、 & 。 и ставит в начале ー (аристократо бейба)")
async def example(_, message: Message):
	try:
		aristocratos = message.command[1]
		db.set(f"aristocrato", aristocratos)
		await message.edit(f"[<b>RUSSIA</b>] Успешно поставлено значение {aristocratos}")
	except IndexError:
		await message.edit("[<b>Aristocrat</b>] Введите значения on/off! (IndexError)")

@module(filters.me)
async def aristocrato(_, message: Message):
	val = db.get("aristocrato")
	if val == "on":
		text = message.text.replace(",", "、").replace(".", "。")
		await message.edit(f"ー {text}")
	else:
		pass
	raise ContinuePropagation

made_by = "@lordnet_modules | @AmokDev"
