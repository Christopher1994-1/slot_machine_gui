from faulthandler import disable
from tkinter import PhotoImage, Toplevel
import tkinter
import customtkinter
from PIL import ImageTk, Image
import random


customtkinter.set_appearance_mode("System") 
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.geometry("500x350")
root.title("Slot Machine Game")
root.iconbitmap("darkModeV.ico")

img1 = ImageTk.PhotoImage(Image.open("C:/Users/yklac/Desktop/projects/git_projects/slot_machine_gui/images/7.png"))
img2 = ImageTk.PhotoImage(Image.open("C:/Users/yklac/Desktop/projects/git_projects/slot_machine_gui/images/busted.png"))
img3 = ImageTk.PhotoImage(Image.open("C:/Users/yklac/Desktop/projects/git_projects/slot_machine_gui/images/cherrys.png"))
img1_path = "C:/Users/yklac/Desktop/projects/git_projects/slot_machine/images/7.png"
img2_path = "C:/Users/yklac/Desktop/projects/git_projects/slot_machine/images/busted.png"
img3_path = "C:/Users/yklac/Desktop/projects/git_projects/slot_machine/images/cherrys.png"

balance_amount = 0
balance = f"${balance_amount}"




def wheel():
    number = random.randint(1, 3)
    return number



def spin():
    global balance_amount
    # first image wheel
    if balance_amount > 0:
        wheel1 = wheel()
        if wheel1 == 1:
            image1.configure(image=img1)
        elif wheel1 == 2:
            image1.configure(image=img2)
        elif wheel1 == 3:
            image1.configure(image=img3)

        # second wheel image
        wheel2 = wheel()
        if wheel2 == 1:
            image2.configure(image=img1)
        elif wheel2 == 2:
            image2.configure(image=img2)
        elif wheel2 == 3:
            image2.configure(image=img3)

        # third wheel image
        wheel3 = wheel()
        if wheel3 == 1:
            image3.configure(image=img1)
        elif wheel3 == 2:
            image3.configure(image=img2)
        elif wheel3 == 3:
            image3.configure(image=img3)


        if wheel1 == 1 and wheel2 == 1 and wheel3 == 1:
            error.configure(text="You Win!")
            balance_amount += 1000
            first_frame_balance_label.configure(text=f"Total Balnce:\n{balance_amount}")

        elif wheel1 == 2 and wheel2 == 2 and wheel3 == 2:
            error.configure(text="You Lose!")
            balance_amount -= 100
            first_frame_balance_label.configure(text=f"Total Balnce:\n{balance_amount}")

        elif wheel1 == 3 and wheel2 == 3 and wheel3 == 3:
            error.configure(text="Almost")
            balance_amount += 500
            first_frame_balance_label.configure(text=f"Total Balnce:\n{balance_amount}")
        else:
            error.configure(text="Spin Again!")
            balance_amount -= 5
            first_frame_balance_label.configure(text=f"Total Balnce:\n{balance_amount}")
    elif balance_amount == 0:
        spin_btn.configure(state="disabled")
        error2.configure(text="Please Deposit Funds!", text_color="red")
    elif balance_amount < 0:
        balance_amount = 0
        spin_btn.configure(state="disabled")
        error2.configure(text="Please Deposit Funds!", text_color="red")


def top_level_btn():
    global balance_amount
    amount = entry.get()
    try:
        error_label.configure(text="")
        balance_amount += int(amount)
        first_frame_balance_label.configure(text=f"Total Balance\n{str(balance_amount)}")
    except ValueError:
        error_label.configure(text=f"{amount} Is NOT an Integer!", text_color="red")
    spin_btn.configure(state="normal")
    error2.configure(text="")
    top.destroy()



def deposit():
    global top
    top = customtkinter.CTkToplevel()
    top.title("Deposit Funds")
    top.iconbitmap("darkModeV.ico")
    top.geometry("500x200") # L x W

    # inside top level first frame that holds label
    top_frame1 = customtkinter.CTkFrame(top)
    top_frame1.pack(pady=5)
    # inside top level first frame, first frame label
    deposit_label = customtkinter.CTkLabel(top_frame1, text="Deposit Amount", text_font=("Arial", 18))
    deposit_label.grid(row=0, column=0)

    # inside top level second frame that holds entry amount to deposit
    top_frame2 = customtkinter.CTkFrame(top)
    top_frame2.pack(pady=5)
    # inside top level second frame, entry amount thing
    global entry
    entry = customtkinter.CTkEntry(top_frame2)
    entry.grid(row=0, column=0)

    # inside top level third frame that holds deposit button
    top_frame3 = customtkinter.CTkFrame(top)
    top_frame3.pack(pady=5)
    # top frame button
    top_btn = customtkinter.CTkButton(top_frame3, text="DEPOSIT", command=top_level_btn)
    top_btn.grid(row=0, column=0)

    # label that gives errors when user.
    global error_label
    error_label = customtkinter.CTkLabel(top, text='')
    error_label.pack(pady=10)





p1 = img1
p2 = img1
p3 = img1


# first frame that holds label
first_frame = customtkinter.CTkFrame(root)
first_frame.pack(pady=12)

# slot machine label
first_frame_label = customtkinter.CTkLabel(first_frame, text="Slot Machine", text_color=("white"), corner_radius=14, text_font=("Arial", 24))
first_frame_label.grid(row=0, column=0)

# total balnce label
first_frame_balance_label = customtkinter.CTkLabel(first_frame, text=f"Total Balance\n{balance}")
first_frame_balance_label.grid(row=0, column=1)


# second frame that holds line card things
second_frame = customtkinter.CTkFrame(root)
second_frame.pack(pady=6)


#image 1
image1 = customtkinter.CTkLabel(second_frame, image=p1)
image1.grid(row=0, column=0)
# image 2
image2 = customtkinter.CTkLabel(second_frame, image=p1)
image2.grid(row=0, column=1)
# image 3
image3 = customtkinter.CTkLabel(second_frame, image=p1)
image3.grid(row=0, column=2)


# third frame that holds buttons

third_frame = customtkinter.CTkFrame(root)
third_frame.pack(pady=10)

spin_btn = customtkinter.CTkButton(third_frame, text='SPIN', command=spin)
spin_btn.grid(row=0, column=0, padx=5)

deposit_btn = customtkinter.CTkButton(third_frame, text="Deposit", command=deposit)
deposit_btn.grid(row=0, column=1, padx=5)


error = customtkinter.CTkLabel(root, text="SPIN AWAY!")
error.pack(pady=5)


error2 = customtkinter.CTkLabel(root, text="")
error2.pack(pady=5)

root.mainloop()

print(balance_amount)