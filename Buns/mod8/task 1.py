class Transport:
    def __init__(self, coordinates, speed, brand, year, number):
        self._coordinates = coordinates
        self._speed = speed
        self._brand = brand
        self._year = year
        self._number = number

    @property
    def coordinates(self):
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        if all(type(item) is int for item in coordinates) and coordinates.lenght == 2:
            self._coordinates = coordinates
        else:
            raise ValueError("Ожидалось Array of int значение")

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, speed):
        if type(speed) is int:
            self._speed = speed
        else:
            raise ValueError("Ожидалось int значение")

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        if type(brand) is str:
            self._brand = brand
        else:
            raise ValueError("Ожидалось string значение")

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, year):
        if type(year) is int:
            self._year = year
        else:
            raise ValueError("Ожидалось int значение")

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        if type(number) is str:
            self._number = number
        else:
            raise ValueError("Ожидалось string значение")

    def __str__(self):
        """
           Представление всей информации для вывода в методе print()
        """
        return (f"coordinates={self._coordinates}, "
                f"speed={self._speed}, brand={self._brand}, "
                f"year={self._year}, number={self._number}")

    def isInArea(self, pos_x, pos_y, length, width) -> bool:
        """
        Присутствие транспортного средства в пределах заданнй области
        pos_x, pos_y - координата левого верхнего угла области
        length, width - длина и ширина области
        """
        x, y = self.coordinates
        if x <= pos_x + length and x >= pos_x:
            if y >= pos_y and y <= pos_y + width:
                return True
        else:
            return False

    def Move(self, coordinates):
        coordinates[0] += 1
        coordinates[1] += 1
        return coordinates


class Passenger:
    def __init__(self, number_of_passengers, passengers_capacity):
        self._number_of_passengers = number_of_passengers
        self._passengers_capacity = passengers_capacity

    @property
    def passengers_capacity(self):
        return self._passengers_capacity

    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity):
        if type(passengers_capacity) is int:
            self._passengers_capacity = passengers_capacity
        else:
            raise ValueError("Ожидалось int значение")

    @property
    def number_of_passengers(self):
        return self._number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers):
        if type(number_of_passengers) is int:
            self._number_of_passengers = number_of_passengers
        else:
            raise ValueError("Ожидалось int значение")


class Cargo:
    def __init__(self, carrying, cargo):
        self.__carrying = carrying
        self._cargo = cargo

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, cargo):
        if self.cargo > self.__carrying:
            print("Груз непоместиться")
        elif type(cargo) is int:
            self._cargo = cargo
        else:
            raise ValueError("Ожидалось int значение")

    @property
    def carrying(self):
        return self.__carrying

    @carrying.setter
    def carrying(self, carrying):
        if type(carrying) is int:
            self.__carrying = carrying
        else:
            raise ValueError("Ожидалось int значение")


class Plane(Transport):
    def __init__(self, height, payload, coordinates, speed, brand, year, number):
        super().__init__(coordinates, speed, brand, year, number)
        self._height = height
        self._payload = payload

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if type(height) is int:
            self._height = height
        else:
            raise ValueError("Ожидалось int значение")

    @property
    def payload(self):
        return self._height

    @payload.setter
    def payload(self, payload):
        if type(payload) is int:
            self._payload = payload
        else:
            raise ValueError("Ожидалось int значение")


class Auto(Transport):
    def __init__(self, color, coordinates, speed, brand, year, number, type_of_car, oil_level):
        super().__init__(coordinates, speed, brand, year, number)
        self._color = color
        self._type_of_car = type_of_car
        self._oil_level = oil_level

    @property
    def type(self):
        return self._type_of_car

    @type.setter
    def type(self, type_of_car):
        if type(type_of_car) is str:
            self._type_of_car = type_of_car
        else:
            raise ValueError("Ожидалось string значение")

    @property
    def color(self):
        return self.color

    @color.setter
    def color(self, color):
        if type(color) is int:
            self._color = color
        else:
            raise ValueError("Ожидалось int значение")

    @property
    def oil_level(self):
        return self.color

    @oil_level.setter
    def oil_level(self, oil_level):
        if oil_level > 100:
            raise ("Максимальной уровень масла 100")
        if type(oil_level) is int:
            self._oil_level = oil_level
        else:
            raise ValueError("Ожидалось int значение")

    def check_oil_level(self):
        return self._oil_level


class Ship(Transport):
    def __init__(self, name, coordinates, speed, brand, year, number, port, purpose):

        super().__init__(coordinates, speed, brand, year, number)
        self._name = name
        self._port = port
        self._purpose = purpose

    @property
    def purpose(self):
        return self._purpose

    @purpose.setter
    def purpose(self, purpose):
        if type(purpose) is str:
            self._purpose = purpose
        else:
            raise ValueError("Ожидалось str значение")

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name):
        if type(name) is str:
            self._name = name
        else:
            raise ValueError("Ожидалось string значение")

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, port):
        if type(port) is str:
            self._port = port
        else:
            raise ValueError("Ожидалось string значение")


