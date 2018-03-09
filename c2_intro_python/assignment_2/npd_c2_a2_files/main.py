'''Contains shape classes and does fun things with them

Shapes:
Triangles
Square
Circle

Data Attributes: (non-callable data)
shape_type
edge_length
name
allies
enemies

Methods:
area
perimeter
update_edge_length
add_ally
add_enemy
'''

class Square(object):
    shape_type = 'square'

    def __init__(self, edge_length, name, allies, enemies):
        self.edge_length = edge_length
        self.name = name
        self.allies = allies
        self.enemies = enemies

    def area(self):
        return self.edge_length**2

    def perimiter(self):
        return self.edge_length * 4

    def update_edge_length(self, new_length):
        self.edge_length = new_length
        return new_length

    def add_ally(self, shape_object):
        self.allies.append(shape_object)

    def add_enemy(self, shape_object):
        self.enemies.append(shape_object)

'''Creating Class Triange'''

class Triangle(object):
    shape_type = 'triangle'

    def __init__(self, edge_length, name, allies, enemies):
        self.edge_length = edge_length
        self.name = name
        self.allies = allies
        self.enemies = enemies

    def area(self):
        return ((self.edge_length**2) / 2)

    def perimeter(self):
        return self.edge_length * 3

    def update_edge_length(self, new_length):
        self.edge_length = new_length
        return new_length

    def add_ally(self, shape_object):
        self.allies.append(shape_object)

    def add_enemy(self, shape_object):
        self.enemies.append(shape_object)

'''Creating Class Circle'''

class Circle(object):
    shape_type = 'circle'

    def __init__(self, edge_length, name, allies, enemies):
        self.edge_length = edge_length
        self.name = name
        self.allies = allies
        self.enemies = enemies

    def area(self):
        '''Area of a circle based on edge_length/2 = radius'''
        return 3.14 * (1/2) * self.edge_length**2

    def perimeter(self):
        '''assumption that radius is 1/2 edge_length'''
        return 2 * 3.14 * (1/2) * self.edge_length

    def update_edge_length(self, new_length):
        self.edge_length = new_length
        return new_length

    def add_ally(self, shape_object):
        self.allies.append(shape_object)

    def add_enemy(self, shape_object):
        self.enemies.append(shape_object)


    def __repr__(self):
        return "<Person {}".format(self.name)

def main():
    '''Assignment:
    -Create two objects from each class
    -Make triangles and circles allies
    -Make squares enemies of triangles and circles
    -Print each object's name, its shape type, its friends, and its enemies'''

    square_sally = Square(3, "Sally", [], [])
    square_sam = Square(2, "Sam", [], [])
    circle_clint = Circle(5, "Clint", [], [])
    circle_clint.add_enemy("square")
    circle_clint.add_ally("triangle")
    circle_cassie = Circle(7, "Cassie", [], [])
    circle_cassie.add_enemy("square")
    circle_cassie.add_ally("triangle")
    triangle_tom = Triangle(5.5, "Tom", [], [])
    triangle_tom.add_enemy("square")
    triangle_tom.add_ally("circle")
    triangle_tina = Triangle(23, "Tina", [], [])
    triangle_tina.add_enemy("square")
    triangle_tina.add_ally("circle")

    print(vars)
    # rolodex = {}
    # square_sam = Square(5, "Sam", [], [])
    # sam_stats = {
    #     'area': square_sam.area(),
    #     'allies': square_sam.allies,
    #     'enemies': square_sam.enemies,
    #     'name': 'sam',
    # }
    # rolodex['Sam'] = sam_stats
    # print(rolodex.values())

if __name__ == '__main__':
    main()
