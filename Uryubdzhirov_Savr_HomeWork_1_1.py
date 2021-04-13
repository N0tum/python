sec_minute = 60
sec_hour = 3600
sec_day = 86400

sec = int(input("Enter duration in seconds: "))
print("duration = ", sec)

days = sec // sec_day
sec = sec - (days * sec_day)

hours = sec // sec_hour
sec = sec - (hours * sec_hour)

minutes = sec // sec_minute
sec = sec - (minutes * sec_minute)

if days > 0:
    print(days, "дн", hours, "час", minutes, "мин", sec, "сек")
elif days > 0 or hours > 0:
    print(hours, "час", minutes, "мин", sec, "сек")
elif days > 0 or hours > 0 or minutes > 0:
    print(minutes, "мин", sec, "сек")
elif days > 0 or hours > 0 or minutes > 0 or sec > 0:
    print(sec, "сек")
