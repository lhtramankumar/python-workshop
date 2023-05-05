guest={} 

total_guest= int(input("Enter the total no of guest : "))

for i in range(total_guest) :
  name = input("Enter the name of guest : ")
  food = input("Enter the name of favorite food : ")
  guest_info =[name,food]
  guest[name]=guest_info

for name, guest_info in guest.items() :
   print(name+ ":"+guest_info[1])
