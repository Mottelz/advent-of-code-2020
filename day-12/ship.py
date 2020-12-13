class Ship:
    def __init__(self, north=0, east=0, heading=0):
        self.___north = north
        self.___east = east
        self.__heading = heading

    def turn_right(self, dgr: int):
        self.__heading = (self.__heading + dgr) % 360

    def turn_left(self, dgr: int):
        self.__heading = (self.__heading - dgr) % 360

    def move_north(self, units: int):
        self.___north += units

    def move_south(self, units: int):
        self.___north -= units

    def move_east(self, units: int):
        self.___east += units

    def move_west(self, units: int):
        self.___east -= units

    def move_forward(self, units: int):
        if self.__heading == 0:
            self.move_east(units)

        elif self.__heading == 90:
            self.move_south(units)

        elif self.__heading == 180:
            self.move_west(units)

        elif self.__heading == 270:
            self.move_north(units)

    def get_location(self):
        return self.___north, self.___east

    def __abs__(self):
        return abs(self.___north)+abs(self.___east)

    def __str__(self):
        return f"Ship at {self.___north}N{self.___east}E, heading: {self.__heading}, MD: {abs(self)}"
