#!/usr/bin/env python

import customtkinter as ctk
from contact_book_model import ContactBook
import tkinter.messagebox

class ContactBookApp(ctk.CTk):
    def __init__(self):
        """
        Initializes a new instance of the `ContactBookApp` class.

        This function sets up the initial state of the application by calling the parent class's `__init__` method.
        It also sets the title and geometry of the application window.

        Parameters:
            None

        Returns:
            None
        """
        super().__init__()

        self.title("Contact Book")
        self.geometry("500x400")

        self.contact_book = ContactBook()

        self.create_widgets()

    def create_widgets(self):
        """
        Creates the widgets for the ContactBook application.

        This function creates the widgets for the ContactBook application, including the heading, button frame, scrollable frame, and other UI elements.
        The widgets created include:
            - A label for the heading of the application.
            - A button frame for the application.
            - A button for add contact.
            - A button for refreshing the contacts.
            - A button for exiting the application.
            - A canvas for displaying the contacts.
            - A scrollbar for scrolling the contacts.
            - A label for displaying the number of contacts.

        Parameters:
            None

        Returns:
            None
        """
        self.clear_frame()

        # Heading
        self.label = ctk.CTkLabel(self, text="Contact Book Application", font=("Arial", 20))
        self.label.pack(pady=20)

        # Button Frame
        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.pack(pady=10)

        # Add Contact Button
        self.add_contact_button = ctk.CTkButton(self.button_frame, text="Add New Contact", command=self.add_new_contact)
        self.add_contact_button.grid(row=0, column=0, padx=10)

        # Refresh Button
        self.refresh_button = ctk.CTkButton(self.button_frame, text="Refresh", command=self.create_widgets)
        self.refresh_button.grid(row=0, column=1, padx=10)

        # Exit Button
        self.exit_button = ctk.CTkButton(self.button_frame, text="Exit", command=self.exit_app)
        self.exit_button.grid(row=0, column=2, padx=10)

        # Scrollable Frame for Contacts
        self.contacts_frame = ctk.CTkFrame(self)
        self.contacts_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.canvas = ctk.CTkCanvas(self.contacts_frame)
        self.scrollbar = ctk.CTkScrollbar(self.contacts_frame, orientation="vertical", command=self.canvas.yview)
        self.scrollable_frame = ctk.CTkFrame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Fetch and display contacts
        self.display_contacts()

    def display_contacts(self):
        """
        Displays the contacts in the ContactBook application.

        This function retrieves all the contacts from the ContactBook and displays the contact count and the contacts in the scrollable frame.
        If there are no contacts, it displays a message indicating that there are no contacts available.
        The contacts are sorted by name in ascending order.
        The contact count is displayed using the label `contact_count_label`.
        The contacts are displayed in the scrollable frame using a for loop.
        The contacts are displayed as contact frames with labels and buttons.

        Parameters:
            None

        Returns:
            None
        """

        contacts = self.contact_book.get_all_contacts()
        contact_count = len(contacts)

        # Display contact count
        contact_name = "Contact" if contact_count == 1 else "Contacts"
        self.contact_count_label = ctk.CTkLabel(self.scrollable_frame, text=f"{contact_name}: {contact_count}")
        self.contact_count_label.pack(pady=10)

        if not contacts:
            self.no_contacts_label = ctk.CTkLabel(self.scrollable_frame, text="No contacts available.")
            self.no_contacts_label.pack(pady=10)
            self.add_contact_button = ctk.CTkButton(self.scrollable_frame, text="Add Contact", command=self.add_new_contact)
            self.add_contact_button.pack(pady=10)
        else:
            sorted_contacts = sorted(contacts, key=lambda contact: contact.name.lower())
            for contact in sorted_contacts:
                contact_frame = ctk.CTkFrame(self.scrollable_frame)
                contact_frame.pack(fill="x", pady=2)

                contact_label = ctk.CTkLabel(contact_frame, text=f"{contact.name} - {contact.phone}")
                contact_label.pack(side="left", padx=5)

                view_button = ctk.CTkButton(contact_frame, text="View", command=lambda c=contact: self.view_contact(c))
                view_button.pack(side="right", padx=5)

    def view_contact(self, contact):
        """
        View a contact.

        Args:
            contact (Contact): The contact to view.

        Returns:
            None

        This method clears the current frame and creates a new label and buttons to view the contact.
        The contact details are displayed in a label and the buttons allow the user to update or delete the contact.
        The 'Back' button returns to the main application.

        """
        self.clear_frame()
        self.label = ctk.CTkLabel(self, text="View Contact", font=("Arial", 20))
        self.label.pack(pady=20)

        contact_details = f"Name: {contact.name}\nPhone: {contact.phone}\nEmail: {contact.email}\nAddress: {contact.address}"
        self.contact_label = ctk.CTkLabel(self, text=contact_details)
        self.contact_label.pack(pady=10)

        self.update_button = ctk.CTkButton(self, text="Update", command=lambda: self.update_contact(contact))
        self.update_button.pack(pady=10)

        self.delete_button = ctk.CTkButton(self, text="Delete", command=lambda: self.delete_contact(contact.id))
        self.delete_button.pack(pady=10)

        self.back_button = ctk.CTkButton(self, text="Back", command=self.create_widgets)
        self.back_button.pack(pady=10)

    def update_contact(self, contact):
        """
        Updates the contact information in the ContactBook application.

        This function clears the current frame, displays a label indicating that the contact is being updated,
        and creates entry fields for the contact's name, phone, email, and address. The initial values of the entry
        fields are set to the corresponding values of the provided contact object. The user can then modify the
        values and save the updated contact.

        Parameters:
            contact (Contact): The contact object to be updated.

        Returns:
            None
        """
        self.clear_frame()
        self.label = ctk.CTkLabel(self, text="Update Contact", font=("Arial", 20))
        self.label.pack(pady=20)

        # Use StringVar to set initial values
        self.name_var = ctk.StringVar(value=contact.name)
        self.phone_var = ctk.StringVar(value=contact.phone)
        self.email_var = ctk.StringVar(value=contact.email)
        self.address_var = ctk.StringVar(value=contact.address)

        self.name_entry = ctk.CTkEntry(self, textvariable=self.name_var, placeholder_text="Name")
        self.name_entry.pack(pady=5)
        self.phone_entry = ctk.CTkEntry(self, textvariable=self.phone_var, placeholder_text="Phone")
        self.phone_entry.pack(pady=5)
        self.email_entry = ctk.CTkEntry(self, textvariable=self.email_var, placeholder_text="Email")
        self.email_entry.pack(pady=5)
        self.address_entry = ctk.CTkEntry(self, textvariable=self.address_var, placeholder_text="Address")
        self.address_entry.pack(pady=5)

        self.save_button = ctk.CTkButton(self, text="Save Contact", command=lambda: self.save_updated_contact(contact.id))
        self.save_button.pack(pady=20)

        self.back_button = ctk.CTkButton(self, text="Back", command=lambda: self.view_contact(contact))
        self.back_button.pack(pady=10)

    def save_updated_contact(self, contact_id):
        """
        Save the updated contact information to the ContactBook application.

        This function retrieves the updated contact information from the GUI and updates the contact in the ContactBook.
        The contact is identified by the provided `contact_id`. The function takes the updated name, phone, email, and address
        from the GUI and updates the contact in the ContactBook. After the update is successful, a message box is displayed
        to inform the user of the success. Finally, the function calls `create_widgets()` to refresh the GUI with the updated
        contact information.

        Parameters:
            contact_id (int): The ID of the contact to be updated.

        Returns:
            None
        """
        name = self.name_var.get()
        phone = self.phone_var.get()
        email = self.email_var.get()
        address = self.address_var.get()

        self.contact_book.update_contact(contact_id, name=name, phone=phone, email=email, address=address)
        tkinter.messagebox.showinfo("Success", "Contact updated successfully!")
        self.create_widgets()

    def delete_contact(self, contact_id):
        """
        Deletes a contact from the contact book.

        Args:
            contact_id (int): The ID of the contact to delete.

        Returns:
            None

        This function prompts the user to confirm the deletion of a contact. If the user confirms, the contact is deleted from the contact book and a success message is displayed. Finally, the widgets are recreated to reflect the updated contact list.
        """
        confirm = tkinter.messagebox.askyesno("Confirm", "Are you sure you want to delete this contact?")
        if confirm:
            self.contact_book.delete_contact(contact_id)
            tkinter.messagebox.showinfo("Success", "Contact deleted successfully!")
            self.create_widgets()

    def add_new_contact(self):
        """
        Adds a new contact to the ContactBook application.

        This function clears the current frame and creates entry fields for the contact's name, phone, email, and address.
        The initial values of the entry fields are set to the corresponding values of the provided contact object.
        The user can then modify the values and save the updated contact.

        Parameters:
            None

        Returns:
            None
        """
        self.clear_frame()
        self.label = ctk.CTkLabel(self, text="Add New Contact", font=("Arial", 20))
        self.label.pack(pady=20)

        self.name_entry = ctk.CTkEntry(self, placeholder_text="Name")
        self.name_entry.pack(pady=5)
        self.phone_entry = ctk.CTkEntry(self, placeholder_text="Phone")
        self.phone_entry.pack(pady=5)
        self.email_entry = ctk.CTkEntry(self, placeholder_text="Email")
        self.email_entry.pack(pady=5)
        self.address_entry = ctk.CTkEntry(self, placeholder_text="Address")
        self.address_entry.pack(pady=5)

        self.save_button = ctk.CTkButton(self, text="Save Contact", command=self.save_contact)
        self.save_button.pack(pady=20)

        self.back_button = ctk.CTkButton(self, text="Back", command=self.create_widgets)
        self.back_button.pack(pady=10)

    def save_contact(self):
        """
        Saves a new contact to the ContactBook application.

        This function retrieves the name, phone, email, and address from the GUI entry fields and attempts to add a new contact
        to the ContactBook using the `add_contact` method of the `contact_book` object. If the contact is successfully added,
        a message box is displayed to inform the user of the success. After the contact is added, the `create_widgets` method
        is called to refresh the GUI with the updated contact list.

        If a `ValueError` is raised during the addition of the contact, indicating a duplicate phone number, a message box
        is displayed to inform the user of the error.

        Parameters:
            None

        Returns:
            None
        """
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        try:
            self.contact_book.add_contact(name=name, phone=phone, email=email, address=address)
            tkinter.messagebox.showinfo("Success", "Contact added successfully!")
            self.create_widgets()
        except ValueError as e:
            tkinter.messagebox.showerror("Error", str(e))

    def clear_frame(self):
        """
        Clears the current frame by destroying all child widgets.

        This function iterates over all the children of the frame and destroys each child widget, effectively clearing the frame of all widgets.

        Parameters:
            None

        Returns:
            None
        """
        for widget in self.winfo_children():
            widget.destroy()

    def exit_app(self):
        """
        Exits the application by destroying the root window.

        This function destroys the application by calling the `destroy` method on the root window. It does not take any arguments or return any values.

        Returns:
            None
        """
        self.destroy()

if __name__ == "__main__":
    app = ContactBookApp()
    app.mainloop()

