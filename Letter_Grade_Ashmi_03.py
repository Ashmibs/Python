"""
Program: Letter Grade Project
Author: Ashmi Bidrupane Suresh
Description: This program Computes final course grades for students based on percentage scores using a function. 
	00 - Announce and get the first and second numbers from the user
	01 - Compute and print the next number in the sequence
"""

#Announce
print("Program to compute a letter grade for a numerical score\n")


# prompt the user for an input
score = float(input("Enter the numerical score:"))

def grade(score):

    #check for A+s
    if score <= 95 and score >= 100:
        print("The letter grade for",score,"percent is,A+.")

    #Check for As
     
    elif score <95 and score >=90:
        print("The letter grade for",score,"percent is,A-.")

    #check for A-
    elif score <90 and score >=85:
        print("The letter grade for",score,"percent is,A.")

    #check for B+s
    elif score <85 and score >=80:
        print("The letter grade for",score,"percent is,B+.")

    #check for Bs
    elif score <80 and score >=75:
        print("The letter grade for",score,"percent is,B.")

    #check for B-s
    elif score <75 and score >=70:
        print("The letter grade for",score,"percent is,B-.")

    #check for C+
    elif score <70 and score >=65:
        print("The letter grade for",score,"percent is,C+.")

    #check for Cs
    elif score <65 and score >=60:
        print("The letter grade for",score,"percent is,C.")

    #check for C-s
    elif score <60 and score >=55:
        print("The letter grade for",score,"percent is,C-.")

    #check for Fs
    elif score <55 and score >=0:
        print("The letter grade for",score,"percent is,F.")
        
    else:
         print("This is invalid,Please try again")

grade(score);




