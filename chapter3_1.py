import random
friends_name=["ali","kamal","aamir"];
print(friends_name[0])
print(friends_name[1])
print(friends_name[2])

#try it yourself 3.2
print(f"hi, {friends_name[0]}");
print(f"hi, {friends_name[1]}");
print(f"hi, {friends_name[2]}");

my_favorit_place = ["macca","madina","islamabd","kabul"]
print(my_favorit_place)
print(sorted(my_favorit_place))
print(my_favorit_place)
my_favorit_place.reverse()
print(my_favorit_place)
my_favorit_place.reverse()
print(my_favorit_place)
my_favorit_place.sort()
print(my_favorit_place)
my_favorit_place.sort(reverse=True)
print(my_favorit_place)

def random_functionn():
    return random.randrange(2,20,2)
print(random_functionn())
print(random_functionn())
print(random_functionn())

list_invite_to_dinne = ["ali","azam","hasan"]
print(list_invite_to_dinne[0],", you are invites for dinner")
print(list_invite_to_dinne[1],", you are invites for dinner")
print(list_invite_to_dinne[2],", you are invites for dinner")

print(len(list_invite_to_dinne)," are invited for dinner")
text = "hello, wordl";
print("o" in text);

print(text[2:5])
print(text.replace("word","prattam"))
a = "Hello, World!"
b = a.split(",,")
print(b)
# store pizza flavor and print it in loop
pizza_flavor = ["chicken","vegetarion","chees"]
for flavor in pizza_flavor:
    print("i like "+flavor+" pizza")
print("i like cheez pizza")
print("because it contain cheez which is my favorite food")
print("i realy like pizza")

#4.3
animals = ["cow" ,"goat" ,"camel"]
for animal in animals:
    #print(animal)
    print(animal+" gives us milk")
print("all these animal give us milk")