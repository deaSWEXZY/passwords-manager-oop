from tkinter import *
from tkinter import messagebox
from generator import PasswordGeneration
from PIL import Image, ImageTk

# --- DESIGN CONSTANTS ---
BG_COLOR = "#242424"      # Deep matte gray background
TEXT_COLOR = "#E0E0E0"    # Soft white text
ACCENT_COLOR = "#3A86FF"  # Modern blue for buttons
FONT = ("Arial", 11, "normal") # Clean, native font
GREEN = "#06D6A0"

class AppInterface:
    def __init__(self, data_manager):
        # Window
        self.window = Tk()
        self.window.title("Password Manager")
        self.window.config(padx=50, pady=50, bg=BG_COLOR)

        # Canvas
        self.canvas = Canvas(width=200, height=200, bg=BG_COLOR, highlightthickness=0)

        #Image(title)
        self.title_icon = PhotoImage(file="title_logo.png")
        self.window.iconphoto(False, self.title_icon)

        #Setting up canvas
        raw_image = Image.open("logo.png")
        resized_image = raw_image.resize((180, 180), Image.Resampling.LANCZOS)
        self.logo_img = ImageTk.PhotoImage(resized_image)
        self.canvas = Canvas(width=200, height=200, bg=BG_COLOR, highlightthickness=0)
        self.logo_image = PhotoImage(file="logo.png")
        self.canvas.create_image(90, 90, image=self.logo_img)
        self.canvas.grid(column=1, row=0)

        #Labels
        self.website_label = Label(text="Website:", bg=BG_COLOR, fg=TEXT_COLOR, font=FONT)
        self.website_label.grid(column=0, row=1, pady=5)

        self.email_user_label = Label(text="Email / Username:", bg=BG_COLOR, fg=TEXT_COLOR, font=FONT)
        self.email_user_label.grid(column=0, row=2, pady=5)

        self.password_label = Label(text="Password:", bg=BG_COLOR, fg=TEXT_COLOR, font=FONT)
        self.password_label.grid(column=0, row=3, pady=5)

        #Entries
        self.website_text_box = Entry(width=33)
        self.website_text_box.grid(column=1, row=1, sticky="w")
        self.website_text_box.focus()
        self.website_text_box.bind("<Return>", self.searching_password)

        self.email_text_box = Entry(width=52)
        self.email_text_box.grid(column=1, row=2, columnspan=2, sticky="w")
        self.email_text_box.insert(0, "typeyourmailhere@gmail.com")

        self.password_text_box = Entry(width=33)
        self.password_text_box.grid(column=1, row=3, sticky="w")
        self.password_text_box.bind("<Return>", self.save_clicked)

        #Buttons
        self.search_button = Button(text="Search", width=14, command=self.searching_password, bg=ACCENT_COLOR, fg="white", font=FONT, relief="flat")
        self.search_button.grid(row=1, column=2, sticky="ew", padx=5)  # sticky="ew" ensures it fills its column space nicely

        self.password_gen_button = Button(text="Generate Password", highlightthickness=0, command=self.generate_password, width=14, bg=ACCENT_COLOR, fg="white", font=FONT, relief="flat")
        self.password_gen_button.grid(column=2, row=3, sticky="ew", padx=5)

        # Increased to match the full width of the entries combined
        self.add_button = Button(text="Add", width=44, command=self.save_clicked, bg=GREEN, fg="black", font=FONT, relief="flat")
        self.add_button.grid(row=4, column=1, columnspan=2, sticky="ew", pady=10)

    def save_clicked(self, event=None):
        # 1. Pulling Data From Entries
        website = self.website_text_box.get()
        email = self.email_text_box.get()
        password = self.password_text_box.get()

        # 2. Using save_data function passing dictionary to Data File
        self.data_manager.save_data(website, email, password)

        # 4. Clear the boxes
        self.website_text_box.delete(0, END)
        self.password_text_box.delete(0, END)

    def generate_password(self):
        generated_password = PasswordGeneration.generate()

        self.password_text_box.delete(0, END)
        self.password_text_box.insert(0, generated_password)

    def searching_password(self, event=None):
        website = self.website_text_box.get()

        if len(website) == 0:
            messagebox.showwarning(title="Error", message="Please enter a website to search.")

            # Ask the storage file for the data
        result = self.data_manager.find_password(website)

        # Show the result to the user
        if result:
            messagebox.showinfo(title=website, message=f"Email: {result['email']}\nPassword: {result['password']}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exist.")
