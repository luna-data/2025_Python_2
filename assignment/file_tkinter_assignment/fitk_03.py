import os
base_dir=os.path.dirname(__file__)
filepath1=os.path.join(base_dir,"file1.txt")
filepath2=os.path.join(base_dir,"file2.txt")
infile1=open(filepath1,"r",encoding="utf-8")
infile2=open(filepath2,"r",encoding="utf-8")

line1=infile1.readline()
line2=infile2.readline()

filepath3=os.path.join(base_dir,"output.txt")
outfile=open(filepath3,"w",encoding="utf-8")

for i in (line1,line2):
    i=i.rstrip()
    outfile.write(i+"\n")
    


infile1.close()
infile2.close()
outfile.close()