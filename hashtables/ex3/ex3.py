def intersection(arrays):

    """
    YOUR CODE HERE
    """
    if len(arrays) == 1:
        return arrays[0]
    else:
        tables = []
        for i in range(1,len(arrays)):
            tables.append({})
            for y in arrays[i]:
                tables[i - 1][y] = 1
        results = []
        
        for item in arrays[0]:
            found = True
            for table in tables:
                if item not in table:
                    found = False
                    break
            if found:
                results.append(item)
    return results


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000,2000000)) + [1,2,3])
    arrays.append(list(range(2000000,3000000)) + [1,2,3])
    arrays.append(list(range(3000000,4000000)) + [1,2,3])

    print(intersection(arrays))
