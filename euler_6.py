print((f:=lambda n:n if n<0else(n+1)**2*n+f(n-1))(99)+1)
# 56 characters
# You can change 99 to int(input())-1 if you want user input instead of a constant value. The program is 68 characters long with this change.
