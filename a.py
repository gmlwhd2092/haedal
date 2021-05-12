class soccer:
    soccer_count = 0

    def __init__(self, name, position, club, country):
        self.name = name
        self.position = position
        self.club = club
        self.country = country
        soccer.soccer_count += 1


    def info(self):
        print(f'축구선수: {self.name}')
        print(f'포지션: {self.position}')
        print(f'소속팀: {self.club}')
        print(f'국가: {self.country}')
        print()


soccer1 = soccer("호날두", "공격수", "유벤투스", "포르투칼")
soccer2 = soccer("메시", "미드필더", "바르셀로나", "아르헨티나")
soccer3 = soccer("반다이크", "수비수", "리버풀", "네덜란드")

soccer1.info()
soccer2.info()
soccer3.info()
