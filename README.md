# Run-Length-Encoding

>19th June 2021 09:19 PM

Been a hot minute 🥵 Literally cuz it's so fricking hot outside these days - it's 9 PM and it's still like 40 degrees outside.

***Given a string s, return its run-length encoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters.***

So basically we start with the most general case i.e if there's only 1 letter. So we print 1 along with the letter in a string.

For the other cases we are gonna iterate from the second character in the string. In this if statement we're sort of covering what should be done in the cases where the next letter is not the same. If two consecutive letters aren't the same then you print the counter with the "previous letter" i.e ``s[i-1]``. And the variable prevLetter is set to the "new" letter that has been encountered.

You'll only hit this after it's counted all consecutive occurences of a letter - until it hits that the counter keeps being incremented.
