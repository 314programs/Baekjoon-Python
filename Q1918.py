#deque to generate a stack
from collections import deque

Expression = input()
#Dictionary in order of importance
prec = {'*':3, '/':3, '+':2, '-':2, '(':1}
opStack = deque([])
postfixList = []
tokenlist = list(Expression)

for token in tokenlist:
  #If character is an alphabet, just append it in postfixList
    if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        postfixList.append(token)
  #If it is a start of a bracket, append it to the opStack, used to store symbols
    elif token == '(':
        opStack.appendleft(token)
  #If it is a end of a bracket, append symbols from opStack that was previously stored untill it reaches a bracket
    elif token == ')':
        topToken = opStack.popleft()
        while topToken != '(':
            postfixList.append(topToken)
            topToken = opStack.popleft()
   #If it is a symbol other than a bracket, compare its order of importance to the previous symbols stored in the stack and append to postfixList
    else:
        while len(opStack) != 0 and prec[opStack[0]] >= prec[token]:
            postfixList.append(opStack.popleft())
        opStack.appendleft(token)
        
while len(opStack) != 0:
    postfixList.append(opStack.popleft())
    
print(''.join(postfixList))
