def has_negatives(a):

    """
    YOUR CODE HERE
    """
    negatives = {}
    for item in a:
        if item < 0:
            negatives[item] = 1
    results = []
    for item in a:
        if item > 0:
            if -item in negatives:
                results.append(item)
    return results

if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
