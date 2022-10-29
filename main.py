from tkinter import *
import numpy as np
root = Tk()
root.geometry("350x350")
root.title("Get Covid-19 Data Country Wise")

def showdata():
    from matplotlib import pyplot as plt
    from covid import Covid
    covid = Covid()
    cases = []
    confirmed = []
    active = []
    deaths = []
    recovered = []
    try:
        root.update()
        countries = data.get()
        country_names = countries.strip()
        country_names = country_names.replace(" ", ",")
        country_names = country_names.split(",")
        for x in country_names:
            cases.append(covid.get_status_by_country_name(x))
            root.update()
        for y in cases:
            confirmed.append(y["confirmed"])
            active.append(y["active"])
            deaths.append(y["deaths"])
            recovered.append(y["recovered"])

        for a in confirmed:
            pass

        for b in deaths:
            pass
        dataa=np.array([int(a),int(b)])
        labels = ['Confirmed', 'Deaths']
        plt.pie(dataa, labels=labels, shadow=True)
        plt.title('Current Covid Cases')
        plt.show()

    except Exception as e:
        data.set("Enter correct details again")


Label(root, text="Enter all countries names\nfor whom you want to get\ncovid-19 data",font="Consolas 15 bold").pack()
Label(root, text="Enter country name:").pack()
data = StringVar()
data.set("Seperate country names using comma or space(not both)")
entry = Entry(root, textvariable=data, width=50).pack()
Button(root, text="Get Data", command=showdata).pack()
root.mainloop()