# try:
#     file = open("a_file.txt")              #if not work
#     a_dict = {"key":"value"}
#     print(a_dict["efsd"])
# except FileNotFoundError:                  #do this
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_message:          #do this
#     print(f"that {error_message} does not exist")
# else:
#     content = file.read()                  #nothing happened
#     print(content)
# finally:                                   #happened or not Do this for everyone
#     # file.close()
#     # print("file was closed")
#     raise TypeError("this is an error that i made up")   #error we can create

# height = float(input("Height: "))
# weight = float(input("weight: "))
#
# if height > 3:
#     raise ValueError("human height should not over 3 meter")
# bmi = weight / height ** 2
# print(bmi)

facebook_posts = [{'Likes': 21, 'Comments': 2}, {'Likes': 13, 'Comments': 2, 'Shares': 1}, {'Likes': 33, 'Comments': 8, 'Shares': 3}, {'Comments': 4, 'Shares': 2},{'Comments': 1, 'Shares': 1}, {'Likes': 19, 'Comments': 3}]

total_likes = 0
# Catching the KeyError exception in the dictionary
for post in facebook_posts:
  try:
    total_likes = total_likes + post['Likes']
  except KeyError:
    pass

print(total_likes)
