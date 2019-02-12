import os

num_lines = sum(1 for line in open('/tmp/poses_dump.txt'))
if num_lines > 1098:
    print("modifying poses dump to 1098 poses")
    file = open('/tmp/poses_dump.txt', "r+", encoding = "utf-8")

    #Move the pointer (similar to a cursor in a text editor) to the end of the file. 
    file.seek(0, os.SEEK_END)

    #This code means the following code skips the very last character in the file - 
    #i.e. in the case the last line is null we delete the last line 
    #and the penultimate one
    pos = file.tell() - 1

    #Read each character in the file one at a time from the penultimate 
    #character going backwards, searching for a newline character
    #If we find a new line, exit the search
    while pos > 0 and file.read(1) != "\n":
        pos -= 1
        file.seek(pos, os.SEEK_SET)

    #So long as we're not at the start of the file, delete all the characters ahead of this position
    if pos > 0:
        file.seek(pos, os.SEEK_SET)
        file.truncate()

    file.close()

num_lines = sum(1 for line in open('/tmp/poses_dump.txt'))
print(num_lines)   
