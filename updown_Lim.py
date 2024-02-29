import random


def updown_game():
    best_score = float('inf')
    play_again = True

    while play_again:
        print("게임을 시작합니다.")
        target_number = random.randint(1, 100)
        playno = 0

        while True:
            try:
                answer = int(input("1부터 100까지의 숫자만 입력하시오. : "))
                if answer < 1 or answer > 100:
                    print("범위에 맞는 숫자를 입력하세요.")
                    continue

                playno += 1

                if answer > target_number:
                    print("Down")
                elif answer < target_number:
                    print("up")
                else:
                    print(f"Hit ! {playno}번 시도했습니다.")
                    if playno < best_score:
                        best_score = playno
                    break

            except ValueError:
                print("범위에 맞는 숫자를 입력하세요")

        play_again_input = input("게임을 다시 하시겠습니까? (yes/no): ")
        play_again = play_again_input.lower() == 'yes'

    print(f"최고 기록: {best_score}번")


updown_game()
