# seat_reservation_gui.py
from tkinter import *

reserved_seats = []  # 전역 리스트

def run_gui():
    root = Tk()
    root.title("좌석 예매 프로그램")
    root.geometry("420x260")

    def update_list_label():
        if reserved_seats:
            txt = ", ".join(reserved_seats)
        else:
            txt = "(없음)"
        label_status.config(text=f"예매 현황: {txt}")

    def reserve():
        name = entry_name.get().strip()
        seat = entry_seat.get().strip().upper()

        if not name or not seat:
            label_result.config(
                text="이름과 좌석을 모두 입력하세요.",
                fg="red"
            )
            return

        if seat in reserved_seats:
            label_result.config(
                text=f"좌석 {seat}은(는) 이미 예매되었습니다.",
                fg="red"
            )
        else:
            reserved_seats.append(seat)
            label_result.config(
                text=f"{seat} 좌석 예매 완료!",
                fg="blue"
            )
            update_list_label()

    def cancel():
        seat = entry_seat.get().strip().upper()
        if not seat:
            label_result.config(text="좌석 번호를 입력하세요.", fg="red")
            return

        if seat in reserved_seats:
            reserved_seats.remove(seat)
            label_result.config(
                text=f"{seat} 좌석 예매가 취소되었습니다.",
                fg="green"
            )
            update_list_label()
        else:
            label_result.config(
                text=f"{seat} 좌석은 예매 목록에 없습니다.",
                fg="red"
            )

    Label(root, text="이름").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    entry_name = Entry(root, width=15)
    entry_name.grid(row=0, column=1, padx=10, pady=5)

    Label(root, text="좌석 번호(A1, B3 등)").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    entry_seat = Entry(root, width=15)
    entry_seat.grid(row=1, column=1, padx=10, pady=5)

    btn_reserve = Button(root, text="예매", width=10, command=reserve)
    btn_reserve.grid(row=2, column=0, padx=10, pady=10)

    btn_cancel = Button(root, text="취소", width=10, command=cancel)
    btn_cancel.grid(row=2, column=1, padx=10, pady=10)

    label_result = Label(root, text="결과 메시지가 여기에 표시됩니다.")
    label_result.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    label_status = Label(root, text="예매 현황: (없음)")
    label_status.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    update_list_label()
    root.mainloop()


if __name__ == "__main__":
    run_gui()
