def lagranzh(x0, x, y):
    l = [0] * len(x)
    for i in range(len(x)):
        l[i] = 1
        for j in range(len(x)):
            if i != j:
                l[i] *= (x0 - x[j]) / (x[i] - x[j])
    res = 0
    for i in range(len(x)):
        res += l[i] * y[i]
    return res
