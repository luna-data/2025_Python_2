class Post:
    def __init__(self,title,author,content):
        Post.count=0
        self.title=title
        self.author=author
        self.content=content    

    def display_info(self):
        print(f"제목: {self.title}\n작성자: {self.author}\n내용: {self.content}\n")
        Post.count+=1


post1=Post("첫 번째 게시글", "홍길동", "안녕하세요. 첫 번째 게시글입니다.")
post2=Post("두 번째 게시글", "홍길동", "안녕하세요. 두 번째 게시글입니다.")

post1.display_info()
post2.display_info()

print("총 게시글 개수:", Post.count) 