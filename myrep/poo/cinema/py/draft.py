class Client:
    def __init__(self, id: str, phone: int):
        self.__id = id
        self.__phone = phone

    def getId(self):
        return self.__id
    
    def getPhone(self):
        return self.__phone
    
    def setId(self, id: str):
        self.__id = id

    def setPhone(self, phone: int):
        self.__phone = phone

    def __str__(self):
        return f"{self.__id}:{self.__phone}"


class Theater:
    def __init__(self, capacity: int):
        self.__seats: list[Client | None] = []
        for _ in range (capacity):
            self.__seats.append(None)

    def search(self, name: str):
        for i, client in enumerate(self.__seats):
            if client and client.getId() == name:
                return i
        return -1
    
    def verifyIndex(self, index: int):
        return 0 <= index < len(self.__seats)
    
    def reserve(self, id :str, phone: int, index: int):
        if not self.verifyIndex(index):
            print("fail: cadeira nao existe")
            return False
        if self.__seats[index] is not None:
            print("fail: cadeira ja esta ocupada")
            return False
        e_sitting = self.search(id)
        if e_sitting != -1:
            print("fail: cliente ja esta no cinema")
            return False
        self.__seats[index] = Client(id, phone)
        return True


    def cancel(self, id: str):
        seat_i = self.search(id)
        if seat_i == -1:
            print("fail: cliente nao esta no cinema")
            return
        self.__seats[seat_i] = None

    def getSeats(self):
        return self.__seats.copy()
    
    def __str__(self):
        seats_str = []
        for seat in self.__seats:
            if seat is None:
                seats_str.append("-")
            else:
                seats_str.append(str(seat))
        return "[" + " ".join(seats_str) + "]"

def main():
    theater = Theater(0)
    while True:

        line = input()
        print("$" + line)
        args = line.split(" ")
        if args[0] == "end":
            break
        if args[0] == "show":
            print(theater)
        if args[0] == "init":
            capacity = int(args[1])
            theater = Theater(capacity)
        if args[0] == "reserve":
            id = args[1]
            phone = int(args[2])
            index = int(args[3])
            theater.reserve(id, phone, index)
        if args[0] == "cancel":
            id = args[1]
            theater.cancel(id)

    
main()