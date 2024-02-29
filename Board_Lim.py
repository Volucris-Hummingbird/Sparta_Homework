# ----- 코드 정의 ------
class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    # TODO : 코드 구현이 필요합니다.

    def display(Member):
        print(f"이름은 {Member.name}, ID는 {Member.username}입니다.")
        # # TODO : 코드 구현이 필요합니다.
        # pass


# post class 지정시에 for 문을 작성하기.
class post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    # def __str__(self):
    #     return f"{self.title} {self.content} {self.author}"
        # for self.author in author:
        #     print(self.author)
#     # TODO : 코드 구현이 필요합니다.
#     pass


Members = [
    Member("Alice", "Alice1", 123456),
    Member("Bob", "Bob1", 123456),
    Member("Charlie", "Charlie1", 123456)
]


# for Member in Members:
#     print(f'Name : {Member.name}, Username : {Member.username}')

for Member in Members:
    Member.display()


posts = []
for Member in Members:
    for i in range(3):
        post_title = f'{Member.name} 의 {i+1}번째 게시글 '
        post_contents = f'이 게시글은 파이썬을 배우고자 하는 {i+1}번째 게시글입니다.'
        posts.append(post(post_title, post_contents, Member.username))


marked_user = "Alice1"
# 특정 유저의 아이디를 입력
for post in posts:
    if post.author == marked_user:
        print(post.title)

marked_content = "파이썬"
for post in posts:
    if marked_content in post_contents:
        print(post.content)

# # # ----- 코드 실행 ------
# posts = []

# # # TODO : 코드 구현이 필요합니다.
