class Kid:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def getAge(self):
        return self.__age
    
    def getName(self):
        return self.__name
    
    def setAge(self, age:int): 
        self.__age = age

    def setName(self, name:str):
        self.__name = name

    def __str__(self):
        return f"{self.__name}:{self.__age}"
    
class Trampoline:
    def __init__(self):
        self.__playing: list[Kid] = []
        self.__waiting: list[Kid] = []

    def removeFromList(self, name:str, lista: list[Kid]) -> Kid | None:
        for i, kid in enumerate(lista):
            if kid.getName() == name:
                return lista.pop(i)
        return None

    def arrive(self, kid: Kid) -> None:
        self.__waiting.append(kid)

    def enter(self):
        if self.__waiting:
            kid = self.__waiting.pop(0)
            self.__playing.append(kid)

    def leave(self):
        if self.__playing:
            kid = self.__playing.pop(0)
            self.__waiting.append(kid)

    def removeKid(self, name: str):
        kid = self.removeFromList(name, self.__playing)
        if kid:
            return kid
        kid = self.removeFromList(name, self.__waiting)
        if kid:
            return kid
        print(f"fail: {name} nao esta no pula-pula")
        return None

    def __str__(self):
        playing_rev = [str(kid) for kid in reversed(self.__playing)]
        waiting_rev = [str(kid) for kid in reversed(self.__waiting)]
        playing_str = ", ".join(playing_rev)
        waiting_str = ", ".join(waiting_rev)
        return f"[{waiting_str}] => [{playing_str}]"


def main():
    trampoline = Trampoline()
    while True:

        line = input()
        print("$" + line)
        args = line.split(" ")
        if args[0] == "end":
            break
        if args[0] == "show":
            print(trampoline)
        if args[0] == "arrive":
            name = args[1]
            age = int(args[2])
            trampoline.arrive(Kid(name, age))
        if args[0] == "enter":
            trampoline.enter()
        if args[0] == "leave":
            trampoline.leave()
        if args[0] == "remove":
            name = args[1]
            trampoline.removeKid(name)
            
main()