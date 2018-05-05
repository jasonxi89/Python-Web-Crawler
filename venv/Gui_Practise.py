import tkinter as tk

window = tk.Tk()

window.title('my window')
window.geometry('200x200')

# var= tk.StringVar()
#
#
# l = tk.Label(window, textvariable=var, bg="green",width=15,height=2)
# l.pack()
# on_hit = False
# def hit_me():
#     global  on_hit
#     if on_hit==False:
#         on_hit =True
#         var.set('you hit me')
#     else:
#         on_hit=False
#         var.set('')


# e = tk.Entry(window,show = '*')
# e.pack()

# def insert_point():
#     var = e.get()
#     t.insert('insert', var)
#
# def insert_end():
#     var = e.get()
#     t.insert('end', var)


var1=tk.StringVar()
l = tk.Label(window, textvariable=var1 , bg= "yellow", width = 15, height = 2)
l.pack()

var2= tk.StringVar()
var2.set((1,2,3,4,5,6,7,8,9,10))
lb= tk.Listbox(window,listvariable=var2)
list_items=[1,2,3,4]
for item in list_items:
    lb.insert('end',item)
lb.pack()

def print_selection():
    value = lb.get(lb.curselection())
    var1.set(value)


b1 = tk.Button(window, text='print selection', width = 15 , height = 2, command=print_selection)
b1.pack()

# b2 = tk.Button(window, text = 'insert end', width = 15 , height = 2, command=insert_end)
# t = tk.Text(window,height=2)
# b2.pack()
# t.pack()
window.mainloop()




