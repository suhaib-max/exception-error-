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

height = float(input("Height: "))
weight = float(input("weight: "))

if height > 3:
    raise ValueError("human height should not over 3 meter")
bmi = weight / height ** 2
print(bmi)
