'''
11-2 패키지
패키지 : 모듈의 집합
'''

# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

from travel import *
trip_to = thailand.ThailandPackage()
trip_to.detail()