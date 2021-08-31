import click
import datetime
import json
from rich.console import Console
from rich.table import Table
from rich.table import Column

console = Console()

defaultData = {
  "lunes": {
    "clases": [],
    "hora": [],
    "link": []
  },
  "martes": {
    "clases": [],
    "hora": [],
    "link": []
  },
  "miercoles": {
    "clases": [],
    "hora": [],
    "link": []
  },
  "jueves": {
    "clases": [],
    "hora": [],
    "link": []
  },
  "viernes": {
    "clases": [],
    "hora": [],
    "link": []
  }
}

# Day variables
MONDAY = ['monday','lunes',"0","mon","lun"]
TUESDAY = ['thuesday','martes',"1","tue","mar"]
WEDNESDAY = ['wednesday','miercoles',"2","wed","mie"]
THURSDAY = ['thursday','jueves',"3","thu","jue"]
FRIDAY = ['friday','viernes',"4","fri","vie"]

class newClass:
    def __init__(self):
        self.day = console.input("[green]Ingresa el dia \n=> ")
        self.name = console.input("[green]Ingresa el nombre de la clase \n=> ")
        self.inicio = int(console.input("[green]Ingresa la hora de inicio de la clase [yellow r][Solo numeros]"
                                        "[/yellow r]\n=> "))
        self.final = int(console.input("[green]Ingresa la hora de terminar de la clase [yellow r][Solo numeros]"
                                       "[/yellow r]\n=> "))
        self.link = console.input("[blue]Ingresa el link de la clase [r][Dejar en blanco si no hay link][/r]"
                                  "\n=> ")

    def printInfo(self):
        print("Informacion de la clase")
        print(f"Clase => {self.name}")
        print(f"Hora => {self.inicio} - {self.final}")
        print(f"Link => {self.link}")

def translateDay(day):
    # return days to the sintax in data.json
    day = day.lower()
    if day in MONDAY:
        return "lunes"
    elif day in TUESDAY:
        return "martes"
    elif day in WEDNESDAY:
        return "miercoles"
    elif day in THURSDAY:
        return "jueves"
    elif day in FRIDAY:
        return "viernes"
    else:
        return False

def writeCalendar():
    day = input("Que dia se modificara? => ")
    day = translateDay(day)
    if day == "all":
        console.print("ALL",style="reverse blink ##ff0522",justify="center")
    else:
        writePerDay(day)
        print("A salido del menu")

def writePerDay(day):
    # Inicializando calendario
    calendar = open("data.json")
    dataCalendar = json.load(calendar)
    perDay(day)

    # Obteniendo array de clases y horas
    clases = dataCalendar[day]["clases"]
    horas = dataCalendar[day]["hora"]

    # Menu
    option = ""
    while option.lower() != 'e':
        option = input("A - Agregar clase\nR - Remover clase\nE - Salir del menu\n[+]=> ")
        if option.lower() == 'a':
            newClase = input("Ingresa el nombre de la clase [+]=> ")
            newHora = []
            # Ingreso de hora
            newHora.append(input("Ingresa la hora de inicio (24 horas) [+]=> "))
            newHora.append(input("Ingresa la hora de salida (24 horas) [+]=> "))
            newLink = input("Ingresa el link de la clase [+]=> ")
            # Escribiendo en el horario
            dataCalendar[day]["clases"].append(newClase)
            dataCalendar[day]["hora"].append(newHora)
            dataCalendar[day]["link"].append(newLink)

            with open("data.json", "w", encoding='utf-8') as f:
                json.dump(dataCalendar, f, ensure_ascii=False, indent=4)
            # Mostrando calendario actualizado
            perDay(day)
        elif option.lower() == 'r':
            print("Removida la clase")
        elif option.lower() != 'e':
            print("Porfavor ingresa un comando valido [A, R, E]")

def perDay(day):
    # Data
    calendar = open("data.json")
    dataCalendar = json.load(calendar)

    # Setting table
    table = Table(
        "Hora",
        Column(header="Clase",style="",justify="center"),
        "Link",
        show_header=True, header_style="bold magenta")

    # Adding rows
    for i in range(len(dataCalendar[day]["clases"])):
        clase = dataCalendar[day]["clases"][i]
        hora = "-".join(str(x) for x in dataCalendar[day]["hora"][i])
        link = dataCalendar["lunes"]["link"][i]
        table.add_row(hora, clase, link)

    console.print(table,justify="center")

def deleteClass(day, name):
    index = 0
    with open("data.json", "r", encoding='utf-8') as f:
        data = json.load(f)
        array = data[day]["clases"]
        index = array.index(name)
        data[day]["clases"].pop(index)
        data[day]["hora"].pop(index)
        data[day]["link"].pop(index)
    return index

@click.group()
def horario():
    pass

@horario.command()
def write():
    """
    Permite registrar una nueva clase
    """
    c = newClass()
    if translateDay(c.day):
        console.print("Dia valido",style="green",justify="center")

        # Iniciando calendario
        calendar = open("data.json")
        dataCalendar = json.load(calendar)
        day = dataCalendar[c.day]
        day["clases"].append(c.name)
        day["hora"].append([c.inicio, c.final])
        day["link"].append(c.link)

        if len(set(day["clases"])) != len(day["clases"]):
            while True:
                option = input("Hay un duplicado de clase: Desea sobreescribirlo? [S] si [N] no\n=> ")
                if option.lower() in ['s','n']:
                    break
            if option == 's':
                deleteClass(c.day, c.name)
        else:
            with open("data.json", "w", encoding='utf-8') as f:
                json.dump(dataCalendar, f, ensure_ascii=False, indent=4)

            perDay(c.day)



@horario.command()
def fix():
    """
    Deja el calendario en su modo default (vacio)
    """
    with open("data.json", "w") as outfile:
        json.dump(defaultData,outfile,ensure_ascii=False,indent=4)

@horario.command()
@click.option('--day', '-d', default="today", help="Elige que dia mostrar")
def show(day):
    """
    Muestra el calendario del dia de hoy
    """
    if day == "today":
        console.print("TODAY", style="red on white", justify="center")
        day = translateDay(str(datetime.datetime.today().weekday()))
        perDay(day)
    else:
        day = translateDay(day)
        perDay(day)

if __name__ == '__main__':
    horario()