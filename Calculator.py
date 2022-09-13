### CALCULATOR
import tkinter as tk


def write(x):
    s = len(data_entry.get())
    data_entry.insert(s, str(x))
    print(x)

hesap = 6
s1 = 0


def islemler(x):
    global hesap
    hesap = x
    global s1
    s1 = float(data_entry.get())
    print(hesap)
    print(s1)
    data_entry.delete(0, "end")
s2 = 0
def hesapla():
    global s2
    s2 = float(data_entry.get())
    global hesap
    sonuc = 0
    if (hesap == 0): sonuc=s1+s2
    elif (hesap == 1): sonuc=s1-s2
    elif (hesap == 2): sonuc = s1 * s2
    elif (hesap == 3): sonuc = s1 / s2
    data_entry.delete(0,"end")
    data_entry.insert(0,str(sonuc))

window = tk.Tk()
window.title("Calculator")
window.geometry("225x275")

data_entry = tk.Entry(window, font="Verdana 14", width=15, justify="right")
data_entry.place(x=20, y=20)

numbers = []
for i in range(1, 10):
    numbers.append(tk.Button(text=str(i), font="Verdana 14", width=2, command=lambda x=i: (write(x))))
count = 0
numbers.reverse()
for i in range(0, 3):
    for j in range(0, 3):
        numbers[count].place(x=120-j*50, y=75+i*50)
        count += 1

process = []
for i in range(0, 4):
    process.append((tk.Button(text=str(i), font="Verdana 14", width=2, command=lambda x=i: islemler(x))))
process[0]["text"] = "+"
process[1]["text"] = "-"
process[2]["text"] = "/"
process[3]["text"] = "x"
for i in range(0, 4):
    process[i].place(x=170, y=75+i*50)

sb = tk.Button(text="0", font="Verdana 14",width=2, command=lambda x=0:write(x))
sb.place(x=20, y=225)
nb = tk.Button(text=".", font="Verdana 14", width=2, command=lambda x=".": write(x))
nb.place(x=70, y=225)
eb = tk.Button(text="=", font="Verdana 14", bg="pink", command=hesapla)
eb.place(x=120, y=225)

window.mainloop()
