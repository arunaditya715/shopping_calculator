
sum=0
while True:
    userInput=input("Please enter a valid price or press q to quit\n")
    if (userInput!='q'):
        sum=sum+eval(userInput)
        print(f"The total price is so far{sum}")

    else:
        print(f"Your Total bill is {sum}.Thanks for shopping with us")
        break
