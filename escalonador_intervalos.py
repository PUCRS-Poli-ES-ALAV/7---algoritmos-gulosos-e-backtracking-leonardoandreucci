def sdm_guloso(s, f):
    n = len(s)
    intervals = list(zip(s, f))
    
    # Ordena pelo final
    intervals.sort(key=lambda x: x[1])
    X = []
    fi = -float('inf')  
    iterations = 0  
    for i in range(n):
        iterations += 1  
        if intervals[i][0] > fi:  
            X.append(intervals[i])  
            fi = intervals[i][1]  
            
    return X, iterations

s = [4, 6, 13, 4, 2, 6, 7, 9, 1, 3, 9]
f = [8, 7, 14, 5, 4, 9, 10, 11, 6, 13, 12]

#s = [1, 2, 4]
#f = [3, 5, 6]


sdm, iterations = sdm_guloso(s, f)

print("Subcoleção Disjunta Máxima:", sdm)
print("Número de iterações:", iterations)
