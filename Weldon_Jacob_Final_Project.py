import tkinter as tk
from tkinter import ttk

class PartyApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Party Swipe!")

        # Create the initial screen with two buttons
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

        self.pages = {}

    def party_swipe_main_page(self):
        # Create the initial screen with two buttons
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
        submit_button = ttk.Button(party_goer_frame, text="Submit", command=self.party_swipe_main_page)
        submit_button.pack(side="left", padx=10)

        self.pages["PartyGoerPage"] = (party_goer_frame, "PartyGoerPage")
        self.show_page("PartyGoerPage")

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

        self.pages["PartyHostPage"] = (party_host_frame, "PartyHostPage")
        self.show_page("PartyHostPage")


PartyApp().mainloop()