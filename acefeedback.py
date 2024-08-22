import sys
import webbrowser

print("""
      / \  / ___| ____|
     / _ \| |   |  _|  
    / _ \ \ |___| |___ 
   /_/   \_\____|_____|   
   -------------------------------------------------------------------------------
   A SIMPLE USER'S FEEDBACK
   -------------------------------------------------------------------------------
   author:DOMINGUEZ ACE
""")
url = "https://www.facebook.com/nagatoxbadside"
name = input("Enter your name: ")
print("nice name " + name)
ask = input("What is your rate in Ace tool it is: (bad/not bad)")
if ask == "bad":
   print("i'm so sorry for that let me upgrade it and i'll promise i'll do a better tool next project")
elif ask == "not bad":
     print("wow thankyou i appreciate it")
else:
    print("sorry wrong input")

use = input("Do you use the tool that Dominguez Ace develop??: (yes/no)")
if use == "yes":
   print("Wow thankyou for using it")
   
elif use == "no":
     print("You should use it now!!")
else:
    print("sorry wrong input")

want = input("Do you want to know more about Dominguez Ace???: (yes/no)")
if want == "yes":
   webbrowser.open(url)
elif want == "no":
     print("why you should know me better")
else:
    print("sorry wrong input")
