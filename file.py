file=open("file.txt","w")
file.write("""
    Hello world 
    How are you
           
           """)
file.close()

with open("file.txt","r") as infile:
    text=infile.read()

modified=text.upper()

with open("updated.txt","w") as outfile:
    outfile.write(modified)



