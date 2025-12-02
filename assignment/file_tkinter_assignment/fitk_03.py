infile1=open("file_tkinter_assignment/file1.txt","r")
infile2=open("file_tkinter_assignment/file2.txt","r")

line1=infile1.readline()
line2=infile2.readline()

outfile=open("file_tkinter_assignment/output.txt","w")

while i in (line1,line2):
    i=i.rstrip()
    outfile.write(i)
outfile=open("output.txt","w")

infile1.close()
infile2.close()
outfile.close()