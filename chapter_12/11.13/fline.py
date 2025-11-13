infile=open("chapter_12/11.13/proverbs.txt",'r')
outfile=open('output.txt','w')

i=1
for line in infile:
    outfile.write(str(i)+": "+line)
    i=i+1

infile.close()
outfile.close()