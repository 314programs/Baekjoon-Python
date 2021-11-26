word = input()
if len(word) < 5:
    print('not cute')
else:
    if word[len(word)-5:len(word)] == 'driip':
        print('cute')
    else:
        print('not cute')
