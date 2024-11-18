# add your code here
cipher = {
    'a':'f',
    'b':'g', 
    'c':'h', 
    "d": "i",
    "e": "j",
    "f": "k",
    "g": "l",
    "h": "m",
    "i": "n",
    "j": "o",
    "k": "p",
    "l": "q",
    "m": "r",
    "n": "s",
    "o": "t",
    "p": "u",
    "q": "v",
    "r": "w",
    "s": "x",
    "t": "y",
    "u": "z",
    "v": "a",
    "w": "b",
    "x": "c",
    "y": "d",
    "z": "e",
}

userinput = input("Enter the message to encrypt. ")
userinput = userinput.lower()

cipher_message = ""
for letter in userinput:
    if letter in cipher:
        letter = cipher[letter]
    cipher_message += letter
   
print("You entered: " + userinput + "\nThe encrypted message is: " + cipher_message)