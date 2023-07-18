card_values = {
    '2': 1,
    '3': 1,
    '4': 1,
    '5': 1,
    '6': 1,
    '7': 0,
    '8': 0,
    '9': 0,
    '10': -1,
    'J': -1,
    'Q': -1,
    'K': -1,
    'A': -1
}

running_count = 0

while True:
    user_input = input('Enter the card: ')
    if user_input == 'q':
        break
    else:
        running_count += card_values[user_input]
        print(f'Running count: {running_count}')
        if running_count > 2:
            print('high')
        elif running_count < 2:
            print('low')
        else:
            print('minimum')
