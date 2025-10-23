from tkinter import *

root = Tk()
root.title("문제5: 상태 기반 블링크")

canvas = Canvas(root, width=360, height=160, bg="white")
canvas.pack(padx=8, pady=8)
txt = canvas.create_text(180, 80, text="READY", font=("Helvetica", 28, "bold"))

state = "ready"      # "ready" / "running"
toggle = False
after_id = None

def loop():
    global toggle, after_id
    toggle = not toggle

    if state == "ready":
        # 빨강/파랑
        canvas.itemconfig(txt, fill="red" if toggle else "blue")
        canvas.itemconfig(txt, text="READY")
    else:
        # 초록/검정
        canvas.itemconfig(txt, fill="green" if toggle else "black")
        canvas.itemconfig(txt, text="RUNNING")

    after_id = root.after(300, loop)

def set_ready():
    global state
    state = "ready"

def set_running():
    global state
    state = "running"

frm = Frame(root)
frm.pack()
Button(frm, text="시작", width=8, command=set_running).pack(side=LEFT, padx=4)
Button(frm, text="중지", width=8, command=set_ready).pack(side=LEFT, padx=4)
Button(frm, text="종료", width=8, command=root.quit).pack(side=LEFT, padx=4)

loop()
root.mainloop()
