# pet_simulator.py
from tkinter import *
from tkinter import ttk, messagebox

# ========== 클래스 ==========
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return "..."

    def info(self):
        return f"이름: {self.name}, 나이: {self.age}살, 종류: Pet"


class Dog(Pet):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        return "멍멍!"

    def info(self):
        return f"[Dog] 이름: {self.name}, 나이: {self.age}살, 품종: {self.breed}"


class Cat(Pet):
    def __init__(self, name, age, indoor):
        super().__init__(name, age)
        self.indoor = indoor

    def speak(self):
        return "야옹!"

    def info(self):
        t = "실내" if self.indoor else "실외"
        return f"[Cat] 이름: {self.name}, 나이: {self.age}살, 유형: {t} 고양이"


class Bird(Pet):
    def __init__(self, name, age, can_fly):
        super().__init__(name, age)
        self.can_fly = can_fly

    def speak(self):
        return "짹짹!"

    def info(self):
        t = "날 수 있음" if self.can_fly else "날 수 없음"
        return f"[Bird] 이름: {self.name}, 나이: {self.age}살, 상태: {t}"


class Person:
    def __init__(self, name):
        self.name = name
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(pet)

    def remove_pet(self, pet_name):
        for p in self.pets:
            if p.name == pet_name:
                self.pets.remove(p)
                return True
        return False

    def list_pets(self):
        return [p.info() for p in self.pets]

    def speak_with_pets(self):
        sounds = [p.speak() for p in self.pets]
        return f"{self.name}의 반려동물 소리: " + ", ".join(sounds) if sounds else "반려동물이 없습니다."


