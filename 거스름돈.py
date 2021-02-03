n=int(input('거스름 돈 입력하세요'))
count =0

listnumber =[500, 100, 50, 10]

for coin in listnumber:
    count += n//coin
    n %= coin

print(count)
