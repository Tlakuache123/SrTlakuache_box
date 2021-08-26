import click
from rich.console import Console
from rich.table import Table
from rich.table import Column
console = Console()

# Day variables
MONDAY = ['monday','lunes']
TUESDAY = ['thuesday','martes']
WEDNESDAY = ['wednesday','miercoles']
THURSDAY = ['thursday','jueves']
FRIDAY = ['friday','viernes']

@click.command()
@click.option('-d','--day',prompt='Ingresa un dia de la semana [nombre completo]')
def perDay(day):
    table = Table(
        "Hora",
        Column(header="Clase",style="",justify="center"),
        "Link",
        show_header=True, header_style="bold magenta")
    if day.lower() in MONDAY + WEDNESDAY:
        table.add_row("7-9", "Estadistica", "https://cuaieed-unam.zoom.us/j/88376164522")
        table.add_row("9-11", "Optimizacion",
                      "https://cuaieed-unam.zoom.us/j/3392322861?pwd=RVBRZnJMOFI2cm5SL3RyQXZvTzJndz09")
        table.add_row("1-3", "Ingles", "https://cuaed-unam.zoom.us/j/9269646133?pwd=bjJlNHRFaHFWeEFtTUhSelNkSHFjdz09")
    elif day.lower() in TUESDAY + THURSDAY:
        table.add_row("7-9", "Ing. Software",
                      "https://us04web.zoom.us/j/79177939762?pwd=bE5Fd3ZjQnlVaTc1WDBLbXN3QWJxUT09")
        table.add_row("9-11", "Seminario",
                      "ID de la reunión: 854 0392 6657")
        table.add_row("11-1", "Ecua. Diferenciales", "https://cuaieed-unam.zoom.us/j/87126857388")
    elif day.lower() in FRIDAY:
        table.add_row("7-9", "Estadistica", "https://cuaieed-unam.zoom.us/j/88376164522")
        table.add_row("9-11", "Optimizacion",
                      "https://cuaieed-unam.zoom.us/j/3392322861?pwd=RVBRZnJMOFI2cm5SL3RyQXZvTzJndz09")
    console.print(table,justify="center")

if __name__ == '__main__':
    perDay()