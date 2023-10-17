from aiogram.dispatcher.router import Router
from aiogram.filters.command import CommandStart
from aiogram.types import Message

from src.config import bot

router = Router()


@router.message(CommandStart())
async def command_start_route(message: Message) -> None:
    bot_info = await bot.get_me()
    bot_username = bot_info.username
    
    answer = (
        f"Hello!\n\n"
        f"Using me:\n\n"
        f"@{bot_username} (1 + 2) / 3 # => send «(1 + 2) / 3 = 1» on open chat\n\n"
        f"Hide expression:\n\n"
        f"@{bot_username} -h (1 + 2) / 3 # => send «3» on open chat\n\n"
    )
    await message.answer(text=answer)
