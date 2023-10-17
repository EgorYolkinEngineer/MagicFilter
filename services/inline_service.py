from helpers.flags import extract_flags


def get_expression_result(query_text: str) -> str:
    query_text, flags = extract_flags(query_text)
    
    expression_result = str(eval(query_text))
    
    if "h" not in flags:
        expression_result = f"{query_text} = {expression_result}"
    
    return expression_result
    
    