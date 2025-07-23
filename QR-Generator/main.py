#importing required modules
import customtkinter as tk  # for GUI
from tkinter import filedialog,messagebox   # for saving the image and show messages
import qrcode  #for creating qr


# functional part

def Gen_qr():
    inp1=inp.get()
    if inp1=="":
        messagebox.showinfo("Alert","pls enter something")
    else:
        global qr
        qr=qrcode.make(inp1)
        qr=qr.resize((280,280))
        if qr:
            # Convert to CTkImage for compatibility
            qr_ctk_img = tk.CTkImage(light_image=qr, dark_image=qr, size=(280, 280))

            # Clear old QR code if any
            for widget in img_area.winfo_children():
                widget.destroy()
            img_label = tk.CTkLabel(img_area, image=qr_ctk_img, text="")
            img_label.image = qr_ctk_img  # Prevent garbage collection
            img_label.pack(pady=20,padx=20)

        else:
            messagebox.showinfo('info','something went wrong')

# function to save the generated qr
def Save():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")]) #open the dialog box to save the img
    if file_path:
            qr.save(file_path)
            messagebox.showinfo("Saved", f"QR code saved to:\n{file_path}")

def Reset():
    inp.delete(0, tk.END)  # Clear the text input
    
    # Clear old QR code if any
    for widget in img_area.winfo_children():
        widget.destroy()



# Initialize the app window
root = tk.CTk()
root.title("QR Generator")
root.geometry("400x450")
root.resizable(False, False)

# Entry field
inp = tk.CTkEntry(root, placeholder_text="Enter text or URL", width=250)
inp.grid(row=0, column=0, padx=(20, 10), pady=(20,10), sticky="w")

# Generate button
gen = tk.CTkButton(root, text="Generate", width=90,command=Gen_qr)
gen.grid(row=0, column=1, padx=(0, 20), pady=(20,10), sticky="e")

# Image display area
img_area = tk.CTkFrame(root, height=300, width=350)
img_area.grid(row=1, column=0, columnspan=2)
img_area.grid_propagate(False)

# Container for buttons
btn_frame = tk.CTkFrame(root)
btn_frame.grid(row=2, column=0, columnspan=2, pady=(10, 20))

# Save and Reset buttons inside the frame
save_btn = tk.CTkButton(btn_frame, text="Save", width=155,command=Save)
save_btn.pack(side="left", padx=10,pady=10)

reset_btn = tk.CTkButton(btn_frame, text="Reset", width=155,command=Reset)
reset_btn.pack(side="right", padx=10,pady=10)

# Start the GUI loop
root.mainloop()
