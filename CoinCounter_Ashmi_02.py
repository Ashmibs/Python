"""
Program: Coin Counter 
Author: Ashmi Bidrupane Suresh
Description: This program will read the string using the input() function and calculate the number of each type of coin, the value of each type of coin and the total monetary value represented. 
Revisions:
	00 - Announce and get the string from the user in lower case
	01 - Initialise the variable to 0 and using for loop to transverse through string and calculate the total amount
	02 - To print the output in the given format.
"""
#Announce
print("Program to count coins and calculate values\n")

#To prompt input from the user in lower case (if entered in upper case as well)
s = input("Enter coin string: ").lower()

#initialising variables (Pennies(p),Nickels(n),Dimes(d),Quaters(q),Half-dollars(h)) to 0
p=0
n=0
d=0
q=0
h=0

#For loop to transverse through the enetered string to increase the variable coint by 1 if the variable is present in string
for c in s: 
    if(c == "p"): 
        p+=1
    elif(c == "n"):
        n+=1
    elif(c == "d"):
        d+=1
    elif(c == "q"):
        q+=1
    else:
        h+=1

# To calculate the total monetary value       
total=(p*0.01+n*0.05+d*0.10+q*0.25+h*0.50) 

#To print in the output in the given format.
print("\n===========================================")
print(f"{f'Coin Counter Report':^43}")
print("===========================================\n")
print(f"Coin{f'Value':>19}\t{f' ':>3}Number{f' ':>4}Amount")
print(f"===={f'=====':>19}\t{f' ':>3}======{f' ':>4}======")
print(f"Pennies{f' ':>8}{f'${0.01}':>8}\t{f' ':>4}{f'{p}':>2}{f' ':>7}${f'{p*0.01:4.2f}':>5}")
print(f"Nickels{f' ':>8}{f'${0.05}':>8}\t{f' ':>5}{f'{n}':<2}{f' ':>6}${f'{n*0.05:4.2f}':>5}")
print(f"Dimes{f' ':>10}{f'${0.10:.2f}':>8}\t{f' ':>5}{f'{d}':<2}{f' ':>6}${f'{d*0.10:4.2f}':>5}")
print(f"Quaters{f' ':>8}{f'${0.25}':>8}\t{f' ':>5}{f'{q}':<2}{f' ':>6}${f'{q*0.25:4.2f}':>5}")
print(f"Half-dollars{f' ':>3}{f'${0.50:.2f}':>8}\t{f' ':>5}{f'{h}':<2}{f' ':>6}${f'{h*0.50:4.2f}':>5}")
print(f"{f'Total amount: $ {total}':>43}")
