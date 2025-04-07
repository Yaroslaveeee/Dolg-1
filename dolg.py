#1
class Stack:
    def __init__(self, size=10):
        self.size = size
        self.stack = [None] * size
        self.top_index = -1

    def push(self, value):
        if self.top_index == self.size - 1:
            print("Ошибка: Стек переполнен")
            return False
        self.top_index += 1
        self.stack[self.top_index] = value
        return True

    def pop(self):
        if self.is_empty():
            print("Ошибка: Стек пуст")
            return None
        value = self.stack[self.top_index]
        self.stack[self.top_index] = None
        self.top_index -= 1
        return value

    def top(self):
        if self.is_empty():
            print("Ошибка: Стек пуст")
            return None
        return self.stack[self.top_index]

    def is_empty(self):
        return self.top_index == -1

    def __str__(self):
        return str(self.stack[:self.top_index + 1])


# Пример использования
if __name__ == "__main__":
    stack = Stack(5)

    print("Добавляем элементы:")
    for i in range(1, 7):
        if stack.push(i):
            print(f"Добавлено: {i}, Стек: {stack}")

    print("\nВерхний элемент:", stack.top())

    print("\nУдаляем элементы:")
    while not stack.is_empty():
        print(f"Удалено: {stack.pop()}, Стек: {stack}")

    print("\nПопытка удалить из пустого стека:")
    stack.pop()

    print("\nПопытка посмотреть верхний элемент пустого стека:")
    print(stack.top())