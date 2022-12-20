print((f:=lambda n:n if n<2else 2*f(n-1)+f(n-2))(int(input())))
# 63 characters
# gives the nth Pell number where n is the user's input
