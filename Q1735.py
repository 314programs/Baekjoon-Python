frac1_top, frac1_bottom = map(int, input().split())
frac2_top, frac2_bottom = map(int, input().split())

#Add the fraction together by multiplying the base and the top
top = (frac1_top*frac2_bottom) + (frac2_top*frac1_bottom)
bottom = frac1_bottom*frac2_bottom

a,b = top, bottom
#Use euclidean algorithm to simplify
R = a%b
while R:
  a = b
  b = R
  R = a%b
print(str(top//b) + ' ' + str(bottom//b))
