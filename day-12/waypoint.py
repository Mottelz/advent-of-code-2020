class ShipWithWaypoint:
    def __init__(self, boat_north=0, boat_east=0, waypoint_north=1, waypoint_east=10):
        self.__boat_north = boat_north
        self.__boat_east = boat_east
        self.__waypoint_north = waypoint_north
        self.__waypoint_east = waypoint_east

    def turn_right(self, dgr: int):
        for i in range((dgr % 90) + 1):
            self.__waypoint_east, self.__waypoint_north = self.__waypoint_north, self.__waypoint_east * -1

    def turn_left(self, dgr: int):
        for i in range((dgr % 90) + 1):
            self.__waypoint_east, self.__waypoint_north = self.__waypoint_north * -1, self.__waypoint_east

    def move_north(self, units: int):
        self.__waypoint_north += units

    def move_south(self, units: int):
        self.__waypoint_north -= units

    def move_east(self, units: int):
        self.__waypoint_east += units

    def move_west(self, units: int):
        self.__waypoint_east -= units

    def move_forward(self, units: int):
        for i in range(units):
            self.__boat_north += self.__waypoint_north
            self.__boat_east += self.__waypoint_east

    def get_location(self):
        return self.__boat_north, self.__boat_east

    def __abs__(self):
        return abs(self.__boat_north)+abs(self.__boat_east)

    def __str__(self):
        return f"Ship: {self.__boat_north}N{self.__boat_east}E, " \
               f"Waypoint: {self.__waypoint_north}N{self.__waypoint_east}E, " \
               f"MD: {abs(self)}"
