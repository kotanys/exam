a = []
def F(n):
    a.append(n)
    #print(n)
    if n < 5:
        F(n + 1)
        F(n + 2)
        
F(2)
print(sum(a))