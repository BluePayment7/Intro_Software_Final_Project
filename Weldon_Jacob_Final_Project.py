import tkinter as tk
from tkinter import ttk, PhotoImage

class PartyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.attributes('-fullscreen',True)
        self.title("Party Swipe!")

        # Configure red and blue color scheme
        self.configure(background="#ff0000")  # Red background
        ttk.Style().configure("TButton", background="#0000ff", foreground="blue")  # Blue buttons
        ttk.Style().configure("TLabel", foreground="blue")  # White labels

        # Create the initial screen with two buttons
        party_type_frame = ttk.Frame(self, padding=20, relief="solid", borderwidth=2)
        party_type_frame.grid(row=0, column=0, sticky="nsew")
        
        party_type_label = ttk.Label(party_type_frame, text="Choose your party type:", font=("Arial", 16, "bold"))
        party_type_label.pack()

        party_type_btns = ttk.Frame(party_type_frame)
        party_type_btns.pack()

        party_goer_btn = ttk.Button(party_type_btns, text="Party Goer", command=self.show_party_goer_page)
        party_goer_btn.pack(side="left", padx=10)

        party_host_btn = ttk.Button(party_type_btns, text="Party Host", command=self.show_party_host_page)
        party_host_btn.pack(side="left", padx=10)

        # Create the exit button frame
        exit_frame = ttk.Frame(self, padding=20)
        exit_frame.grid(row=1, column=0, sticky="se")

        # Add the exit button to the frame
        exit_button = ttk.Button(exit_frame, text="Exit", command=self.destroy)
        exit_button.pack()

        # Create a frame for the image label
        image_frame = ttk.Frame(self)
        image_frame.grid(row=2, column=0)

        # Load the image
        image = PhotoImage(file="cheers.png")

        # Create a Label widget to display the image
        image_label = ttk.Label(image_frame, image=image)
        image_label.image = image  # Keep a reference to avoid garbage collection

        # Add the image label to the frame
        image_label.pack()

        self.pages = {}

    def party_swipe_main_page(self):
        # Create the initial screen 
        party_type_frame = ttk.Frame(self, padding=20)
        party_type_frame.grid(row=0, column=0, sticky="nsew")
        
        party_type_label = ttk.Label(party_type_frame, text="Choose your party type:")
        party_type_label.pack()

        party_type_btns = ttk.Frame(party_type_frame)
        party_type_btns.pack()

        party_goer_btn = ttk.Button(party_type_btns, text="Party Goer", command=self.show_party_goer_page)
        party_goer_btn.pack(side="left", padx=10)

        party_host_btn = ttk.Button(party_type_btns, text="Party Host", command=self.show_party_host_page)
        party_host_btn.pack(side="left", padx=10)

        # Create a frame for the image label
        image_frame = ttk.Frame(self)
        image_frame.grid(row=2, column=0)

        # Load the image
        image = PhotoImage(file="cheers.png")

        # Create a Label widget to display the image
        image_label = ttk.Label(image_frame, image=image)
        image_label.image = image  # Keep a reference to avoid garbage collection

        # Add the image label to the frame
        image_label.pack()

        self.pages = {}

    def show_page(self, page_name):
        # Hide all pages except for the one with the given name
        for page, page_id in self.pages.values():
            if page_name == page_id:
                page.grid(row=0, column=0, sticky="nsew")
            else:
                page.grid_forget()

    def show_party_goer_page(self):
        # Create a page for party goers with input fields
        party_goer_frame = ttk.Frame(self, padding=20)

        name_label = ttk.Label(party_goer_frame, text="Name:")
        name_label.pack()

        name_entry = ttk.Entry(party_goer_frame)
        name_entry.pack()

        age_label = ttk.Label(party_goer_frame, text="Age:")
        age_label.pack()

        age_entry = ttk.Entry(party_goer_frame)
        age_entry.pack()

        location_label = ttk.Label(party_goer_frame, text="Location:")
        location_label.pack()

        location_entry = ttk.Entry(party_goer_frame)
        location_entry.pack()

        picture_label = ttk.Label(party_goer_frame, text="Upload a picture of yourself:")
        picture_label.pack()

        picture_button = ttk.Button(party_goer_frame, text="Browse...")
        picture_button.pack()

        # Back button to return to the Party Swipe Main Page
        back_button = ttk.Button(party_goer_frame, text="Back", command=self.party_swipe_main_page)
        back_button.pack(side="left", padx=10)

        # Submit button to continue
        submit_button = ttk.Button(party_goer_frame, text="Submit", command=self.show_party_goer)
        submit_button.pack(side="left", padx=10)

        # Create a frame for the image label
        image_frame = ttk.Frame(self)
        image_frame.grid(row=2, column=0)

        # Load the image
        image = PhotoImage(file="goer.png")

        # Create a Label widget to display the image
        image_label = ttk.Label(image_frame, image=image)
        image_label.image = image  # Keep a reference to avoid garbage collection

        # Add the image label to the frame
        image_label.pack()

        self.pages["PartyGoerPage"] = (party_goer_frame, "PartyGoerPage")
        self.show_page("PartyGoerPage")

    def show_party_goer(self):
        # Create a page for party goers with input fields
        party_goer_frame2 = ttk.Frame(self, padding=20)


        # Back button to return to the Party Swipe Main Page
        back_button = ttk.Button(party_goer_frame2, text="Back", command=self.show_party_goer_page)
        back_button.pack(side="left", padx=10)

        self.pages["PartyGoerInfo"] = (party_goer_frame2, "PartyGoerInfo")
        self.show_page("PartyGoerInfo")

    def show_party_host_page(self):
        # Create a page for party hosts with input fields
        party_host_frame = ttk.Frame(self, padding=20)

        name_label = ttk.Label(party_host_frame, text="Name:")
        name_label.pack()

        name_entry = ttk.Entry(party_host_frame)
        name_entry.pack()

        age_label = ttk.Label(party_host_frame, text="Age:")
        age_label.pack()

        age_entry = ttk.Entry(party_host_frame)
        age_entry.pack()

        location_label = ttk.Label(party_host_frame, text="Location:")
        location_label.pack()

        location_entry = ttk.Entry(party_host_frame)
        location_entry.pack()

        theme_label = ttk.Label(party_host_frame, text="Party theme:")
        theme_label.pack()

        theme_entry = ttk.Entry(party_host_frame)
        theme_entry.pack()

        venue_label = ttk.Label(party_host_frame, text="Upload photos of the party venue:")
        venue_label.pack()

        venue_button = ttk.Button(party_host_frame, text="Browse...")
        venue_button.pack()

        # Back button to return to the Party Swipe Main Page
        back_button = ttk.Button(party_host_frame, text="Back", command=self.party_swipe_main_page)
        back_button.pack(side="left", padx=10)

        # Submit button to continue
        submit_button = ttk.Button(party_host_frame, text="Submit", command=self.party_swipe_main_page)
        submit_button.pack(side="left", padx=10)

        # Create a frame for the image label
        image_frame = ttk.Frame(self)
        image_frame.grid(row=2, column=0)

        # Load the image
        image = PhotoImage(file="host.png")

        # Create a Label widget to display the image
        image_label = ttk.Label(image_frame, image=image)
        image_label.image = image  # Keep a reference to avoid garbage collection

        # Add the image label to the frame
        image_label.pack()

        self.pages["PartyHostPage"] = (party_host_frame, "PartyHostPage")
        self.show_page("PartyHostPage")




PartyApp().mainloop()