import tkinter
import speedtest


def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download() / (10**6), 3)) + "Mbps"
    up = str(round(sp.upload() / (10**6), 3)) + "Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)


sp = tkinter.Tk()
sp.title("Internet Speed Test")
sp.geometry("500x650")
sp.config(bg="Blue")

lab = tkinter.Label(
    sp,
    text="Internet Speed Test",
    font=("Time New Roman", 30, "bold"),
    bg="blue",
    fg="white",
)
lab.place(x=60, y=40, height=50, width=380)

lab = tkinter.Label(
    sp,
    text="Download Speed",
    font=("Time New Roman", 30, "bold"),
)
lab.place(x=60, y=130, height=50, width=380)

lab_down = tkinter.Label(
    sp,
    text="00",
    font=("Time New Roman", 30, "bold"),
)
lab_down.place(x=60, y=200, height=50, width=380)

lab = tkinter.Label(
    sp,
    text="Upload Speed",
    font=("Time New Roman", 30, "bold"),
)
lab.place(x=60, y=290, height=50, width=380)

lab_up = tkinter.Label(
    sp,
    text="00",
    font=("Time New Roman", 30, "bold"),
)
lab_up.place(x=60, y=360, height=50, width=380)

button = tkinter.Button(
    sp,
    text="Check Speed",
    font=("Time New Roman", 30, "bold"),
    relief=tkinter.RAISED,
    bg="Red",
    command=speedcheck
)
button.place(x=60, y=460, height=50, width=380)


sp.mainloop()
