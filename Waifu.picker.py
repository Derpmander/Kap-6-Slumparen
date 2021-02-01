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

import random

dag = 0
dagar = ["Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag", "Lördag", "Söndag"]

#Waifuval = random.randint(0, len(Waifus)-1)

for i in range(0,7):
    Waifuval = random.randint(0, len(Waifus)-1)
    print (f"--{dagar[dag].capitalize()}--")
    print (f"Dagens Waifu: {Waifus[Waifuval]}\n")
    dag += 1