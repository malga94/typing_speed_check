After cloning the repo, create an environment variable named `DICTIONARY_PATH`, containing a path to a file. This file acts as the dictionary 
for the program, and the text that the user will have to type is sampled from the file. The structure of the file is a list of words separated by 
newline characters.

On Linux and Mac, there are files in /usr/share/dict/ containing huge lists of words which can be used. You can customize things like the minimum length
of the words by using grep and piping the output to a new file.

For example, on Mac OS you can do `grep -e '^[a-z]\{4\}' /usr/share/dict/words > PATH_TO_CLONED_REPO/dict.txt` followed by 
`DICTIONARY_PATH=PATH_TO_CLONED_REPO/dict.txt`to get a large amount of words with more than 3 letters.

After configuring `DICTIONARY_PATH`, just run the script normally with `python speedtest.py` and check how quickly you can type.
