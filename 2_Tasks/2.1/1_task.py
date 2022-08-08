from datetime import timedelta, date

date_c = list(map(int, input().strip().split()))
days = int(input())

results = date(date_c[0], date_c[1], date_c[2]) + timedelta(days=days)

print(results.strftime("%Y %-m %-d"))
