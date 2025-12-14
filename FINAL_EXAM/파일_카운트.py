# file_stats_gui.py
from tkinter import *
from tkinter import filedialog, messagebox

def count_stats_digits_alpha(filename):
    digit_cnt = 0
    alpha_cnt = 0
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            for ch in line:
                if ch.isdigit():
                    digit_cnt += 1
                if ch.isalpha():
                    alpha_cnt += 1
    return digit_cnt, alpha_cnt


def run_gui():
    root = Tk()
    root.title("문자 개수 세기")
    root.geometry("520x200")

    def select_file():
        path = filedialog.askopenfilename(
            title="텍스트 파일 선택",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not path:
            return
        label_file.config(text=f"선택된 파일: {path}")

        try:
            digits, alphas = count_stats_digits_alpha(path)
            label_result.config(
                text=f"숫자: {digits}개, 알파벳: {alphas}개"
            )
        except Exception as e:
            messagebox.showerror("에러", f"파일 처리 중 오류가 발생했습니다.\n{e}")

    btn = Button(root, text="파일 선택", command=select_file)
    btn.pack(pady=10)

    label_file = Label(root, text="선택된 파일: (없음)")
    label_file.pack(pady=5)

    label_result = Label(root, text="숫자와 알파벳 개수가 여기에 표시됩니다.")
    label_result.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    run_gui()
