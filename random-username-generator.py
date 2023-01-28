#Insert first and last name here

first_name = "Random"
last_name = "Person"
random_username = []

#You can adjust the range as preferred, as well as the variation of letters to be used

for x in range(100):
    username = first_name[0] + last_name[0] + str(x)
    random_username.append(username)
    username = first_name[1] + last_name[1] + str(x)
    random_username.append(username)
    username = first_name[2] + last_name[2] + str(x)
    random_username.append(username)
    username = first_name[3] + last_name[3] + str(x)
    random_username.append(username)
    username = first_name[4] + last_name[4] + str(x)
    random_username.append(username)
    username = first_name[5] + last_name[5] + str(x)
    random_username.append(username)

print(random_username)

#This portion saves the usernames as the text file "random-usernames.txt", this can be changed if used more than once.

with open("random-usernames.txt", "w") as file:
        file.write("/n" .join(random_username))
