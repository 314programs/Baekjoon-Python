print('\n')
while True:
  Phase = input()
  if Phase == 'I quacked the code!':
    print('\n')
    break
  if Phase[-1] == '.':
    print('*Nod*')
    print('\n')
  elif Phase[-1] == '?':
    print('Quack!')
    print('\n')
