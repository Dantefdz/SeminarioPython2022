from consolemenu import *
from consolemenu.items import *
import desafioClase4



# Creating the menu
menu = ConsoleMenu("Seminario de lenguajes", "Python 3.1 - Clase 4")

function_item1 = FunctionItem("ver archivo generado", print(open("nuevo_archivo.txt","r",encoding="utf-8")))

function_item2 = FunctionItem("ver los 5 paises con mas producciones", desafioClase4)

# Once we're done creating them, we just add the items to the menu
menu.append_item(function_item1)
menu.append_item(function_item2)

# Finally, we call show to show the menu and allow the user to interact
menu.show()