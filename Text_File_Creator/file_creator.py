name = input("What's your name? \n")
color = input("What is your favorite color? ")
with open("user_data.txt", "a") as file:
    file.write(f"Favorite color: {color}\n")

with open('example.txt', 'w') as file:
    file.write(f"{name} created this file")
