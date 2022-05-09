'''
9-12 퀴즈
Quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.

(출력 예제)
총 3대의 매물이 있습니다.
강남 아파트 매매 10억 2010년
마포 오피스텔 전세 5억 2007년
송파 빌라 월세 500/50 2000년
'''

class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
    
    # 매물 정보 표시
    def show_detail(self):
        print(f"{self.location} {self.house_type} {self.deal_type} {self.price} {self.completion_year}")

gangnam_apt = House("강남", "아파트", "매매", "10억", "2010년")
mapo_office = House("마포", "오피스텔", "전세", "5억", "2007년")
songpa_villa = House("송파", "빌라", "월세", "500/50", "2000년")

매물 = []
매물.append(gangnam_apt)
매물.append(mapo_office)
매물.append(songpa_villa)

print("총 {}대의 매물이 있습니다.".format(len(매물)))
for 집 in 매물:
    집.show_detail()