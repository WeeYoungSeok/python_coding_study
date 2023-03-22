# 2007년
x, y = map(int, input().split())

days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

first_x = 1
first_y = 1

day_index = 1

while first_x != x or first_y != y:
    first_y += 1
    day_index += 1
    if day_index >= len(days):
        day_index = 0
    if (first_x == 1 or first_x == 3 or first_x == 5 or first_x == 7 or first_x == 8 or first_x == 10 or first_x == 12) and first_y > 31:
        first_y = 1
        first_x += 1
    elif (first_x == 4 or first_x == 6 or first_x == 9 or first_x == 11) and first_y > 30:
        first_y = 1
        first_x += 1
    elif first_x == 2 and first_y > 28:
        first_y = 1
        first_x += 1
      
print(days[day_index])