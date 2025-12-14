class Media:
    def __init__(self, title, year):
        self.title = title
        self.year = year
    
    def get_info(self):
        return f"{self.title} ({self.year})"


class Book(Media):  # Book is a Media
    def __init__(self, title, year, author, pages):
        super().__init__(title, year)
        self.author = author
        self.pages = pages


class Movie(Media):  # Movie is a Media
    def __init__(self, title, year, director, duration):
        super().__init__(title, year)
        self.director = director
        self.duration = duration

# Book 객체 생성
b1 = Book("해리 포터와 마법사의 돌", 1997, "J.K. 롤링", 320)

# Movie 객체 생성
m1 = Movie("인터스텔라", 2014, "크리스토퍼 놀란", 169)

# 정보 출력
print(b1.get_info(), "-", b1.author, "/", f"{b1.pages}쪽")
print(m1.get_info(), "-", m1.director, "/", f"{m1.duration}분")