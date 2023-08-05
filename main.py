print("Welcome to the Love Calculator!")

name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lowercase_name1 = name1.lower()
lowercase_name2 = name2.lower()

result_string = lowercase_name1+lowercase_name2

count_t = result_string.count("t")
count_r = result_string.count("r")
count_u = result_string.count("u")
count_e = result_string.count("e")

sum_true = count_t+count_r+count_u+count_e

count_l = result_string.count("l")
count_o = result_string.count("o")
count_v = result_string.count("v")
count_e = result_string.count("e")

sum_true = count_t+count_r+count_u+count_e
sum_love = count_l+count_o+count_v+count_e

print(f"Total number of true is {sum_true} ")
print(f"Total number of love is {sum_love} ")

love_score= str(sum_true)+ str(sum_love)

total = int(love_score)

if total < 10 or total > 90 :
  print(f"your score is {total},you go togerther like coke and mentos")
elif total>=40 and total<=50 :
  print(f"Your score is {total}, you are alright together.")
else:
  print(f"Your score is {total}")
  
