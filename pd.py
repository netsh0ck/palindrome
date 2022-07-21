number = input("Enter any number to check if it is a palindrome: ")
# original value to use in condtions
temporary = number
# var to use for operations
reverse = 0
remainder = reverse

while(temporary > 0):
    remainder = temporary % 10
    temporary = temporary / 10
    reverse = reverse * 10 + remainder

if(int(number) == reverse) :
    print "\n\t\tGiven number " +str(number)+" is palindrome"
else :
    print "\n\t\tGiven number " +str(number)+" is not a palindrome"
