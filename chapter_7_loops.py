ls = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]

for i in ls:
	print(i)



for i in range(25, 51):
	print(i)



ls = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
for index, ls in enumerate(ls):
	print(index)
	print(ls



numbers = [69, 420, 666]

while True:
	answer = input("Guess a number or type q to quit:  ")
	if answer == "q":
		break
	try:
		answer = int(answer)
	except ValueError:
		print("not a number. try again or q to quit:  ")
	if answer in numbers:
		print("you guessed it right!")
	else:
		print("try again fool")




list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
list3 = []

for i in list1:
	for j in list2:
		list3.append(i * j)

print(list3)









