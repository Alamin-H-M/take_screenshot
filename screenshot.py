import pyautogui, tkinter as tk 

root = tk.Tk()
root.geometry("300x300")
root.title("SS Taker")

def take_ss():
    image = pyautogui.screenshot("capture.png")

def quit():
    root.destroy()

button_1 = tk.Button(root, text="capture", command= take_ss)
button_1.place(50,50)

button_2 = tk.Button(root, text="quit", command= quit)
button_1.place(100,100)

root.mainloop()
