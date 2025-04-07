def filter_greater_than(a, b):
    c = []
    for i in a:
        if i > b:
            c.append(i)
    return c


print(filter_greater_than([1,3,5,6,9], 5))





