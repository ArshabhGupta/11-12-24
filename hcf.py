largest = int(input("Enter a number: "))
smallest = int(input("Enter a number: "))

while(smallest):
    store = smallest
    smallest = largest % smallest
    largest = store

print("The HCF is: ", largest)