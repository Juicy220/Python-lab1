def shell_sort(inp, n):
 
    h = n // 2
    while h > 0:
        for i in range(h, n):
            t = inp[i]
            j = i
            while j >= h and inp[j - h] > t:
                inp[j] = inp[j - h]
                j -= h
 
            inp[j] = t
        h = h // 2
