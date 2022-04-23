from helper import module, Message, session

import urllib.parse
import json
import os
from io import BytesIO

async def get_code(code: str):
    return urllib.parse.quote_plus(code)


@module(commands=["carbon", "code", "код"], args=["code/file/reply"], description="преобразование кода в картинку")
async def example(_, message: Message):
    try:
        filepath = None
        if (
            len(message.command) == 1
            and not message.reply_to_message
            and not message.document
        ):
            return await message.edit(
                "<b>Пожалуйста, сделайте реплай на файл/текст или напишите текст в строке.</b>"
            )
        elif len(message.command) > 1:
            code = message.text.split(maxsplit=1)[1]
        elif message.reply_to_message:
            if message.reply_to_message.document:
                filepath = f"downloads/{message.reply_to_message.document.file_name}"
                await message.reply_to_message.download(filepath)
                code = open(filepath, "r", encoding="utf-8").read()
            elif message.reply_to_message.text:
                code = message.reply_to_message.text
            elif message.reply_to_message.caption:
                code = message.reply_to_message.caption
            else:
                return await message.edit(
                    "<b>Пожалуйста, сделайте реплай на файл/текст или напишите текст в строке.</b>"
                )
        elif message.document:
            filepath = f"downloads/{message.document.file_name}"
            await message.download(filepath)
            code = open(filepath, "r", encoding="utf-8").read()
        else:
            return await message.edit(
                "<b>Пожалуйста, сделайте реплай на файл/текст или напишите текст в строке.</b>"
            )

        await message.edit("<b>Генерация картинки...</b>")

        async with session.post(
            "http://lordcarbon.herokuapp.com/",
            json={"code": await get_code(code)},
        ) as resp:
            if not resp.ok:
                return await message.edit("<b>Ошибка при получении изображения.</b>")
            image = BytesIO(await resp.read())
            image.name = "carbon.jpg"
            image.seek(0)
        await message.reply_document(image)
        await message.delete()

        if filepath:
            os.remove(filepath)
    except Exception as e:
        return await message.edit(e)



        
made_by = "@lordnet_modules"
