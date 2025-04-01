def common(set1, set2):
    return set1.intersection(set2)

A = {"london", "paris", "tokyo", "cairo", "athens"}
B = {"london", "berlin", "seol", "cairo", "rome"}

print(common(A,B))