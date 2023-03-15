def alpha_omega():
    x = [1, 2, 3, 4, 5]
    idx1 = x.index(1)
    idx2 = x.index(5)
    x[idx1], x[idx2] = x[idx2], x[idx1]
    print(x)
alpha_omega()