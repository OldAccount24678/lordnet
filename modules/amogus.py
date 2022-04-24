# module by t.me/KeyZenD
# Adaptation for LordNet by AmokDev
# AmokDev's' GitHub - https://github.com/AmokDev/lordnet
#¯\_(ツ)_/¯

from pyrogram import Client, filters
from pyrogram.types import Message

from helper import import_library
from helper import module
from helper import session as req
import os.path

async def get(url):
    async with req.get(url) as res:
        return res


Image = import_library('PIL.Image', 'pillow')
ImageFont = import_library('PIL.ImageFont')
ImageDraw = import_library('PIL.ImageDraw')

from io import BytesIO
from random import randint, choice
from textwrap import wrap

clrs = {'red': 1, 'lime': 2, 'green': 3, 'blue': 4, 'cyan': 5, 'brown': 6, 'purple': 7, 'pink': 8, 'orange': 9, 'yellow': 10, 'white': 11, 'black': 12}
url = "https://raw.githubusercontent.com/KeyZenD/AmongUs/master/"


if not os.path.isfile('downloads/bold.ttf'):
    loop = asyncio.get_event_loop()
    res = loop.run_until_complete(get(url+"bold.ttf"))
    data = loop.run_until_complete(res.read())
    datapath = 'downloads/bold.ttf'
    open(datapath, 'wb').write(data)
    
font = ImageFont.truetype(datapath, 60)


async def get_impostor(index: int, url: str):
    path = f'downloads/{index}_amogus.png'
    if not os.path.isfile(path):
        res = await get(url)
        data = await res.read()
        open(path, 'wb').write(data)
    return path


@module(commands=["amogus", "амогус"], args=["text"], desc="amgus, tun tun tun tun tun tun tun tudududn tun tun")
async def example(_, message: Message):
	clr = randint(1,12)
	text = " ".join(message.command[1:])
	await message.edit("<b>amgus, tun tun tun tun tun tun tun tudududn tun tun...</b>")
        data = await get_impostor(clr, f"{url}{clr}.png")
	imposter = Image.open(data)
	text_ = "\n".join(["\n".join(wrap(part, 30)) for part in text.split("\n")])
	w, h = ImageDraw.Draw(Image.new("RGB", (1,1))).multiline_textsize(text_, font, stroke_width=2)
	text = Image.new("RGBA", (w+30, h+30))
	ImageDraw.Draw(text).multiline_text((15,15), text_, "#FFF", font, stroke_width=2, stroke_fill="#000")
	w = imposter.width + text.width + 10
	h = max(imposter.height, text.height)
	image = Image.new("RGBA", (w, h))
	image.paste(imposter, (0, h-imposter.height), imposter)
	image.paste(text, (w-text.width, 0), text)
	image.thumbnail((512, 512))
	output = BytesIO()
	output.name = "imposter.webp"
	image.save(output)
	output.seek(0)
	await message.delete()
	await client.send_sticker(message.chat.id, output)

made_by = "@SosokDev"
