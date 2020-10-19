import tkinter as tk
import pyautogui

def catch():
    pyautogui.screenshot(nama.get()) #fungsi mengambil screenshot
    
def reset():
    nama.delete(0, 50) #fungsi mengatur ulang nama file

root = tk.Tk()
root.title('ScreenCatch') #sebagai master 
label = tk.Label(root, text='Masukan Nama File :')
label.grid(row=0, column=1)

tombol1 = tk.Button(root, text='Catch!', width=20, command=catch)
tombol1.grid(row=2, column=1)
tombol2 = tk.Button(root, bg='yellow', text='Reset', width=20, command=reset)
tombol2.grid(row=3, column=1, padx=5, pady=2)

nama = tk.Entry(root, width=25)
nama.grid(row=1, column=1, pady=7)

root.mainloop()

