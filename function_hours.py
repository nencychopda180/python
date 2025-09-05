def getminutes(hours,minutes):
    total_minutes=hours*60
    total_minutes+=minutes
    hours=0
    minutes=0
    return total_minutes

hours=int(input("enter hours: "))
minutes=int(input("enter minutes: "))

total_minutes=getminutes(hours,minutes)
print(f"total_minutes={total_minutes}")
