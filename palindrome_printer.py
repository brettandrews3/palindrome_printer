# Thing-a-ma-jig exercise from Head First Learn to Code (p. 133 in book, 173 in PDF)
# The code below runs through list 'characters' L-R, then runs through list R-L
# to spell 'TACOCAT' (I'm a palindrome!)

#characters = ['T', 'A', 'C', 'O']      # Outputs 'TACOCAT'
#characters = ['A', 'M', 'A', 'N', 'A', 'P', 'L', 'A', 'N', 'A', 'C'] # Outputs 'A MAN A PLAN A CANAL PANAMA'
#characters = ['W', 'A', 'S', 'I', 'T', 'A', 'R'] # Outputs 'WAS IT A RAT I SAW'
#characters = ['D', 'O', 'N', 'T']      # Outputs 'DONT RUN'
#characters = ['R', 'E', 'D', 'R', 'U', 'M', 'S', 'I', 'R'] # Outputs 'RED RUM SIR IS MURDER'

output = ''                             # a blank space to hold the list output, 1 letter at a time
length = len(characters)                # length = 4
i = 0                                   # Starting point for our counter 'i'
while (i < length):                     # while i < 4:
    output = output + characters[i]     # Print characters, one by one, L-R
    i = i + 1

length = length * -1                    # Print list in reverse using negative indices
i = -2                                  # Starting point is 2nd character from the right

while (i >= length):                    # Counting from -2, -1, 0:
    output = output + characters[i]     # Print characters, one by one, to variable 'output'
    i = i -1                            # Counting down from -2, -1, 0

print(output)                           # Should print 'TACOCAT' (I'm a palindrome!)