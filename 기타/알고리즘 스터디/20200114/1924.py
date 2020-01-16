x, y = map(int, input().split())
days = [31,28,31,30,31,30,31,31,30,31,30,31]
day = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
daySum = 0
for i in range(x-1):
    daySum += days[i]
daySum += y-1
print(day[daySum%7])





