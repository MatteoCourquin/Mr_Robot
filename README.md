# Mr_Robot

***• Card Generator :***

The code contains a few conditions (if) and a loop (while).

The starting condition checks that there is no error when choosing the cards, the second selects the type of card and adds a first number according to it (visa or mastercard).

The while loop adds 15 random numbers to make the complete map.

And I post it last.

***• Password Generator :***

First, I check (with an if) if the user entered a number. If it is not the case I return an error to him.

Then (in a while loop) I generate random numbers and letters.

Then I mix it all up and display my password proposal


***• Pin code :***

First, I import the "hashlib" function that allows me to hash passwords.

After I pass in parameter "8a069869956a4e0cf7ac69f9c20e0d49", which is the hash of the password to look for.

Then I created a function which generates all the numbers from 99999999 to 9999999 and the hashes.
In this function I compare all the hashes of these numbers to "8a069869956a4e0cf7ac69f9c20e0d49". And if a hash matches, the loop stops and displays the password.
Otherwise, if no password matches, I display it and stop the loop.


***• Binery to Hexa :***

I start by asking for a binary number.

Then I create a function which returns me the letters corresponding to the numbers.

Below I create a condition to check if the user has entered a binary. If it's ok, I execute my code, otherwise I return an error.

If the format of the binary is correct I launch a loop which calculates by portion of 4 the result of my binary. Then I call on my function to retrieve the letters.

Finally I display all.