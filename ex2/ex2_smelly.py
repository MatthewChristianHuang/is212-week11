class Shape:
    def calculate_area(self, shape_type, **kwargs):
        shape_class = {
            'circle': Circle,
            'rectangle': Rectangle,
            'triangle': Triangle,
        }.get(shape_type, UnknownShape)
        return shape_class().calculate_area(**kwargs)


class Circle:
    def calculate_area(self, **kwargs):
        radius = kwargs.get('radius')
        return 3.14 * radius * radius


class Rectangle:
    def calculate_area(self, **kwargs):
        length = kwargs.get('length')
        width = kwargs.get('width')
        return length * width


class Triangle:
    def calculate_area(self, **kwargs):
        base = kwargs.get('base')
        height = kwargs.get('height')
        return 0.5 * base * height


class UnknownShape:
    def calculate_area(self, **kwargs):
        return None
