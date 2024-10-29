# create a file named "number.txt" containing 50 integers, separate all the even and odd numbers in 2 differnt file 

numbers = open("number.txt", 'a')

n = int(input("Enter the range: "))
for i in range(n):
    numbers.write(str(i+1) + ",")

numbers.close()

numbers = open("number.txt", 'r')
content = numbers.read()
numbers.close()

num_arr = content.split(",")
num_arr.pop()
print(num_arr)
print(len(num_arr))

even = open("even.txt", 'w')
even.write('')
even.close()
odd = open("odd.txt", 'w')
odd.write('')
odd.close()

even = open("even.txt", 'a')
odd = open("odd.txt", 'a')


for i in range(len(num_arr)):
    if int(num_arr[i]) % 2 == 0:
        even.write(num_arr[i] + " ")
    else:
        odd.write(num_arr[i] + " ")

even.close()
odd.close()