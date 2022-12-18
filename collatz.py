print([n:=int(input())]+(c:=lambda e:[]if e==1 else[e:=[e//2,e*3+1][e%2]]+c(e))(n))
# 83 characters
