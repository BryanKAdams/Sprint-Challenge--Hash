def get_indices_of_item_weights(weights, length, limit):

    """
    YOUR CODE HERE
    """
    keyweight = {}
    for idx, val in enumerate(weights):
        if val in keyweight:
            keyweight[val].append(idx)
        else:
            keyweight[val] = [idx]
            
    if length < 2:
        return None
    else:
        for idx, val in enumerate(weights):
            match = limit - val
            if match in keyweight:
                if match == val:
                    if len(keyweight[match]) > 1:
                        return (keyweight[match][1], keyweight[match][0])
                else:
                    index2 = keyweight[match][0]
                    if index2 > idx:
                        return (index2, idx)
                    else:
                        return(idx, index2)
        return None

