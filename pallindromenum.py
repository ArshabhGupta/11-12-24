num = int(input("Enter a number: "))

orig_num = num
rev_num = 0

while num > 0:
    digit = num % 10
    rev_num = rev_num * 10 + digit
    num //= 10

if orig_num == rev_num:
    print("Number is a pallindrome")
else:
    print("Number is not a pallindrome")