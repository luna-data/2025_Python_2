from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# =========================
# 도형 그리기 함수
# =========================
def rectang():
    canvas.delete("all")
    canvas.create_rectangle(50, 50, 150, 150, fill="red") 

def one():
    canvas.delete("all")
    canvas.create_oval(200, 80, 300, 180, fill="blue")

# =========================
# 사진 열기 기능
# =========================
def open_photo():
    global img

    file_path = filedialog.askopenfilename(
        title="사진 파일 선택",
        filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")]
    )

    if not file_path:
        return  # 취소하면 종료

    # Canvas 초기화
    canvas.delete("all")

    # 이미지 로딩
    pil_img = Image.open(file_path)
    img = ImageTk.PhotoImage(pil_img)

    # 이미지 캔버스에 표시
    canvas.create_image(10, 10, anchor=NW, image=img)

    # =========================
    # 이미지 속성 표시
    # =========================
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path) // 1024  # KB 단위
    width, height = pil_img.size

    info_msg = f"파일명: {file_name}\n해상도: {width} x {height}\n파일 크기: {file_size} KB"
    info_label.config(text=info_msg)


# =========================
# 캔버스 지우기
# =========================
def clean():
    canvas.delete("all")
    info_label.config(text="도형 또는 사진을 선택하세요.")

# =========================
# 메인 윈도우 구성
# =========================
root = Tk()
root.title("중간고사 7번 - 사진/도형 그리기")
root.geometry("430x500")

canvas = Canvas(root, width=400, height=320, bg="white")
canvas.pack()

frame = Frame(root)
frame.pack(pady=10)

Button(frame, text="사각형", width=10, command=rectang).pack(side="left", padx=10)
Button(frame, text="원", width=10, command=one).pack(side="left", padx=10)
Button(frame, text="사진 열기", width=10, command=open_photo).pack(side="left", padx=10)
Button(frame, text="지우기", width=10, command=clean).pack(side="left", padx=10)

info_label = Label(root, text="도형 또는 사진을 선택하세요.", fg="black")
info_label.pack(pady=10)

root.mainloop()
