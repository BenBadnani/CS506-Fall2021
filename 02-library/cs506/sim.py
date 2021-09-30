def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    dist = 0
    for i in range(len(x)):
        dist += abs(x[i] -y[i])
    return dist
    
def jaccard_dist(x, y):
    test = list(set(x+y))
    if len(test) == 0 or (len(test) == 1 and test[0] == 0):
        return 1
    intersection_cardinality = len(list(set(x) & set(y)))
    union_cardinality = len(x) + len(y)
    return intersection_cardinality/union_cardinality

def cosine_sim(x, y):

    test = list(set(x+y))
    if len(test) == 0 or (len(test) == 1 and test[0] == 0):
        return 1
    dot_prod = 0
    x_mag = 0
    y_mag = 0

    for i in range(len(x)):
        dot_prod += x[i]*y[i]

    x_mag = sum([elem**2 for elem in x])**(1/2)
    y_mag = sum([elem**2 for elem in y])**(1/2)

    return dot_prod/(x_mag * y_mag)


# Feel free to add more
