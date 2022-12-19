print((f:=lambda n:n if n<0else(n+1)**2*n+f(n-1))(int(input())-1)+1)
# 68 characters
