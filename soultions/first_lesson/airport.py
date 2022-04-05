class Passenger:
    def __init__(self, name, ticket_id, ticket_class):
        self.name = name
        self.ticket_id = ticket_id
        self.ticket_class = ticket_class

    def __str__(self):
        return f'{self.name} {self.ticket_id} {self.ticket_class}.'


class Flight:

    def __init__(self, flight_id, destination):
        self.flight_id = flight_id
        self.destination = destination
        self.passengers = []

    def contains_ticket_id(self, passenger):
        for item in self.passengers:
            if item.ticket_id == passenger.ticket_id:
                return True
        return False

    def add_passenger(self, passenger):
        if not self.contains_ticket_id(passenger):
            self.passengers.append(passenger)
        else:
            print(f'Már van az alábbi jegyszámmal utas a gépen: {passenger.ticket_id}')

    def has_first_class(self):
        for passenger in self.passengers:
            if passenger.ticket_class == 1:
                return True
        return False

    def __str__(self):
        return f'Id: {self.flight_id} Destination: {self.destination} '


def init():
    passenger1 = Passenger("John", "12HJf", 1)
    passenger2 = Passenger("Jane", "12HJd", 2)
    passenger3 = Passenger("Jack", "12HJa", 3)
    passenger4 = Passenger("Jill", "12HJw", 2)
    passenger5 = Passenger("Jonathan", "12HJq", 3)
    passenger6 = Passenger("Bill", "12HJp", 3)
    passenger7 = Passenger("Jasmine", "12HJm", 3)
    passenger8 = Passenger("George", "12HJaa", 2)

    flight1 = Flight("sdio2", "London")
    flight2 = Flight("sdio3", "Budapest")
    flight3 = Flight("sdio4", "Liverpool")

    flight1.add_passenger(passenger1)
    flight1.add_passenger(passenger2)
    flight1.add_passenger(passenger3)
    flight1.add_passenger(passenger4)

    flight2.add_passenger(passenger2)
    flight2.add_passenger(passenger3)
    flight2.add_passenger(passenger5)

    flight3.add_passenger(passenger1)
    flight3.add_passenger(passenger8)
    flight3.add_passenger(passenger7)
    flight3.add_passenger(passenger6)
    flight3.add_passenger(passenger5)

    return [flight1, flight2, flight3]


def max_number_of_passengers(airport_in):
    max_flight = airport_in[0]
    for item in airport_in:
        if len(item.passengers) > len(max_flight.passengers):
            max_flight = item
    return max_flight


def flights_with_first_class(airport_in):
    result = []
    for flight in airport_in:
        if flight.has_first_class():
            result.append(flight)
    return result


def find_passenger(airport_in, ticket_id_in):
    dummy_passenger = Passenger("Dummy", ticket_id_in, 2)
    for flight in airport_in:
        if flight.contains_ticket_id(dummy_passenger):
            return flight
    return None


def find_flight(airport_in, flight_id_in):
    for item in airport_in:
        if item.flight_id == flight_id_in:
            return item
    return None


def is_correct_order(flight):
    for i in range(1, len(flight.passengers)):
        if flight.passengers[i].ticket_class < flight.passengers[i - 1].ticket_class:
            return False
    return True


def are_passengers_in_correct_order(airport_in, flight_id_in):
    searched_flight = find_flight(airport_in, flight_id_in)
    if searched_flight is not None:
        return is_correct_order(searched_flight)
    else:
        return True


if __name__ == '__main__':
    airport = init()
    print("1. feladat")
    print(f'Flight with max passengers: {max_number_of_passengers(airport)}')
    print("2. feladat")
    print(f'Flights with first class:')
    for item in flights_with_first_class(airport):
        print(f'    * {item}')

    print("3. feladat:")
    ticket_id = input("Ticket id: ")
    flight_result = find_passenger(airport, ticket_id)

    if flight_result is None:
        print("Cannot find passenger!")
    else:
        print(f'Destination: {find_passenger(airport, ticket_id).destination}')

    print("4. feladat:")
    flight_id = input("Flight id: ")
    if are_passengers_in_correct_order(airport, flight_id):
        print('Order is correct!')
    else:
        print('Order is NOT correct!')

    print("5. feladat")
    for flight in airport:
        if is_correct_order(flight):
            print('Order is correct!')
        else:
            print('Order is NOT correct!')
