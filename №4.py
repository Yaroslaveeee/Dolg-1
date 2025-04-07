def find_min_max(a):
    if not a:
        return None
    return (min(a), max(a))

print(find_min_max([1,2,3,4,52]))

