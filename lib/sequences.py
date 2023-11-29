def remove_duplicates(sequence):
    visited = set()
    result = []
    
    for item in sequence:
        if item not in visited:
            result.append(item)
            visited.add(item)
    
    if isinstance(sequence, tuple):
        result = tuple(result)
    
    return result

input_sequence = [4, 2, 2, 6, 5, 3, 6,4 ,3]
result = remove_duplicates(input_sequence)
print(result)  