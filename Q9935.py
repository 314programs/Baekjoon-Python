#I forgot that [:] exisited, so I struggled with a harder method until I saw someone using [:]
Word = input()
Trigger = input()
Stack = []

for i in range(len(Word)):
    char = Word[i]
    Stack.append(char)
    if char == Trigger[-1] and ''.join(Stack[len(Stack) -len(Trigger):]) == Trigger:
        for x in range(len(Trigger)):
            Stack.pop()
    
if Stack:
    print(''.join(Stack))
else:
    print('FRULA')
