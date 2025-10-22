from tkinter import *
def click(key):
    if key=='=':
        try:
            result=eval(entry.get())
            entry.delete(0,END)
            entry.insert(END,str(result))
        except:
            entry.insert(END, "오류!")
    elif key =='C':
        entry.delete(0,END)
    else:
        entry.insert(END, key)

root=Tk()
root.title("간단한 계산기")

buttons=[
    '7','8','9','+','C',
    '4','5','6','-',' ',
    '1','2','3','*',' ',
    '0','.','=','/',' ']

i=0
for b in buttons:
    cmd=lambda x=b: click(x)
    b=Button(root, text=b, width=5, relief="ridge",command=cmd)
    b.grid(row=i//5+1,column=i%5)
    i+=1

entry=Entry(root, width=33, bg="yellow")
entry.grid(row=0,column=0,columnspan=5)

root.mainloop()
