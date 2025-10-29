import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


#시험볼 때 실제로 작성헤야하는 부분!!!
def plot_graph():
    x=float(x_entry.get())
    y=float(y_entry.get())
    x_data.append(x)
    y_data.append(y)
    ax.clear()
    ax.plot(x_data, y_data, marker='o',linestyle='-')
    canvas.draw()
#**********************************************************


root=tk.Tk()
root.title("Dynamic Line Graph")

x_data=[]
y_data=[]

x_label=tk.Label(root, text="Enter x coordinate:")
x_label.pack()
x_entry=tk.Entry(root)
x_entry.pack()

y_label=tk.Label(root, text="Enter y coordinate:")
y_label.pack()
y_entry=tk.Entry(root)
y_entry.pack()

plot_button=tk.Button(root, text="Plot", command=plot_graph)
plot_button.pack()

fig=Figure(figsize=(5,4), dpi=100)
ax=fig.add_subplot(111)

canvas=FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

root.mainloop()