# 치킨 쿠폰
def solution(chicken):
    answer = 0
    while chicken >= 10:
        add_coupon = chicken // 10
        chicken %= 10
        chicken += add_coupon
        answer += add_coupon
    return answer