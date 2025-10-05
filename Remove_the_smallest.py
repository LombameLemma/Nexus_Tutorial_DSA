def can_reduce_to_one_element(test_cases):
    results = []
    for case in test_cases:
        n, arr = case
        min_val = min(arr)
        max_val = max(arr)
        if max_val - min_val <= 1:
            results.append("YES")
        else:
            results.append("NO")
    return results
