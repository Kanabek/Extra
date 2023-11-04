l = int(input('Enter number of lessons: '))
t = l*45 + (l // 2) * 5 + ((l + 1) // 2 - 1) * 15
h = int(t / 60) + 9
m = int(t % 60)
print(h, m)