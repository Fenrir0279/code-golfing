print((lambda e:sum(filter(lambda q:not q%2,[(d:=lambda n:d(n-1)+d(n-2)if n>1 else n)(i)for i in range(e)])))(int(input())))
