from helper import module, Message, db

from pyrogram import filters, ContinuePropagation

#¯\_(ツ)_/¯

@module(commands="russia", args=["on/off"], desc="заменяет буквы З и В на Z & V в тексте")
async def example(_, message: Message):
	try:
		ZV = message.command[1]
		if ZV != "on" or ZV != "off":
			await message.edit("[<b>RUSSIA</b>] Введите значения on/off!")
		else:
			db.set(f"Z", ZV)
			await message.edit(f"[<b>RUSSIA</b>] Успешно поставлено значение {ZV}")
	except IndexError:
		await message.edit("[<b>RUSSIA</b>] Введите значения on/off!")

@module(filters.me)
async def russia(_, message: Message):
	val = db.get("Z")
	if val == "on":
		text = message.text.replace("з", "Z").replace("в", "V").replace("З", "Z").replace("В", "V")
		await message.edit(text)
	else:
		pass
	raise ContinuePropagation

made_by = "@lordnet_modules | @AmokDev"
