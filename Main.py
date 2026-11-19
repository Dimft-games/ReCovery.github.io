from tkinter import *
import subprocess
import ctypes, sys
import psutil

if not ctypes.windll.shell32.IsUserAnAdmin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    sys.exit()

processes = [p.info['name'] for p in psutil.process_iter(['name']) if p.info['name']]

#DEFs

def clrui():
    run(r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Shell /t REG_SZ /d "explorer.exe" /f')
    run(r'reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon" /v Userinit /t REG_SZ /d "C:\Windows\system32\userinit.exe," /f')
def clrar():
    run()
def restart(process):
    run(f"taskkill /f /im {process}")
    run(f"start {process}")
def run(cmd):
    subprocess.run(cmd,shell=True)

def update():
    global processes
    processes = [p.info['name'] for p in psutil.process_iter(['name']) if p.info['name']]
    global proct
    proct.delete(0,END)
    i = 0
    for i in processes:
        proct.insert(END, i)
def destroy():
    if proct.curselection():
      run(f'taskkill /f /im {proct.get(ANCHOR)}')

#ROOT OPTIONS

root = Tk()
root['bg']="#fafafa"
root.title("ReCovery by Dimft")
root.geometry("480x360")

#CANVAS & FRAME

canvas = Canvas(root,width=480,height=360,bg='#fafafa')
canvas.pack()

frame = Frame(canvas,width=480,height=360,bg="#fafafa")
frame.pack()

#ELEMENTS

title = Label(frame, text = "ReCovery", fg="black", font=("Arial",24), bg = '#fafafa')
title.pack()

cmd = Button(frame,text='Run CMD',fg="black", font=("Arial",12), bg = '#fafafa',command=lambda: run('start'))
cmd.pack()

uir = Button(frame,text='Restart Explorer (system UI)',fg="black", font=("Arial",12), bg = '#fafafa',command=lambda: restart('explorer.exe'))
uir.pack()

shellr = Button(frame,text = 'Reset Shell (System UI app on start)',fg="black", font=("Arial",12), bg = '#fafafa',command=lambda: clrui())
shellr.pack()

winro = Button(frame,text = 'Load WinRO (Recovery Menu)',fg="black", font=("Arial",12), bg = '#fafafa',command=lambda: run('shutdown /r /o /t 0'))
winro.pack()

mgrt = Label(frame, text= ' - SIMPLE TASK MANAGER - ', font = ('Arial', 18), fg = 'black', bg = '#fafafa')
mgrt.pack()

proct = Listbox(frame, font = ('Arial', 8))
proct.pack()
update()
procup = Button(frame, text = 'Update processes list', bg = '#fafafa', font = ('Arial', 12), command = lambda: update())
procup.pack()

taskb = Button(frame,text = 'Destroy',fg="black", font=("Arial",12), bg = '#fafafa',command=lambda: destroy())
taskb.pack()

# root mainloop
root.mainloop()