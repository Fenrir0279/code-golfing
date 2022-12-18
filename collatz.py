print((lambda n:[n]+(c:=lambda e:[]if e==1 else[e:=[e//2,e*3+1][e%2]]+c(e))(n))(int(input())))
# 94 characters
