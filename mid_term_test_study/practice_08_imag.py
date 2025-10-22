import tkinter as tk
from PIL import ImageTk, Image
import os

#현재 파이썬 파일이 있는 폴더 기준으로 경로 설정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def update_image():
    global current_index

    #현재 이미지 파일 경로 생성 (폴더 경로+파일명)-> 폴더 안에 사진이 저장되어있어 따로 사용 안함
    #image_path=image_files[current_index]
    image_path=os.path.join(BASE_DIR, image_files[current_index])
    
    #이미지 열시
    image=Image.open(image_path)
    #크지 조정
    image=image.resize((400,300))
    #객체로 변환
    photo=ImageTk.PhotoImage(image)
    #Label 위젯에 이미지 표시
    image_label.config(image=photo)
    image_label.image=photo

    #다음 이미지 인덱스로 이동 (마지막이면 0으로 돌아감)
    current_index=(current_index+1)%len(image_files)
    #일정 시간이 지나면 다시 update_image 실행 
    root.after(interval, update_image)


root=tk.Tk()
root.title("Image Slider")

image_files=["image1.jpg","image2.jpg","image3.jpg","image4.jpg"] 

interval=2000 #2초
current_index=0

image_label=tk.Label(root)
image_label.pack()

update_image()

root.mainloop()