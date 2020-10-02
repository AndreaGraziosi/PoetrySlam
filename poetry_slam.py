from random import choice

#worked with Joi , Sawywer
def get_file_lines(filename):
    """ 
    return a list of strings containing the lines of the file.
    """
    infile = open(filename, "r")
    poem = infile.readlines()
    infile.close()
    return poem

#print (get_file_lines('PoetrySlam/poem.txt'))

 

def lines_printed_backwards(lines_list):
#worked with Joi , Sawywer
    """
   returns the lines of the poem in reverse
    """
    lines_list.reverse() #this reverses a list .reverse()
    lines_list_length = len(lines_list)
   
    for i in range(lines_list_length): #changed the for loops to use index so we can have the nums
        current_line = lines_list_length[i]
        line_num = lines_list_length - i
        print(f"{(line_num} {current_line}")
        


def lines_printed_random(lines_list):
    """
    prints lines of poem in random order
    """ 
    for line in lines_list:
         print(choice(lines_list))


def lines_printed_custom(lines_list):

    
  vowels= ["a", "e", "i", "o", "u"]

  #this loop will not print any lines sarting with a vowel
  for line in lines_list:
    # if it doesn't start with a vowel, print
    if line[0] not in vowels:
      print(line)
    
     
        


       
poem_lines = get_file_lines("PoetrySlam/poem.txt")

lines_printed_backwards(poem_lines)
lines_printed_random(poem_lines)
lines_printed_custom(poem_lines)