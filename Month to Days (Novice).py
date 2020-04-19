mon_31 = ["Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"]
mon_30 = ["Apr", "Jun", "Sep", "Nov"]


def month(d):
    if d in mon_31:
        print("31 days")
    elif d in mon_30:
        print("30 days")
    else:
        print("28 or 29 days")


month(input())