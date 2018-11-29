# Wordlist Creator manpage

Wordlist Creator is a simple tool which purpose is to produce all the combinations
of words starting from a pattern. 

The basic running command is: 

$ python3 wordlist_creator.py %ord 

If no dictionary is specified (option -d) then the default one is used. Accepted dictionaries are:
-d 'alphabet' #(default)
-d 'numbers'
-d custom dictionary

The script will recognise the placeholder's position (% this is a placeholder) and it will  substitute each of them based on the provided dictionary.

The basic command above will produce the following output:

aord
bord
cord
....
word
....
sord
....
zord


Note: to specify a Custom dictionary simply put letter, symbols or numbers in a file, with no space, no carriage return. For example, if I would use just vocals I would to the script input a file containing:

"aeiou" <- Named for example vocals.txt

command: $ python3 wordlist_creator.py %ord -d /path/to/vocals.txt
