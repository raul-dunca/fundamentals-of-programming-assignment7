nr_1="5"
nr_2="5"
ok=True

f = open("settings.properties", "rt")


from Ui.ui import UI


for line in f.readlines():
        name,rest = line.split(maxsplit=1, sep='=')
        if name=="grid":
            try:
                nr_1,nr_2=rest.split(maxsplit=1,sep="X")
            except ValueError as ve:
                pass
        elif name=="first":
            if(rest=="yes"):
                ok=True
            elif rest=="no":
                ok=False


try:
    if int(nr_1) <= 1 or int(nr_2) <= 1:
        print("Height and width must be > 1, so the grid will get the basic value: 5X5")
        ui= UI(5, 5,ok)
        ui.start()
    else:
        w=int(nr_1)
        h=int(nr_2)
        ui = UI(w, h,ok)
        ui.start()
except ValueError as ve:
    print(ve)
