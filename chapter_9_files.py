"""challenge 2"""
userinput = input("type in some text: ")

with open("chapter_9_files.txt", "w") as f:
	f.write(userinput)



"""challenge 3"""
import csv

with open("chapter_9_files.csv", "w", newline='') as f:
	w = csv.writer(f, delimiter=",")
	w.writerow(["Top Gun", "Risky Business", "Minority Report"])
	w.writerow(["Titanic", "The Revenant", "Inception"])
	w.writerow(["Training Day", "Man on Fire", "Flight"])