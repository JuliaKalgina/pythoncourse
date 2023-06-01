class Shape:
    def __init__(self, color, size, corners):
        self.color = color
        self.size = size
        self.corners = corners


class Square(Shape):
    def __init__(self, color, size, corners):
        super().__init__(color, size, corners)
        self.type = 'Square'


class Circle(Shape):
    def __init__(self, color, size, corners):
        super().__init__(color, size, corners)
        self.type = 'Circle'


class Triangle(Shape):
    def __init__(self, color, size, corners):
        super().__init__(color, size, corners)
        self.type = 'Triangle'


class Box:
    def __init__(self, contents: list):
        self.contents = contents

    def put_in_a_box(self, item):
        self.contents.append(item)

    def list_contents(self):
        result = ''
        for item in self.contents:
            description = item.size + ' ' + item.color + ' ' + item.type.lower()
            result += description + ' '
        return result


A_Square = Square('green', 'medium', 4)
print(A_Square.type)
The_Box = Box([])
The_Box.put_in_a_box(A_Square)
print(The_Box.list_contents())