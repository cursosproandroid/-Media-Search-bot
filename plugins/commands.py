# Cursos Pro Android by Skueletor ©️ 2021
import os
import logging
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from info import START_MSG, CHANNELS, ADMINS
from utils import Media

logger = logging.getLogger(__name__)


@Client.on_message(filters.command('start'))
async def start(bot, message):
    """Toca algún botón para iniciar :D"""
    buttons =   [[
                  InlineKeyboardButton('🔎 Buscar aquí', switch_inline_query_current_chat=''),
        InlineKeyboardButton('Buscar en otro chat 🔍', switch_inline_query='')
                ],
                [
                  InlineKeyboardButton(text="👤 Soporte", url="https://t.me/DKzippO")
                ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply(START_MSG, reply_markup=reply_markup)


@Client.on_message(filters.command('channel') & filters.user(ADMINS))
async def channel_info(bot, message):
    """Enviar información básica del canal"""
    if isinstance(CHANNELS, (int, str)):
        channels = [CHANNELS]
    elif isinstance(CHANNELS, list):
        channels = CHANNELS
    else:
        raise ValueError("Tipo inesperado de CANALES")

    for channel in channels:
        channel_info = await bot.get_chat(channel)
        string = str(channel_info)
        if len(string) > 4096:
            filename = (channel_info.title or channel_info.first_name) + ".txt"
            with open(filename, 'w') as f:
                f.write(string)
            await message.reply_document(filename)
            os.remove(filename)
        else:
            await message.reply(str(channel_info))


@Client.on_message(filters.command('total') & filters.user(ADMINS))
async def total(bot, message):
    """Mostrar el total de archivos en la base de datos"""
    msg = await message.reply("Procesando...⏳", quote=True)
    try:
        total = await Media.count_documents()
        await msg.edit(f'📁 Saved files: {total}')
    except Exception as e:
        logger.exception('Failed to check total files')
        await msg.edit(f'Error: {e}')


@Client.on_message(filters.command('logger') & filters.user(ADMINS))
async def log_file(bot, message):
    """Enviar archivo de registro"""
    try:
        await message.reply_document('TelegramBot.log')
    except Exception as e:
        await message.reply(str(e))


@Client.on_message(filters.command('delete') & filters.user(ADMINS))
async def delete(bot, message):
    """Eliminar archivo de la base de datos"""
    reply = message.reply_to_message
    if reply and reply.media:
        msg = await message.reply("Procesando...⏳", quote=True)
    else:
        await message.reply('Responda al archivo que desee eliminar de la base de datos con el comando /delete', quote=True)
        return

    for file_type in ("document", "video", "audio"):
        media = getattr(reply, file_type, None)
        if media is not None:
            break
    else:
        await msg.edit('Este formato de archivo no es compatible')
        return

    result = await Media.collection.delete_one({
        'file_name': media.file_name,
        'file_size': media.file_size,
        'mime_type': media.mime_type,
        'caption': reply.caption
    })
    if result.deleted_count:
        await msg.edit('El archivo se eliminó correctamente de la base de datos ✅')
    else:
        await msg.edit('Archivo no encontrado en la base de datos ❌')
