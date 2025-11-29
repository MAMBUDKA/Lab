def min_removals_for_valid_parentheses(s):
    stack = []
    removals = 0
    bracket_pairs = {')': '(', ']': '[', '}': '{'}
    
    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if stack and stack[-1] == bracket_pairs[char]:
                stack.pop()
            else:
                removals += 1
        else:
            removals += 1
    
    removals += len(stack)
    
    return removals


def nearest_smaller_right(n, arr):
    result2 = [-1] * n
    stack = []
    
    for i in range(n):
        while stack and arr[i] < arr[stack[-1]]:
            idx = stack.pop()
            result2[idx] = i
        stack.append(i)
    
    return result2


if __name__ == "__main__":
    print("=== Задача 1: Получение ПСП ===")
    try:
        s = input().strip()
        result1 = min_removals_for_valid_parentheses(s)
        print(result1)
    except:
        print(0)
    
    print("\n=== Задача 2: Ближайший меньший ===")
    try:
        n = int(input().strip())
        arr = list(map(int, input().strip().split()))
        result2 = nearest_smaller_right(n, arr)
        print(" ".join(map(str, result2)))
    except:
        print("")
