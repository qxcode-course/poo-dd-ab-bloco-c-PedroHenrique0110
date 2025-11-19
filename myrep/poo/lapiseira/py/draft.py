class Lead:
    def __init__(self, thickness: float, hardness: str, size: int):
        self.__thickness = thickness
        self.__hardness = hardness
        self.__size = size

    def usagePerSheet(self) -> float:
        if self.__hardness == "HB":
            return 1
        elif self.__hardness == "2B":
            return 2
        elif self.__hardness == "4B":
            return 4
        elif self.__hardness == "6B":
            return 6
        else:
            return 0

    def getSize(self):
        return self.__size

    def setSize(self, size: float):
        self.__size = size

    def __str__(self):
        return f"[{self.__thickness}:{self.__hardness}:{self.__size}]"

class Pencil:
    def __init__(self, thickness: float):
        self.__thickness = thickness
        self.__bico: list[Lead] = []
        self.__tambor: list[Lead] = []

    def inserir(self, thickness: float, hardness: str, size: int):
        if thickness != self.__thickness:
            print("fail: calibre incompatível")
            return
        self.__tambor.append(Lead(thickness, hardness, size))

    def remover(self):
            if not self.__bico:
                print("fail: nao existe grafite")
                return
            self.__bico.pop()

    def puxar(self):
        if self.__bico:
            print("fail: ja existe grafite no bico")
            return
        if not self.__tambor:
            print("fail: nao existe grafite")
            return
        lead = self.__tambor.pop(0)
        self.__bico.append(lead)

    def escrever(self):
        if not self.__bico:
            print("fail: nao existe grafite no bico")
            return
        lead = self.__bico[0]
        size = lead.getSize()
        if size <= 10:
            print("fail: tamanho insuficiente")
            return
        usage = lead.usagePerSheet()
        
        if size - usage < 10:
            lead.setSize(10)
            print("fail: folha incompleta")
        else:
            lead.setSize(size - usage)


    def __str__(self):
        bico_content = ""
        if self.__bico:
            lead_str = str(self.__bico[0])
            bico_content = lead_str[1:-1]

        tambor_str = ""
        for lead in self.__tambor: 
            tambor_str += str(lead)
        return f"calibre: {self.__thickness}, bico: [{bico_content}], tambor: <{tambor_str}>"

        
def main():
    pencil = Pencil(0)
    while True:
        line = input()
        print("$" + line)
        args = line.split()
        if args[0] == "end":
            break
        if args[0] == "show":
            print(pencil)
        if args[0] == "init":
            thickness = float(args[1])
            pencil = Pencil(thickness)
        if args[0] == "insert":
            thickness = float(args[1])
            hardness = args[2]
            size = int(args[3])
            pencil.inserir(thickness, hardness, size)
        if args[0] == "remove":
            pencil.remover()
        if args[0] == "pull":
            pencil.puxar()
        if args[0] == "write":
            pencil.escrever()


main()
