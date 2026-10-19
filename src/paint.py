import tkinter as tk,math
r=tk.Tk();r.geometry("420x420");i=n=12
while i:
 i-=1;a=2*math.pi*i/n
 tk.Button(r,text=str(i+1),width=3).place(x=200+120*math.cos(a),y=200+120*math.sin(a))
r.mainloop()