guest_list = ["obama", "putin" , "kojima"]

for i in range(len(guest_list)):
    print(guest_list[i] + ", can you come to my house for dinner tonight?" )

print(guest_list[0] + " and " + guest_list[1] + " can't make it to dinner ")
del guest_list[0:2]
print(guest_list)
guest_list.append("shakira")
guest_list.append("alice")
print(guest_list)
for i in range(len(guest_list)):
    print(guest_list[i] + ", can you come to my house for dinner tonight?" )
for i in range(len(guest_list)):
    print(guest_list[i] + ", i found a bigger table")
guest_list.insert(0,"selena")
guest_list.insert(2,"charlize")
guest_list.append("vanessa")
print(guest_list)
for i in range(len(guest_list)):
    print(guest_list[i] + ", can you come to my house for dinner tonight?" )
cancel_invitation = ", i can only invite 2 people"
for i in range(len(guest_list)):
    print(guest_list[i] + cancel_invitation )
remove_guest = guest_list.pop(-1)
for i in range (3):
    remove_guest = guest_list.pop(-1)
    print(remove_guest + ", i cancel ur invitation")
for i in range (len(guest_list)):
    print(guest_list[i] + ", you're still invited")

del guest_list[0:2]
print(guest_list)

place = ["Japan", "Australia" , "United Kingdom", "Belgia", "Chilli"]
print(place)
print(sorted(place))
print(place)
print(sorted(place,reverse=True))
print(place)
place.reverse()
print(place)
place.reverse()
print(place)
place.sort()
print(place)
place.reverse()
print(place)
x =5/2
print(x)

































