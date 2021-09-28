string = input()
string_cap= string.split()
new_string=""

for i in string_cap:
    cap=i.capitalize()
    new_string+=cap+" "
print(new_string)
