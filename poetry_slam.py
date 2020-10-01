import random

def get_file_lines(filename):
    """ 
    return a list of strings containing the lines of the file.
    """

poem = "PoetrySlam/poem.txt"
infile = open(poem, "r")
        #   return infile.read()

# print(infile.read())
infile.close()


def lines_printed_backwards(lines_list):

    """
   returns the lines of the poem in reverse

    """
    f = open(lines_list, "r") #lines_list is a list of strings containing lines of my poem f is the opened poem in read mode
    line_list = f.read().splitlines() # n/ effect so each line has a break 
    line_num =len(line_list) #adds the line numbers to the length of line_list
    line_list = line_list[::-1] #reversing
   
    for i in range(len(line_list)): 
        reverse = str(line_num -i) + " " + line_list[i]
        print(reverse)
        infile.close()
lines_printed_backwards("PoetrySlam/poem.txt")

def lines_printed_random(lines_list):
    """
    prints lines of poem in random order
    """ 
    f = open(lines_list, "r") #lines_list is a list of strings containing lines of my poem f is the opened poem in read mode
    line_list = f.read().splitlines() # n/ effect so each line has a break 
    line_num =len(line_list) #adds the line numbers to the length of line_list

    print(random.randint(1,32))#uses intergers not floats both numbers are inclusive


def lines_printed_custom(Lines_list):

   