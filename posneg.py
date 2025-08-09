##n=float(input("enter a number: "))
#if n>0:
    #print("number is positive")
#else:
    #print("number is negative")



#n=float(input("enter a number:"))
#if n%2==0:
 #   print("number is even")
#else:
 #   print("number is odd")



ch = input("Enter a alphabet: ")

if len(ch) == 1 :
    if ch in ['a', 'e', 'i', 'o', 'u']:
        print("The character is a vowel.")
    else:
        print("The character is a consonant.")
else:
    print("Invalid input.")
