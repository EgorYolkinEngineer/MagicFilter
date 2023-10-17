from src.config import BASE_FLAGS


def extract_flags(expression: str) -> tuple[str, list[str]]:
    found_flags = list()
    
    for flag in BASE_FLAGS:
        if '-' + flag in expression:
            found_flags.append(flag)
            expression = expression.replace("-" + flag, "")
    
    expression = expression.strip()
    
    return (expression, found_flags)
