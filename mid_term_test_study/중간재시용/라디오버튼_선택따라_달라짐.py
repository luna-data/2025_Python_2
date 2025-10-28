from tkinter import *
from tkinter import ttk

root = Tk()
root.title("중간고사 고급-GUI")
root.geometry("500x420")

# --------------------
# 상태 변수
# --------------------
shape_var = IntVar(value=1)       # 1=사각형, 2=원, 3=텍스트
fill_var  = BooleanVar(value=False)
grad_var  = BooleanVar(value=False)
color_var = StringVar(value="black")

# --------------------
# 유틸: 색 보간 (left->right 0~1)
# --------------------
RGB = {
    "black": (0, 0, 0),
    "red":   (255, 0, 0),
    "green": (0, 128, 0),
    "blue":  (0, 0, 255),
}
def lerp(a, b, t):
    return int(a + (b - a) * t)

def lerp_color(name, t, base="white"):
    br, bg, bb = (255, 255, 255) if base == "white" else RGB.get(base, (0,0,0))
    tr, tg, tb = RGB.get(name, (0,0,0))
    r = lerp(br, tr, t); g = lerp(bg, tg, t); b = lerp(bb, tb, t)
    return f"#{r:02x}{g:02x}{b:02x}"

# --------------------
# 위젯 배치 (grid만 사용)
# --------------------
# 0행: 라디오 3개 + 체크 2개 + 컬러 콤보
rb1 = Radiobutton(root, text="사각형", variable=shape_var, value=1)
rb2 = Radiobutton(root, text="원",     variable=shape_var, value=2)
rb3 = Radiobutton(root, text="텍스트", variable=shape_var, value=3)
cb_fill = Checkbutton(root, text="fill", variable=fill_var)
cb_grad = Checkbutton(root, text="grad", variable=grad_var)

Label(root, text="color:").grid(row=0, column=5, padx=4, pady=6, sticky="e")
color_cb = ttk.Combobox(root, textvariable=color_var, values=["red","green","blue","black"], state="readonly", width=8)

rb1.grid(row=0, column=0, padx=6, pady=6, sticky="w")
rb2.grid(row=0, column=1, padx=6, pady=6, sticky="w")
rb3.grid(row=0, column=2, padx=6, pady=6, sticky="w")
cb_fill.grid(row=0, column=3, padx=6, pady=6, sticky="w")
cb_grad.grid(row=0, column=4, padx=6, pady=6, sticky="w")
color_cb.grid(row=0, column=6, padx=6, pady=6, sticky="w")

# 1행: (x, y, size) 라벨/엔트리
Label(root, text="x:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
Label(root, text="y:").grid(row=1, column=2, padx=5, pady=5, sticky="e")
Label(root, text="size:").grid(row=1, column=4, padx=5, pady=5, sticky="e")

entry_x = Entry(root, width=8)
entry_y = Entry(root, width=8)
entry_size = Entry(root, width=8)

entry_x.grid(row=1, column=1, padx=5, pady=5, sticky="w")
entry_y.grid(row=1, column=3, padx=5, pady=5, sticky="w")
entry_size.grid(row=1, column=5, padx=5, pady=5, sticky="w")

# 2행: 그리기 버튼
def parse_int(e):
    try:
        v = int(e.get())
        if v < 0:
            raise ValueError
        return v
    except:
        return None

status = Label(root, text="", fg="blue")
def draw():
    # 유효성 검증
    x = parse_int(entry_x); y = parse_int(entry_y); size = parse_int(entry_size)
    if x is None or y is None or size is None:
        status.config(text="오류: x, y, size는 0 이상의 정수여야 합니다.", fg="red")
        return

    canvas.delete("all")
    col = color_var.get()
    mode = shape_var.get()
    do_fill = fill_var.get()
    do_grad = grad_var.get()

    # 사각형
    if mode == 1:
        x0, y0 = x, y
        x1, y1 = x + size, y + size
        if do_fill:
            if do_grad:
                steps = 20
                for i in range(steps):
                    t0 = i / steps
                    t1 = (i + 1) / steps
                    xi0 = int(x0 + (x1 - x0) * t0)
                    xi1 = int(x0 + (x1 - x0) * t1)
                    canvas.create_rectangle(xi0, y0, xi1, y1,
                                            outline="", fill=lerp_color(col, t0))
            else:
                canvas.create_rectangle(x0, y0, x1, y1, outline=col, fill=col)
        else:
            canvas.create_rectangle(x0, y0, x1, y1, outline=col, fill="")

    # 원 (중심 (x,y), 반지름 size//2)
    elif mode == 2:
        r = max(1, size // 2)
        x0, y0 = x - r, y - r
        x1, y1 = x + r, y + r
        if do_fill:
            if do_grad:
                # 좌->우 그라디언트 흉내: 왼쪽에서 오른쪽으로 bbox를 조금씩 줄이며 채우기
                steps = 24
                for i in range(steps):
                    t = i / (steps - 1)
                    xi0 = int(x0 + (x1 - x0) * (t * 0.9))  # 살짝 오른쪽으로 이동
                    canvas.create_oval(xi0, y0, x1, y1, outline="",
                                       fill=lerp_color(col, t))
            else:
                canvas.create_oval(x0, y0, x1, y1, outline=col, fill=col)
        else:
            canvas.create_oval(x0, y0, x1, y1, outline=col, fill="")

    # 텍스트
    else:
        font_size = max(10, size)
        canvas.create_text(x, y, text="Hello Duksung",
                           fill=col, font=("Arial", font_size, "bold"), anchor="nw")

    status.config(text=f"그리기 완료: mode={['사각형','원','텍스트'][mode-1]}, color={col}, "
                       f"fill={'ON' if do_fill else 'OFF'}, grad={'ON' if do_grad else 'OFF'}",
                  fg="blue")

btn = Button(root, text="그리기", command=draw)
btn.grid(row=2, column=0, columnspan=7, pady=6)

# 3행~: 캔버스, 마지막 행 상태라벨
canvas = Canvas(root, width=400, height=250, bg="white", highlightthickness=1, highlightbackground="#ccc")
canvas.grid(row=3, column=0, columnspan=7, padx=10, pady=8)

status.grid(row=4, column=0, columnspan=7, sticky="w", padx=10, pady=(0,6))

# 보너스: 마우스 좌표 실시간 표시
def on_move(e):
    status.config(text=f"마우스: ({e.x}, {e.y})", fg="gray")
canvas.bind("<Motion>", on_move)

root.mainloop()
