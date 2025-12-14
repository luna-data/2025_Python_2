# movie_ticket_gui.py
from tkinter import *

class MovieTicket:
    def __init__(self, title, theater):
        self.title = title
        self.theater = theater
        self.reserved = False

    def reserve(self):
        if not self.reserved:
            self.reserved = True
            return f"{self.title}(이)가 예매되었습니다."
        else:
            return f"{self.title}는 이미 예매된 상태입니다."

    def cancel(self):
        if self.reserved:
            self.reserved = False
            return f"{self.title} 예매가 취소되었습니다."
        else:
            return f"{self.title}는 아직 예매되지 않았습니다."


def run_gui():
    root = Tk()
    root.title("영화 예매 프로그램")
    root.geometry("380x220")

    ticket = None

    def reserve_ticket():
        nonlocal ticket
        title = entry_title.get().strip()
        theater = entry_theater.get().strip()
        if not title:
            title = "제목없음"
        if not theater:
            theater = "상영관 미지정"
        ticket = MovieTicket(title, theater)
        msg = ticket.reserve()
        label_result.config(text=msg)

    def cancel_ticket():
        nonlocal ticket
        title = entry_title.get().strip()
        if not title and ticket is None:
            label_result.config(text="취소할 예매가 없습니다.")
            return
        if ticket is None:
            label_result.config(text=f"{title or '제목없음'} 예매 정보가 없습니다.")
        else:
            msg = ticket.cancel()
            label_result.config(text=msg)

    Label(root, text="영화 제목").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    entry_title = Entry(root, width=20)
    entry_title.grid(row=0, column=1, padx=10, pady=5)

    Label(root, text="상영관").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    entry_theater = Entry(root, width=20)
    entry_theater.grid(row=1, column=1, padx=10, pady=5)

    btn_reserve = Button(root, text="예매", command=reserve_ticket)
    btn_reserve.grid(row=2, column=0, padx=10, pady=10)

    btn_cancel = Button(root, text="취소", command=cancel_ticket)
    btn_cancel.grid(row=2, column=1, padx=10, pady=10)

    label_result = Label(root, text="결과가 여기에 표시됩니다.")
    label_result.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    root.mainloop()


if __name__ == "__main__":
    run_gui()
