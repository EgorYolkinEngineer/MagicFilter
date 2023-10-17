from src.config import TELEGRAM_API_KEY
from src.config import dispatcher, bot
from handlers import inline, messages

import asyncio

dispatcher.include_routers(inline.router, 
                           messages.router)


async def main():
    await dispatcher.start_polling(bot)
    

if __name__ == "__main__":
    asyncio.run(main())