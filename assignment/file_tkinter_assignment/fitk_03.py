infile1=open("assignment/file_tkinter_assignment/file1.txt","r",encoding="utf-8")
infile2=open("assignment/file_tkinter_assignment/file2.txt","r",encoding="utf-8")

line1=infile1.readline()
line2=infile2.readline()

outfile=open("assignment/file_tkinter_assignment/output.txt","w",encoding="utf-8")

for i in (line1,line2):
    i=i.rstrip()
    outfile.write(i+"\n")
    


infile1.close()
infile2.close()
outfile.close()