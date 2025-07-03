# bat = "Yes" and "No"
# weather = "Good" and "bad"
# if bat == "Yes" and weather == "Good":
#     print("Go out and play cricket")
# elif bat == "No" and weather == "Good":
#     print("Go out and play football")
# elif bat == "Yes" and weather == "Bad":
#     print("Play cricket at home")
# else:
#     print("Play football at home")

# # nested if
# if weather == "Good":
#     bat = input("Do you want to play cricket? (Yes/No): ")
#     if bat == "Yes":
#         print("Go out and play cricket")
#     else:
#         print("cannot play cricket")
# else:
#     print("cant play cricket")
# # for loop

# for i in range(50):
#     for j in range(i, 51):
#         j = j / 3
#         if 0:
#             continue
#         else:
#             break
#     print(i, j)

# n = int(input("enter a number:"))
# factorial = 1
# for i in range(1, n + 1):
#     factorial = factorial * i

# print(factorial)


for i in range(20, 0, -1):
    print(i)


str = "hello"
for ch in str:
    if ch == "o":
        break

    print(ch, end="")