class Car(Auto):

    def __init__(self, color, coordinates, speed, brand, year, number, type_of_car, oil_level):
        super().__init__(color, coordinates, speed, brand, year, number, type_of_car, oil_level)

    def add_oil(self):
        if self.oil_level + 10 < 100:
            self.oil_level += 10
        elif self.oil_level + 10 > 100:
            self.oil_level = 100
        else:
            print("Уровень масла на отметке MAX")


class Bus(Auto, Passenger):

    def __init__(self, color, coordinates, speed, brand, year, number, type_of_car, oil_level,
                 number_of_passengers, passengers_capacity):

        super().__init__(color, coordinates, speed, brand, year, number, type_of_car, oil_level)
        super().__init__(passengers_capacity, number_of_passengers)

    def bus_boarding(self):
        if self.number_of_passengers > self.passengers_capacity:
            print("Мест больше нет. Пассажиров осталось без места: "
                  + self.passengers_capacity - self.number_of_passengers)
        else:
            self.passengers_capacity -= self.number_of_passengers
            print("посадка прошла успешно. Места осталось: " + self.passengers_capacity - self.number_of_passengers)


class CargoAuto(Auto, Cargo):

    def __init__(self, color, coordinates, speed, brand, year, number, type_of_car, oil_level, carrying, cargo):
        super().__init__(color, coordinates, speed, brand, year, number, type_of_car, oil_level)
        super().__init__(carrying, cargo)

    def load_car(self):
        if self.carrying > self._cargo:
            self.carrying -= self._cargo
            print("загрузка прошла успешно")
        else:
            self.carrying -= self._cargo
            print("груза больше, чем места в машине :( места осталось" + self.carrying - self._cargo)


class Boat(Ship):
    def __init__(self, name, coordinates, speed, brand, year, number, port, purpose, fuel):
        super().__init__(name, coordinates, speed, brand, year, number, port, purpose)
        self._fuel = fuel

    @property
    def fuel(self):
        return self._fuel

    @fuel.setter
    def fuel(self, fuel):
        if self._fuel > 100:
            raise ValueError("Максимальное кол-во топлива 100")

        elif type(fuel) is int:
            self._fuel = fuel
        else:
            raise ValueError("Ожидалось int значение")

    def fill_fuel(self):
        if self._fuel + 10 < 100:
            self._fuel += 10
        if self._fuel + 10 > 100:
            self._fuel = 100
        else:
            print("И так полный бак... остатки вылились ")


class PassengerShip(Ship, Passenger):
    def __init__(self, name, coordinates, speed, brand, year, number, port,
                 purpose, number_of_passengers, passengers_capacity):

        super().__init__(name, coordinates, speed, brand, year, number, port, purpose)
        super().__init__(number_of_passengers, passengers_capacity)

    def take_passenger(self):
        if self.passengers_capacity < self.number_of_passengers:
            print("борт полон осталось: " + self.passengers_capacity - self.number_of_passengers + "людей")
            self.passengers_capacity -= self.number_of_passengers
        else:
            self.passengers_capacity -= self.number_of_passengers
            print("Посадка окончена")


class CargoShip(Ship, Cargo):

    def __init__(self, name, coordinates, speed, brand, year, number, port, purpose, carrying, cargo):
        super().__init__(name, coordinates, speed, brand, year, number, port, purpose)
        super().__init__(carrying, cargo)

    def load_ship(self):
        if self.carrying > self._cargo:
            self.carrying -= self._cargo
            print("Загрузка прошла успешно")
        else:
            self.carrying -= self._cargo
            print("груза больше, чем вместимость корабля :( места осталось" + self.carrying - self._cargo)


class PassengerPlane(Plane, Passenger):

    def __init__(self, height, payload, coordinates, speed, brand, year, number, number_of_passengers,
                 passengers_capacity):
        super().__init__(height, payload, coordinates, speed, brand, year, number)
        super().__init__(number_of_passengers, passengers_capacity)

    def plane_boarding(self):
        if self.number_of_passengers > self.passengers_capacity:
            print("Мест больше нет. Пассажиров осталось без места: "
                  + self.passengers_capacity - self.number_of_passengers)
            self.passengers_capacity -= self.number_of_passengers
        else:
            self.passengers_capacity -= self.number_of_passengers
            print("посадка прошла успешно. Места осталось: " + self.passengers_capacity - self.number_of_passengers)
            self.passengers_capacity -= self.number_of_passengers


class CargoPlane(Plane, Cargo):
    def __init__(self, height, payload, coordinates, speed, brand, year, number, carrying, cargo):
        super().__init__(height, payload, coordinates, speed, brand, year, number)
        super().__init__(carrying, cargo)

    def load_plane(self):
        if self.carrying > self._cargo:
            self.carrying -= self._cargo
            print("Загрузка прошла успешно")
        else:
            self.carrying -= self._cargo
            print("груза больше, чем вместимость самолета :( места осталось" + self.carrying - self._cargo)


class SeaPlane(Plane,Ship):

    def __init__(self, height, payload, coordinates, speed, brand, year, number,name, port,purpose):
        super().__init__(height, payload, coordinates, speed, brand, year, number)
        super().__init__(name, coordinates, speed, brand, year, number, port, purpose)


