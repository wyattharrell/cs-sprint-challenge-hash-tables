def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """

    counter = 0
    dict = {}
    for item in weights:
        # if item in dict:
        #     x = dict[item]
        #     tup = (x, counter)
        #     dict[item] = tup
        # else:
        dict[item] = counter
        counter += 1

    print(dict)
    for item in weights:
        temp = limit - item
        if temp in dict:
            l = [dict[temp]]
            l.append(dict[item])
            print(l)
            return l

    return None
