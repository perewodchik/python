A = [(1,5), (-3,4), (-7,2), (8,3), (0,0)] #Лист кортежей 
for x,y in A:
	print(x,y)
	
s  = "Hello"
print("ло встречается на позиции",s.find("lo"))
str2 = ("""Мой дядя
самых честных
правил.""")
print(str2)
x = 1234_5678_9012_3456

screening = 'I\'m a student'

print("Буква а количество:", str2.count('а'))

aaa = "AAAAAA"
aaa.replace("AAA","BB")
print("Строчка не изменилась - ", aaa) #не изменится

t = aaa.replace("AAA","BB")
print("Нужно создавать новую!!! -",t)

#Строчку нельзя изменить!!!

print("Обратная индексация в питоне:", s[-1],s[-2], s[-3],s[-4],s[-5])

s1 = s[1:4] #[start : stop : step]
print(s1)

#Срезы применимы к спискам PogChamp

A = [0,1,2,3,4]
B = A[1:4] #Требует большой асимптотики. Аккуратнее!!!0

print(*A[::-1])

line = "abcdefgh"
x = line
line = line[::2] + line[::-2]

A[0:3] = [10,20,30]

#Для списка чисел

summation = sum(A)
m1 = max(A)
m2 = min(A)

#Для строк

fio = input("ФИО:")
stroke_list = fio.split()

Upp = stroke_list[0][0].upper()