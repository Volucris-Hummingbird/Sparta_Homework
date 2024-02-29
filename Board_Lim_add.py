import hashlib
# import secrets

# ----- 코드 정의 ------


class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = self._encrypt_password(password)

    def _encrypt_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def display(self):
        print(f"이름은 {self.name}, ID는 {self.username}입니다.")
        # # TODO : 코드 구현이 필요합니다.
        # pass


# post class 지정시에 for 문을 작성하기.
class post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author


Members = []
posts = []


#  회원가입 기능과 같이 일정 기능을 수행하기 위해서는 '함수'를 만들어야 한다.
#  더불어 input 기능에 대해서 숙지, 숙달해야한다.

def create_member():
    name = input("이름을 입력하세요 : ")
    username = input("아이디를 입력하세요 : ")
    password = input("비밀번호를 입력하세요 : ")
    Members.append(Member(name, username, password))


def create_post():
    if not Members:
        print("회원가입을 하셔야 게시글 작성이 가능합니다.")
        return
    author_username = input("게시글을 작성하기 위한 아이디를 입력해주세요 : ")
    for Member in Members:
        if Member.username == author_username:
            title = input("글 제목을 입력하세요 : ")
            contents = input("내용을 입력하세요 : ")
            posts.append(post(title, contents, author_username))
            print("글이 게시되었습니다.")
            return
    print("회원가입을 하셔야 게시글 작성이 가능합니다.")


#  While true: 문에 대해서 숙달이 필요
while True:
    create_member_option = input("회원가입 하시겠습니까? (yes/no) : ")
    if create_member_option.lower() == 'yes':
        create_member()
    else:
        break

while True:
    create_post_option = input("게시글을 기재하겠습니까? (yes/no) : ")
    if create_post_option.lower() == 'yes':
        create_post()
    else:
        break

for Member in Members:
    print(Member.username)


for post in posts:
    if post.author == "Alice1":
        print(post.title)


for post in posts:
    if '파이썬' in post.content:
        print(post.title)

# marked_user = "Alice1"
# # 특정 유저의 아이디를 입력
# for post in posts:
#     if post.author == marked_user:
#         print(post.title)

# marked_content = "파이썬"
# for post in posts:
#     if marked_content in post_contents:
#         print(post.content)


# # # # ----- 코드 실행 ------
# # posts = []

# # # # TODO : 코드 구현이 필요합니다.
