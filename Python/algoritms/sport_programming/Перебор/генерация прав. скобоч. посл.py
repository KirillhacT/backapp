n = 3

def rec(idx, balance, a=""):
    if idx == 2 * n:
        if balance == 0:
            print(a)
    else:
        if balance < n:
            rec(idx + 1, balance + 1, a + "(")
        if balance > 0:
            rec(idx + 1, balance - 1, a + ")")
rec(0, 0)