# ========== 파일 입출력 ==========
def export_pets_to_file(pets, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for p in pets:
            if isinstance(p, Dog):
                line = f"Dog,{p.name},{p.age},{p.breed}\n"
            elif isinstance(p, Cat):
                line = f"Cat,{p.name},{p.age},{int(p.indoor)}\n"
            elif isinstance(p, Bird):
                line = f"Bird,{p.name},{p.age},{int(p.can_fly)}\n"
            else:
                line = f"Pet,{p.name},{p.age},0\n"
            f.write(line)


def import_pets_from_file(filename):
    pets = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                t, name, age, extra = line.split(",")
                age = int(age)
                if t == "Dog":
                    pets.append(Dog(name, age, extra))
                elif t == "Cat":
                    pets.append(Cat(name, age, bool(int(extra))))
                elif t == "Bird":
                    pets.append(Bird(name, age, bool(int(extra))))
                else:
                    pets.append(Pet(name, age))
    except FileNotFoundError:
        pass
    return pets


# ========== GUI ==========
def main():
    root = Tk()
    root.title("반려동물 상호작용 시뮬레이터")
    root.geometry("780x420")

    person = Person("이름없음")

    # 상단 - 사람 정보
    frame_top = Frame(root, padx=10, pady=10)
    frame_top.pack(fill="x")

    Label(frame_top, text="사람 이름").pack(side="left")
    entry_person = Entry(frame_top, width=15)
    entry_person.pack(side="left", padx=5)
    entry_person.insert(0, "홍길동")

    label_person = Label(frame_top, text="현재 사람: 홍길동")
    label_person.pack(side="left", padx=10)

    def set_person():
        name = entry_person.get().strip() or "이름없음"
        person.name = name
        label_person.config(text=f"현재 사람: {name}")
        update_status("사람 정보가 변경되었습니다.")

    Button(frame_top, text="사람 생성/변경", command=set_person).pack(side="left", padx=5)

    # 중간 - 왼쪽: Pet 등록
    frame_mid = Frame(root)
    frame_mid.pack(fill="both", expand=True)

    frame_left = Frame(frame_mid, padx=10, pady=10)
    frame_left.pack(side="left", fill="y")

    Label(frame_left, text="반려동물 타입").grid(row=0, column=0, sticky="w")
    pet_type_var = StringVar(value="Dog")
    combo_pet = ttk.Combobox(frame_left, textvariable=pet_type_var,
                             values=["Dog", "Cat", "Bird"], state="readonly", width=10)
    combo_pet.grid(row=0, column=1, pady=5)

    Label(frame_left, text="이름").grid(row=1, column=0, sticky="e")
    entry_pet_name = Entry(frame_left, width=12)
    entry_pet_name.grid(row=1, column=1, pady=3)

    Label(frame_left, text="나이").grid(row=2, column=0, sticky="e")
    entry_pet_age = Entry(frame_left, width=12)
    entry_pet_age.grid(row=2, column=1, pady=3)
    entry_pet_age.insert(0, "1")

    # 타입별 추가 옵션
    Label(frame_left, text="품종(Dog)").grid(row=3, column=0, sticky="e")
    entry_breed = Entry(frame_left, width=12)
    entry_breed.grid(row=3, column=1, pady=3)

    indoor_var = BooleanVar()
    check_indoor = Checkbutton(frame_left, text="실내 고양이", variable=indoor_var)
    check_indoor.grid(row=4, column=0, columnspan=2, sticky="w")

    canfly_var = BooleanVar()
    check_canfly = Checkbutton(frame_left, text="날 수 있음(Bird)", variable=canfly_var)
    check_canfly.grid(row=5, column=0, columnspan=2, sticky="w")

    # 오른쪽 - 목록 & 상호작용
    frame_right = Frame(frame_mid, padx=10, pady=10)
    frame_right.pack(side="left", fill="both", expand=True)

    Label(frame_right, text="반려동물 목록").pack(anchor="w")
    listbox = Listbox(frame_right, width=40, height=15)
    listbox.pack(fill="both", expand=True)

    text_info = Text(frame_right, height=8)
    text_info.pack(fill="x", pady=5)

    status_label = Label(root, text="상태 메시지")
    status_label.pack(fill="x", pady=3)

    def update_status(msg):
        status_label.config(text=msg)

    def refresh_listbox():
        listbox.delete(0, END)
        for p in person.pets:
            listbox.insert(END, f"{type(p).__name__} - {p.name} ({p.age}살)")

    def add_pet():
        ptype = pet_type_var.get()
        name = entry_pet_name.get().strip() or "이름없음"
        try:
            age = int(entry_pet_age.get())
        except ValueError:
            messagebox.showerror("입력 오류", "나이는 정수로 입력하세요.")
            return

        if ptype == "Dog":
            breed = entry_breed.get().strip() or "알 수 없음"
            pet = Dog(name, age, breed)
        elif ptype == "Cat":
            pet = Cat(name, age, indoor_var.get())
        elif ptype == "Bird":
            pet = Bird(name, age, canfly_var.get())
        else:
            pet = Pet(name, age)

        person.add_pet(pet)
        refresh_listbox()
        update_status(f"{ptype} '{name}' 추가 완료.")

    def delete_selected():
        sel = listbox.curselection()
        if not sel:
            return
        idx = sel[0]
        pet = person.pets[idx]
        name = pet.name
        person.pets.pop(idx)
        refresh_listbox()
        update_status(f"'{name}' 삭제 완료.")

    def show_all_info():
        text_info.delete("1.0", END)
        for p in person.pets:
            text_info.insert(END, p.info() + "\n")
        if not person.pets:
            text_info.insert(END, "반려동물이 없습니다.\n")

    def speak_all():
        msg = person.speak_with_pets()
        update_status(msg)

    def save_to_file():
        export_pets_to_file(person.pets, "pets_data.txt")
        update_status("pets_data.txt에 저장 완료.")

    def load_from_file():
        pets = import_pets_from_file("pets_data.txt")
        person.pets = pets
        refresh_listbox()
        update_status("pets_data.txt에서 불러오기 완료.")

    Button(frame_left, text="반려동물 추가", width=15, command=add_pet).grid(row=6, column=0, columnspan=2, pady=5)
    Button(frame_left, text="선택 삭제", width=15, command=delete_selected).grid(row=7, column=0, columnspan=2, pady=5)
    Button(frame_left, text="모든 정보 보기", width=15, command=show_all_info).grid(row=8, column=0, columnspan=2, pady=5)
    Button(frame_left, text="모든 소리 듣기", width=15, command=speak_all).grid(row=9, column=0, columnspan=2, pady=5)
    Button(frame_left, text="저장", width=7, command=save_to_file).grid(row=10, column=0, pady=5)
    Button(frame_left, text="불러오기", width=7, command=load_from_file).grid(row=10, column=1, pady=5)

    root.mainloop()


if __name__ == "__main__":
    main()
