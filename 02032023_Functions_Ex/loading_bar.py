def loading_bar(some_number:int) -> str:
    if some_number == 100:
        return "100% Complete! \n[%%%%%%%%%%]"
    else:
        loaded_percenmts = some_number // 10
        return f"{some_number}% [{'%' * loaded_percenmts}{'.'* (10 - loaded_percenmts) }]\nStill loading..."


input_integer = int(input())
print(loading_bar(input_integer))
