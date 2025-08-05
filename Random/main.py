import customtkinter as tk
import random
import threading
import time

def Roll():
    def roll_animation():
        # Disable button during animation
        roll.configure(state="disabled")
        
        # Animation effect - show rolling
        for i in range(8):
            temp_num = random.randint(1,6)
            label.configure(text=f"🎲 {temp_num}", font=('Arial', 72, 'bold'), text_color="#FFB84D")
            root.update()
            time.sleep(0.1)
        
        # Final result
        final_num = random.randint(1,6)
        label.configure(text=f"🎲 {final_num}", font=('Arial', 72, 'bold'), text_color="#FF6B6B")
        
        # Re-enable button
        roll.configure(state="normal")
    
    # Run animation in separate thread
    thread = threading.Thread(target=roll_animation, daemon=True)
    thread.start()

def RandomNum():
    def random_animation():
        # Disable button during animation
        random_num.configure(state="disabled")
        
        # Animation effect - show counting
        for i in range(10):
            temp_num = random.randint(1,100)
            label.configure(text=f"{temp_num}", font=('Arial', 80, 'bold'), text_color="#FFB84D")
            root.update()
            time.sleep(0.05)
        
        # Final result
        final_num = random.randint(1,100)
        label.configure(text=f"{final_num}", font=('Arial', 80, 'bold'), text_color="#4ECDC4")
        
        # Re-enable button
        random_num.configure(state="normal")
    
    # Run animation in separate thread
    thread = threading.Thread(target=random_animation, daemon=True)
    thread.start()

def RCP():
    def rcp_animation():
        # Disable button during animation
        rcp.configure(state="disabled")
        
        choices = ["🪨", "📄", "✂️"]
        choice_names = ["Rock", "Paper", "Scissors"]
        
        # Animation effect - show cycling
        for i in range(12):
            temp_idx = random.randint(0, 2)
            label.configure(text=f"{choices[temp_idx]}\n{choice_names[temp_idx]}", 
                           font=('Arial', 48, 'bold'), text_color="#FFB84D")
            root.update()
            time.sleep(0.08)
        
        # Final result
        final_idx = random.randint(0, 2)
        label.configure(text=f"{choices[final_idx]}\n{choice_names[final_idx]}", 
                       font=('Arial', 48, 'bold'), text_color="#45B7D1")
        
        # Re-enable button
        rcp.configure(state="normal")
    
    # Run animation in separate thread
    thread = threading.Thread(target=rcp_animation, daemon=True)
    thread.start()
    
root=tk.CTk()
root.title('🎲 Random Generator')
root.geometry("500x350")
root.resizable(False,False)

# Configure grid weights for responsive layout
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)

# Button frame with better proportions
frame1=tk.CTkFrame(root, height=70)
frame1.grid(row=0, column=0, padx=15, pady=15, sticky="ew")
frame1.grid_columnconfigure((0,1,2), weight=1)

random_num=tk.CTkButton(frame1, text="Random Num\n(1-100)", width=140, height=50, 
                       font=('Arial', 12, 'bold'), command=RandomNum)
random_num.grid(row=0, column=0, padx=8, pady=10)

roll=tk.CTkButton(frame1, text='🎲 Dice Roll\n(1-6)', width=140, height=50, 
                 font=('Arial', 12, 'bold'), command=Roll)
roll.grid(row=0, column=1, padx=8, pady=10)

rcp=tk.CTkButton(frame1, text='✂️ Rock Paper\nScissors', width=140, height=50, 
                font=('Arial', 12, 'bold'), command=RCP)
rcp.grid(row=0, column=2, padx=8, pady=10)

# Result display frame with better proportions
frame2=tk.CTkFrame(root)
frame2.grid(row=1, column=0, padx=15, pady=(0,15), sticky="nsew")
frame2.grid_columnconfigure(0, weight=1)
frame2.grid_rowconfigure(0, weight=1)

label=tk.CTkLabel(frame2, text="Click any button to start!", 
                 font=('Arial', 24, 'bold'), text_color="#00D4FF")
label.grid(row=0, column=0, padx=20, pady=20)
root.mainloop()
