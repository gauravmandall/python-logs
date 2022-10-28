'''
    String Functions
        some of the mostly used functions to perform operations
        on or manipulate strings are :
            1> len() function --> This function returns the length of the string
                    len ("Gaurav") --> returns 6
            
            2> string endswith("rav") --> This function tells whether the variable 
            string ends with the string "rav" or not. if string is "Gaurav", it 
            returns true for "rav" since Harry ends with rav.
            
            3> string.count("c") --> Counts the total number of occurence of any character.

            4> string.capitalize() --> This function capitalizes the first character of a given string.

            5> string.find(word) --> This function finds a word and returns the index of first occurence of 
            thhat word in the string.

            6> string.replace(old_word, new_word) --> This function replaces the oldword with newword in the entire string.
'''



story = "once upon a time there was a youtuber named Gaurav who uploaded python course with notes"

# String Functions
print(len(story))
print(story.endswith("notes"))
print(story.count("c"))
print(story.capitalize())
print(story.find("Gaurav"))
print(story.replace("Gaurav", "Gaurav (the certified Ethical Hacker)"))