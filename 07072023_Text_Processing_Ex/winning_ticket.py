def check_ticket(ticket):

    if len(ticket) != 20:
        return "invalid ticket"

    winning_symbols = ['@', '#', '$', '^']
    left_side = ticket[:10]
    right_side = ticket[10:]

    for symbol in winning_symbols:
        for uninterrupted_match_length in range(10, 5, -1):
            winning_symbols_repetition = symbol * uninterrupted_match_length
            if winning_symbols_repetition in left_side and winning_symbols_repetition in right_side:
                if uninterrupted_match_length == 10:
                    return f'ticket "{ticket}" - {uninterrupted_match_length}{symbol} Jackpot!'
                return f'ticket "{ticket}" - {uninterrupted_match_length}{symbol}'

    return f'ticket "{ticket}" - no match'


tickets = [ticket.strip() for ticket in input().split(", ")]

for ticket in tickets:
    print(check_ticket(ticket))

