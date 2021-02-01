Waifus = [ 
    "Rem",
    "Nekomata Okayu",
    "Inugami Korone",
    "Sakura Miko",
    "Gwar Gura",
    "Erina Nakiri",
    "Aida Riko",
    "Mako Reizi",
    "Kay",
    "Izumo Kamiki",
    "Frenda"
]

Waifus2 = [ 
    "Rem",
    "Nekomata Okayu",
    "Inugami Korone",
    "Sakura Miko",
    "Gwar Gura",
    "Erina Nakiri",
    "Aida Riko",
    "Mako Reizi",
    "Kay",
    "Izumo Kamiki",
    "Frenda"
]

import random

dag = 0
dagar = ["Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag", "Lördag", "Söndag"]

print ("Any doubles are intentional for the best experience\n")

for i in range(0,7):
    Waifuval = random.randint(0, len(Waifus)-1)
    Waifuval2 = random.randint(0, len(Waifus2)-1)
    print (f"--{dagar[dag].capitalize()}--")
    print (f"Dagens 2 Waifus: {Waifus[Waifuval]} and {Waifus2[Waifuval2]}\n")
    dag += 1