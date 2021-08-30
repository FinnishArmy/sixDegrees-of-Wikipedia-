 # CS 224 Assignment - sixDegrees
 
The goal is to get from a random starting page to Star Wars in no more than 6 hops.  A ‘hop’ isa single link followed, including Star Wars, but not your starting page.  However, there are somerules for which links are permissible:
•All links must remain inside Wikipedia
•Links may not go through special pages, like categories or files
•Links within the same page do not count
•Links must be in the main body of the article, not in the left-hand sidebar
 
 ## Usage
 
To run, cd into the directory you downloaded.

Run, " python3 wiki.py "

To try a specific Wikipedia page, change the url on the variable, "inputUrl"


 # Bugs
 
There are some problems with the code. 

For one, it doesn't succesfully go into each URL once it finds all of them on the inputUrl. 
Secondly, when it does find the Star Wars url, it prints that it found it multiple times, same with if it doesn't find it.
It also doesn't print the path at which it found the url, but that's because it doesn't even make a path in the first place.
