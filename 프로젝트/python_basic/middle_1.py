def print_diamond(height):
    if height % 2 == 0:
        print("숫자로 입력해주세요")
        return

    for i in range(height // 2 + 1):
        spaces = ' ' * (height // 2 - i)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)

    for i in range(height // 2 - 1, -1, -1):
        spaces = ' ' * (height // 2 - i)
        stars = '*' * (2 * i + 1)
        print(spaces + stars)

h=print_diamond(5)