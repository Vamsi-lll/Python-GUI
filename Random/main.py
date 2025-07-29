import customtkinter as tk
import random

def Roll():
    ran_num=random.randint(0,7)
    label.configure(text=ran_num)
    
root=tk.CTk()
root.title('random')
root.geometry("400x300")
root.resizable(False,False)
frame1=tk.CTkFrame(root,width=380,height=50)
frame1.grid(row=0,column=0,padx=10,pady=10)

random_num=tk.CTkButton(frame1,text="random num",width=50)
random_num.grid(row=0,column=0,padx=10,pady=10)

roll=tk.CTkButton(frame1,text='roll',command=Roll)
roll.grid(row=0,column=1,padx=(0,10))

rcp=tk.CTkButton(frame1,text='RCP',width=100)
rcp.grid(row=0,column=2,padx=(0,5))

frame2=tk.CTkFrame(root,width=380,height=200)
frame2.grid(row=1,column=0,padx=10)

label=tk.CTkLabel(frame2,text="",font=('calibri',100))
label.pack(padx=10,pady=10)
root.mainloop()
