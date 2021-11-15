class Rectangle:

    def __init__(self, length, width, color="red"):
        self.length = length
        self.width = width
        self.color = color

    def calculate_area(self):
        return self.width * self.length


class ToolBox:
    def __init__(self):
        self.tools = []

    def add_tool(self, tool):
        pass

    def remove_tool(self, tool):
        pass


class ScrewDriver:
    def __init__(self, size):
        self.size = size

    def tighten(self, screw):
        pass

    def loosen(self, screw):
        pass


class Hammer:
    def __init__(self, color="red"):
        self.color = color

    def paint(self, color):
        self.color = color

    def hammer_in(self, nail):
        pass

    def remove(self, nail):
        pass


class Screw:
    """Vis."""

    MAX_TIGHTNESS = 5

    def __init__(self):
        self.tightness = 0

    def loosen(self):
        if self.tightness > 0:
            self.tightness -= 1

    def tighten(self):
        if self.tightness < self.MAX_TIGHTNESS:
            self.tightness += 1

    def __str__(self):
        return "Vis avec un serrage de {}".format(self.tightness)


class Nail:
    """Clou."""

    def __init__(self):
        self.in_wall = False

    def nail_in(self):
        if not self.in_wall:
            self.in_wall = True

    def remove(self):
        if self.in_wall:
            self.in_wall = False

    def __str__(self):
        wall_state = "dans le mur" if self.in_wall else "hors du mur"
        return f"Clou {wall_state}."


# Instancier une boîte à outil, un tournevis, et un marteau
box_1 = ToolBox()
screw_driver_1 = ScrewDriver(2)
hammer_1 = Hammer("blue")

# Placer le marteau et le tournevis dans la boîte à outils
box_1.add_tool(screw_driver_1)
box_1.add_tool(hammer_1)

# Instancier une vis, et serrez-là avec le tournevis. Affichez la vis avant et après l'avoir serrée
screw_1 = Screw()
print(screw_1.__str__())
screw_1.tighten()
print(screw_1.__str__())

# Instancier un clou, puis enfoncez-le avec le marteau. Afficher le clou avant et après
nail_1 = Nail()
print(nail_1.__str__())
nail_1.nail_in()
print(nail_1.__str__())

"""
rect = Rectangle(3, 6, "blue")
rect2 = Rectangle(4, 7, "pink")
print(rect.length)
print(rect.calculate_area())
print(rect.color)
print(rect2.color)
print(rect2.calculate_area())
"""