def find_substring_occurrences(S, T):
   
    if not T:
        return []
    
    def build_prefix_function(pattern):
        n = len(pattern)
        pi = [0] * n
        j = 0
        
        for i in range(1, n):
            while j > 0 and pattern[i] != pattern[j]:
                j = pi[j - 1]
            if pattern[i] == pattern[j]:
                j += 1
            pi[i] = j
        return pi
    
    prefix_func = build_prefix_function(T)
    
    result = []
    j = 0
    n = len(S)
    m = len(T)
    
    for i in range(n):
        while j > 0 and S[i] != T[j]:
            j = prefix_func[j - 1]
        
        if S[i] == T[j]:
            j += 1
        
        if j == m:
            result.append(i - m + 1)
            j = prefix_func[j - 1]
    
    return result


def find_cyclic_shift(S, T):
    if len(S) != len(T):
        return -1
    
    if S == T:
        return 0
    
    doubled_S = S + S    
    pos = doubled_S.find(T)
    
    if pos != -1:
        return (len(S) - pos) % len(S)
    
    return -1

if __name__ == "__main__":
    try:
        S = input().strip()
        T = input().strip()
        
        result = find_cyclic_shift(S, T)
        print(result)
    except:
        print(-1)


if __name__ == "__main__":
    print("=== Задача 1: Поиск подстроки ===")
    try:
        S1 = input().strip()
        T1 = input().strip()
        
        indices = find_substring_occurrences(S1, T1)
        if indices:
            print(" ".join(map(str, indices)))
        else:
            print("")
    except:
        print("")
    
    print("\n=== Задача 2: Циклический сдвиг ===")
    try:
        S2 = input().strip()
        T2 = input().strip()
        
        shift = find_cyclic_shift(S2, T2)
        print(shift)
    except:
        print(-1)
