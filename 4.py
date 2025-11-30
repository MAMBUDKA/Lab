import sys

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert_node(root, value):
    """Вставка узла в двоичное дерево поиска"""
    if root is None:
        return TreeNode(value)
    
    if value < root.value:
        root.left = insert_node(root.left, value)
    elif value > root.value:
        root.right = insert_node(root.right, value)
    
    return root

def build_tree():
    """Построение дерева"""
    print("Введите числа для построения дерева (0 для завершения):")
    root = None
    
    while True:
        try:
            line = input().strip()
            if not line:
                continue
                
            numbers = list(map(int, line.split()))
            for num in numbers:
                if num == 0:
                    return root
                root = insert_node(root, num)
                
        except EOFError:
            break
        except ValueError:
            print("Пожалуйста, вводите только целые числа")
            continue
    
    return root

# Задача 1: Вершины с одним ребенком
def find_single_child_nodes(root, result):
    """Поиск вершин с одним ребенком"""
    if root is None:
        return
    
    children_count = 0
    if root.left:
        children_count += 1
    if root.right:
        children_count += 1
    
    if children_count == 1:
        result.append(root.value)
    
    find_single_child_nodes(root.left, result)
    find_single_child_nodes(root.right, result)

# Задача 2: Проверка сбалансированности
def get_height_and_balance(root):
    """Возвращает высоту и флаг сбалансированности"""
    if root is None:
        return 0, True
    
    left_height, left_balanced = get_height_and_balance(root.left)
    right_height, right_balanced = get_height_and_balance(root.right)
    
    height = max(left_height, right_height) + 1
    current_balanced = abs(left_height - right_height) <= 1
    balanced = current_balanced and left_balanced and right_balanced
    
    return height, balanced

def main():
    # Способ 1: Интерактивный ввод
    root = build_tree()
    
    if root is None:
        print("Дерево пустое")
        return
    
    # Задача 1
    print("\n=== Задача 1: Вершины с одним ребенком ===")
    result1 = []
    find_single_child_nodes(root, result1)
    for value in sorted(result1):
        print(value)
    
    # Задача 2
    print("\n=== Задача 2: Сбалансированность дерева ===")
    _, balanced = get_height_and_balance(root)
    print("YES" if balanced else "NO")

if __name__ == "__main__":
    main()