s = "12:59:45PM"
print(s[:2])

H = s[:2]
if s[-2:] == "PM":
    H = str(int(s[:2]) + 12) if s[:2] != "12" else "12"
elif s[-2:] == "AM" and s[:2] == "12":
    H = "00"
time = str(H + s[2:-2])
    
print(time)