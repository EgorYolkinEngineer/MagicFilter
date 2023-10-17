from aiogram.dispatcher.router import Router
from aiogram.types import (InlineQuery, 
                           InlineQueryResultArticle,
                           InputTextMessageContent)

from services.inline_service import get_expression_result

router = Router()


@router.inline_query()
async def inline_route(query: InlineQuery) -> None:
    query_text = query.query.strip()
    
    query_expression_result = get_expression_result(query_text)
    
    
    results = [InlineQueryResultArticle(
        id=str(1),
        title=query_expression_result,
        input_message_content=InputTextMessageContent(
            message_text=query_expression_result, 
            disable_web_page_preview=True
        )
    )]
    await query.answer(results)
    