start = 1800
end = 2024
while(start<=end):
    if (start%100==0 and start%400==0) or (start%100!=0 and start%4==0):
        print(start)
    start = start+1