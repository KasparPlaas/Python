import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import csv
import os
import shutil
from PIL import Image, ImageTk
from tkinter import font as tkfont


class PetShelterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lemmikloomade Varjupaiga Haldamise Süsteem")

        # Create input fields
        self.name_label = ttk.Label(root, text="Nimi:")
        self.name_entry = ttk.Entry(root)
        self.species_label = ttk.Label(root, text="Liik:")
        self.species_entry = ttk.Entry(root)
        self.age_label = ttk.Label(root, text="Vanus:")
        self.age_entry = ttk.Entry(root)
        self.gender_label = ttk.Label(root, text="Sugu:")
        self.gender_entry = ttk.Entry(root)
        self.picture_button = ttk.Button(root, text="Lisa Pilt", command=self.upload_picture)
        self.picture_panel = ttk.Label(root)

        # Create buttons
        self.add_button = ttk.Button(root, text="Lisa Uus Lemmikloom", command=self.add_pet)
        self.show_detailed_info_button = ttk.Button(root, text="Kuva Lemmikloom", command=self.show_detailed_info)
        self.remove_button = ttk.Button(root, text="Eemalda Valitud Lemmikloom", command=self.remove_pet)
        self.save_button = ttk.Button(root, text="Salvesta", command=self.save_pet_data)
        self.load_button = ttk.Button(root, text="Laadi", command=self.load_pet_data_from_file)
        self.edit_button = ttk.Button(root, text="Edit Animal", command=self.edit_pet)
        self.edit_button.config(state="disabled")  # Initially disable the button

        # Place the input fields and buttons on the grid
        self.picture_panel.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        self.name_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.name_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")
        self.species_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.species_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        self.age_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.age_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")
        self.gender_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.gender_entry.grid(row=4, column=1, padx=10, pady=10, sticky="w")
        self.picture_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
        self.add_button.grid(row=6, column=0, padx=10, pady=10, sticky="w")
        self.show_detailed_info_button.grid(row=6, column=1, padx=10, pady=10, sticky="w")
        self.remove_button.grid(row=7, column=0, padx=10, pady=10, sticky="w")
        self.save_button.grid(row=8, column=0, columnspan=2, padx=10, pady=10)
        self.edit_button.grid(row=7, column=1, padx=10, pady=10, sticky="w")

        # Treeview to display the list of pets
        self.tree = ttk.Treeview(root, columns=('ID', 'Name', 'Species', 'Age', 'Gender'))
        self.tree.heading('#0', text='ID')
        self.tree.heading('ID', text='ID')
        self.tree.heading('Name', text='Nimi')
        self.tree.heading('Species', text='Liik')
        self.tree.heading('Age', text='Vanus')
        self.tree.heading('Gender', text='Sugu')
        self.tree.column('#0', minwidth=0, width=0, stretch=tk.NO)
        self.tree.column('ID', anchor=tk.CENTER, width=50)
        self.tree.column('Name', anchor=tk.CENTER, width=100)
        self.tree.column('Species', anchor=tk.CENTER, width=100)
        self.tree.column('Age', anchor=tk.CENTER, width=50)
        self.tree.column('Gender', anchor=tk.CENTER, width=80)
        self.tree.grid(row=9, column=0, columnspan=2, padx=10, pady=10)

        # Create a temporary directory for storing selected images
        self.temp_dir = os.path.join(os.getcwd(), "temp_pictures")
        if not os.path.exists(self.temp_dir):
            os.makedirs(self.temp_dir)

        # Initialize pet data
        self.pet_data = []
        self.selected_pet_id = None

        # Load pet data from CSV file if it exists
        default_file_path = os.path.join(os.path.dirname(__file__), "andmebaas.csv")
        if os.path.exists(default_file_path):
            self.load_pet_data_from_file(default_file_path)
        else:
            # Create an empty database file if it doesn't exist
            with open(default_file_path, "w", newline="") as file:
                writer = csv.DictWriter(file, fieldnames=["ID", "Name", "Species", "Age", "Gender", "Image_Path"])
                writer.writeheader()

        # Load pet data from the database file
        self.load_pet_data_from_file(default_file_path)  # Fixed method call

    def upload_picture(self):
        # Check if there's an existing image in the temporary directory and remove it
        if hasattr(self, 'picture_panel') and hasattr(self.picture_panel, 'image_path'):
            if os.path.exists(self.picture_panel.image_path):
                os.remove(self.picture_panel.image_path)

        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            # Get the directory where the code is run
            current_directory = os.path.dirname(os.path.abspath(__file__))
            temp_directory = os.path.join(current_directory, "temp_pictures")

            # Check if the temporary directory exists, if not, create it
            if not os.path.exists(temp_directory):
                os.makedirs(temp_directory)

            # Get the filename from the file path
            filename = os.path.basename(file_path)

            # Construct the temporary path
            temp_path = os.path.join(temp_directory, filename)

            # Copy the selected image to the temporary directory
            shutil.copyfile(file_path, temp_path)

            # Display the copied image
            image = Image.open(temp_path)
            resized_image = image.resize((200, 200))  # Resize the image to fit in the label
            self.picture_panel.image = ImageTk.PhotoImage(resized_image)
            self.picture_panel.configure(image=self.picture_panel.image)

            # Store the temporary file path
            self.picture_panel.image_path = temp_path  # Store the temporary file path



    def add_pet(self):
        # Get the values from the input fields
        name = self.name_entry.get()
        species = self.species_entry.get()
        age = self.age_entry.get()
        gender = self.gender_entry.get()
        
        # Validate the input fields
        if not name or not species or not age or not gender:
            messagebox.showerror("Error", "Please enter all the information.")
            return

        # Generate a unique ID for the pet
        if len(self.pet_data) == 0:
            pet_id = 1
        else:
            pet_id = self.pet_data[-1]["ID"] + 1
        
        # Construct the temporary path
        current_directory = os.path.dirname(os.path.abspath(__file__))
        temp_directory = os.path.join(current_directory, "temp_pictures")
        temp_path = os.path.abspath(os.path.join(temp_directory, f"{pet_id}_{name}.jpg"))

        # Check if an image is uploaded
        if hasattr(self, 'picture_panel') and hasattr(self.picture_panel, 'image_path'):
            # Get the temporary image path
            temp_image_path = self.picture_panel.image_path

            # Check if the file exists before moving it
            if os.path.exists(temp_image_path):
                # Move the temporary image to the permanent directory
                current_directory = os.path.dirname(os.path.abspath(__file__))
                target_directory = os.path.join(current_directory, "pildid")
                if not os.path.exists(target_directory):
                    os.makedirs(target_directory)
                target_path = os.path.join(target_directory, f"{pet_id}_{name}.jpg")
                shutil.move(temp_image_path, target_path)

                # Update the image path to the permanent one
                self.picture_panel.image_path = target_path

                # Clear the picture panel on the main menu
                self.picture_panel.destroy()
                self.picture_panel = ttk.Label(self.root)
                self.picture_panel.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
            else:
                messagebox.showerror("Error", "Selected image file not found.")
                return
        else:
            messagebox.showerror("Error", "Please select an image.")
            return

        # Create a new pet dictionary
        new_pet = {
            "ID": pet_id,
            "Name": name,
            "Species": species,
            "Age": age,
            "Gender": gender,
            "Image_Path": target_path  # Store the permanent image file path
        }

        # Append the new pet to the pet data list
        self.pet_data.append(new_pet)

        # Add the new pet to the treeview
        self.tree.insert("", "end", text=pet_id, values=(pet_id, name, species, age, gender))

        # Clear the input fields
        self.clear_input_fields()

        # Display a success message
        messagebox.showinfo("Success", f"Edukalt lisatud looma ID: {pet_id}, nimi: {name}")

    def clear_input_fields(self):
        # Clear the input fields
        self.name_entry.delete(0, tk.END)
        self.species_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.gender_entry.delete(0, tk.END)

    def clear_picture_panel(self):
        # Clear the picture panel on the main menu
        self.picture_panel.configure(image=None)
        self.picture_panel.image_path = None



    def show_detailed_info(self):
        selected_item = self.tree.focus()
        if selected_item:
            pet_id = int(self.tree.item(selected_item, "text"))
            self.selected_pet_id = pet_id  # Update the selected pet ID
            pet = next((p for p in self.pet_data if p["ID"] == pet_id), None)
            if pet:
                detailed_window = tk.Toplevel(self.root)
                detailed_window.title("Pet Details")

                # Create a frame for styling
                frame = ttk.Frame(detailed_window)
                frame.pack(fill="both", expand=True)

                # Add a decorative border
                frame.config(borderwidth=5, relief="groove")
                self.edit_button.config(state="normal")
                # Display the image if available
                if "Image_Path" in pet and pet["Image_Path"]:
                    # Attempt to open the image using the stored path
                    try:
                        image = Image.open(pet["Image_Path"])
                        resized_image = image.resize((200, 200))  # Resize the image
                        photo_image = ImageTk.PhotoImage(resized_image)
                        image_label = ttk.Label(frame, image=photo_image)
                        image_label.image = photo_image
                        image_label.grid(row=0, column=0, columnspan=2, pady=(10, 20), padx=(20, 0))
                    except FileNotFoundError:
                        # Handle the case when the image file is not found
                        print("Image file not found:", pet["Image_Path"])
                else:
                    # Handle the case when the image path is empty or not available
                    print("Image path not available:", pet.get("Image_Path", "N/A"))

                # Create font style for labels and values
                font_style = tkfont.Font(family="Arial", size=12)

                # Display pet information with styled labels and values
                labels_info = [("ID:", str(pet['ID'])), ("Nimi:", pet['Name']), ("Liik:", pet['Species']), ("Vanus:", str(pet['Age'])),
                               ("Sugu:", pet['Gender'])]
                for idx, (label_text, value_text) in enumerate(labels_info, start=1):
                    label = ttk.Label(frame, text=label_text, font=font_style)
                    label.grid(row=idx, column=0, sticky="e", padx=(20, 10), pady=(0, 5))
                    value_label = ttk.Label(frame, text=value_text,
                                            font=(font_style.actual()['family'], font_style.actual()['size'], 'bold'))
                    value_label.grid(row=idx, column=1, sticky="w", padx=(0, 20), pady=(0, 5))

                # Calculate the required width based on the picture size and labels
                required_width = 300  # Default width
                if "Image_Path" in pet and pet["Image_Path"]:
                    required_width = resized_image.width + 55  # Add padding for the labels

                # Calculate the required height based on the number of labels
                required_height = (len(labels_info) * 25) + 310  # Base height + height per row

                # Set the window geometry to fit the contents and move the right edge to the left
                x_coordinate = self.root.winfo_rootx() + self.root.winfo_width() - required_width - 50
                detailed_window.geometry(
                    f"{required_width}x{required_height}+{x_coordinate}+{self.root.winfo_rooty() + 50}")

                # Add a close button
                close_button = ttk.Button(frame, text="Close", command=detailed_window.destroy)
                close_button.grid(row=len(labels_info) + 1, column=0, columnspan=2, pady=(20, 10), padx=(20, 0),
                                   sticky="ew")
            else:
                messagebox.showerror("Error", "Pet not found.")
        else:
            messagebox.showerror("Error", "No pet selected.")
            
    def remove_pet(self):
        # Get the selected item from the treeview
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Error", "Please select a pet.")
            return

        # Get the pet ID from the selected item
        pet_id = int(self.tree.item(selected_item, "text"))

        # Find the pet in the pet data list
        pet = next((p for p in self.pet_data if p["ID"] == pet_id), None)
        if not pet:
            messagebox.showerror("Error", "Pet not found.")
            return

        # Ask for confirmation before deletion
        confirmation = messagebox.askokcancel("Kustutamise kinnitus",
                                               f"Kas olete kindel, et soovite kustutada ID {pet_id} - {pet['Name']}?")
        if not confirmation:
            return

        # Remove the pet from the pet data list
        self.pet_data.remove(pet)

        # Remove the pet from the treeview
        self.tree.delete(selected_item)

        # Disable the edit button after removing the pet
        self.edit_button.config(state="disabled")

        # Remove the pet's image file from the pildid directory
        if "Image_Path" in pet and pet["Image_Path"]:
            image_path = pet["Image_Path"]
            if os.path.exists(image_path):
                os.remove(image_path)
                messagebox.showinfo("Success", f"ID {pet_id} - {pet['Name']} on kustutatud.")
            else:
                messagebox.showwarning("Warning", "Pet image file not found.")
        else:
            messagebox.showwarning("Warning", "Pet image file path not available.")
        
        



    def edit_pet(self):
        selected_item = self.tree.focus()
        if selected_item:
            pet_id = int(self.tree.item(selected_item, "text"))
            pet = next((p for p in self.pet_data if p["ID"] == pet_id), None)
            if pet:
                edit_window = tk.Toplevel(self.root)
                edit_window.title("Edit Pet Details")

                # Create a frame for styling
                frame = ttk.Frame(edit_window)
                frame.pack(fill="both", expand=True)

                # Add a decorative border
                frame.config(borderwidth=5, relief="groove")

                # Define image_label as an instance variable
                self.image_label = None

                # Display the image if available
                if "Image_Path" in pet and pet["Image_Path"]:
                    # Open the image using the stored path
                    image = Image.open(pet["Image_Path"])
                    resized_image = image.resize((200, 200))  # Resize the image
                    photo_image = ImageTk.PhotoImage(resized_image)
                    self.image_label = ttk.Label(frame, image=photo_image)
                    self.image_label.image = photo_image
                    self.image_label.grid(row=0, column=0, columnspan=2, pady=(10, 20), padx=(20, 0))

                # Create font style for labels and values
                font_style = tkfont.Font(family="Arial", size=12)

                # Create input fields for editing pet details
                name_label = ttk.Label(frame, text="Nimi:", font=font_style)
                name_label.grid(row=1, column=0, sticky="e", padx=(20, 10), pady=(0, 5))
                name_entry = ttk.Entry(frame, font=font_style)
                name_entry.insert(0, pet["Name"])
                name_entry.grid(row=1, column=1, sticky="w", padx=(0, 20), pady=(0, 5))

                # Liik field
                species_label = ttk.Label(frame, text="Liik:", font=font_style)
                species_label.grid(row=2, column=0, sticky="e", padx=(20, 10), pady=(0, 5))
                species_entry = ttk.Entry(frame, font=font_style)
                species_entry.insert(0, pet.get("Species", ""))
                species_entry.grid(row=2, column=1, sticky="w", padx=(0, 20), pady=(0, 5))

                # Vanus field
                age_label = ttk.Label(frame, text="Vanus:", font=font_style)
                age_label.grid(row=3, column=0, sticky="e", padx=(20, 10), pady=(0, 5))
                age_entry = ttk.Entry(frame, font=font_style)
                age_entry.insert(0, pet.get("Age", ""))
                age_entry.grid(row=3, column=1, sticky="w", padx=(0, 20), pady=(0, 5))

                # Sugu field
                gender_label = ttk.Label(frame, text="Sugu:", font=font_style)
                gender_label.grid(row=4, column=0, sticky="e", padx=(20, 10), pady=(0, 5))
                gender_entry = ttk.Entry(frame, font=font_style)
                gender_entry.insert(0, pet.get("Gender", ""))
                gender_entry.grid(row=4, column=1, sticky="w", padx=(0, 20), pady=(0, 5))

                # Function to update the image
                def update_image():
                    nonlocal pet
                    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
                    if file_path:
                        # Update the image in the label
                        image = Image.open(file_path)
                        resized_image = image.resize((200, 200))
                        photo_image = ImageTk.PhotoImage(resized_image)
                        self.image_label.configure(image=photo_image)
                        self.image_label.image = photo_image

                        # Update the pet dictionary with the new image path
                        pet["Image_Path"] = file_path

                        # Focus on the editor window
                        edit_window.focus_force()

                # Button to upload a new picture
                picture_button = ttk.Button(frame, text="Change Picture", command=update_image)
                picture_button.grid(row=5, column=0, columnspan=2, pady=(20, 10), padx=(20, 0), sticky="ew")

                # Function to save the edited pet details
                def save_edited_pet():
                    # Get the edited values from the input fields
                    edited_name = name_entry.get()
                    edited_species = species_entry.get()
                    edited_age = age_entry.get()
                    edited_gender = gender_entry.get()

                    # Update the pet's details
                    pet["Name"] = edited_name
                    pet["Species"] = edited_species
                    pet["Age"] = edited_age
                    pet["Gender"] = edited_gender

                    # Close the edit window
                    edit_window.destroy()

                    # Update the treeview with the edited details
                    self.tree.item(selected_item, values=(pet["ID"], edited_name, edited_species, edited_age, edited_gender))

                    # Update the pet data list with the edited pet
                    index = next((index for index, p in enumerate(self.pet_data) if p["ID"] == pet["ID"]), None)
                    if index is not None:
                        self.pet_data[index] = pet

                    # Save the updated pet data to the CSV file
                    self.save_pet_data()

                    # Display a success message
                    messagebox.showinfo("Success", "Pet details updated successfully.")

                # Create a save button to apply the changes
                save_button = ttk.Button(frame, text="Save", command=save_edited_pet)
                save_button.grid(row=6, column=0, columnspan=2, pady=(20, 10), padx=(20, 0), sticky="ew")

                # Create a close button to close the edit window
                close_button = ttk.Button(frame, text="Close", command=edit_window.destroy)
                close_button.grid(row=7, column=0, columnspan=2, pady=(20, 10), padx=(20, 0), sticky="ew")

                # Enable the edit button when a pet is selected
                self.edit_button.config(state="normal")
            else:
                messagebox.showerror("Error", "No pet selected.")

    def save_pet_data(self):
        # Default file path where the CSV file is located
        default_file_path = os.path.join(os.path.dirname(__file__), "andmebaas.csv")

        # Check if the default file path exists
        if os.path.exists(default_file_path):
            file_path = default_file_path
        else:
            # If the default file path doesn't exist, ask for a new file path
            file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])

        if file_path:
            # Save the pet data to the CSV file
            with open(file_path, "w", newline="") as file:
                # Define fieldnames without 'Image_Path'
                fieldnames = ["ID", "Name", "Species", "Age", "Gender"]

                # Create a DictWriter with the modified fieldnames
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()

                # Write rows to the CSV file, excluding 'Image_Path'
                for pet in self.pet_data:
                    pet_data_without_image_path = {key: value for key, value in pet.items() if key != "Image_Path"}
                    writer.writerow(pet_data_without_image_path)

            # Display a success message
            messagebox.showinfo("Success", "Pet data saved successfully.")
       
   
    def load_pet_data_from_file(self, file_path):
        # Clear the existing pet data
        self.pet_data.clear()
        self.tree.delete(*self.tree.get_children())

        # Load the pet data from the CSV file
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                image_path = os.path.join(os.path.dirname(file_path), "pildid", f"{row['ID']}_{row['Name']}.jpg")
                if os.path.exists(image_path):
                    self.pet_data.append({
                        "ID": int(row["ID"]),
                        "Name": row["Name"],
                        "Species": row["Species"],
                        "Age": row["Age"],
                        "Gender": row["Gender"],
                        "Image_Path": image_path
                    })
                else:
                    self.pet_data.append({
                        "ID": int(row["ID"]),
                        "Name": row["Name"],
                        "Species": row["Species"],
                        "Age": row["Age"],
                        "Gender": row["Gender"],
                        "Image_Path": ""  # Empty string if image file not found
                    })
                self.tree.insert("", "end", text=row["ID"], values=(row["ID"], row["Name"], row["Species"], row["Age"], row["Gender"]))

        # Display a success message
        messagebox.showinfo("Success", "Pet data loaded successfully.")

root = tk.Tk()
app = PetShelterApp(root)
root.mainloop()