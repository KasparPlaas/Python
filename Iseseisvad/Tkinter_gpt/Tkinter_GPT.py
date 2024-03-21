import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image, ImageTk
import csv


class LemmikloomadeVarjupaik:

    def __init__(self, root):
        self.root = root
        self.root.title("Lemmikloomade Varjupaik")
        self.root.geometry("800x600")

        # Lemmikloomade andmete hoidmine
        self.lemmikloomad = []

        # Laadime eelnevalt salvestatud andmed
        self.load_data()

        # Kasutajaliidese loomine
        self.create_ui()

    def create_ui(self):
        # Peamine raam
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Navigatsiooniraam
        navigation_frame = tk.Frame(main_frame)
        navigation_frame.pack(pady=10)

        # Nupud
        btn_add = ttk.Button(navigation_frame, text="Lisa Lemmikloom", command=self.add_lemmikloom)
        btn_add.grid(row=0, column=0, padx=10)
        btn_view = ttk.Button(navigation_frame, text="Vaata Lemmikloomi", command=self.view_lemmikloomad)
        btn_view.grid(row=0, column=1, padx=10)
        btn_exit = ttk.Button(navigation_frame, text="Välju", command=self.root.quit)
        btn_exit.grid(row=0, column=2, padx=10)

    def add_lemmikloom(self):
        # Funktsioon lemmiklooma lisamiseks
        add_window = tk.Toplevel(self.root)
        add_window.title("Lisa Lemmikloom")

        # Lisainfo väljad
        lbl_name = tk.Label(add_window, text="Nimi:")
        lbl_name.grid(row=0, column=0, padx=10, pady=5)
        entry_name = tk.Entry(add_window)
        entry_name.grid(row=0, column=1, padx=10, pady=5)

        lbl_species = tk.Label(add_window, text="Liik:")
        lbl_species.grid(row=1, column=0, padx=10, pady=5)
        entry_species = tk.Entry(add_window)
        entry_species.grid(row=1, column=1, padx=10, pady=5)

        lbl_age = tk.Label(add_window, text="Vanus:")
        lbl_age.grid(row=2, column=0, padx=10, pady=5)
        entry_age = tk.Entry(add_window)
        entry_age.grid(row=2, column=1, padx=10, pady=5)

        lbl_gender = tk.Label(add_window, text="Sugu:")
        lbl_gender.grid(row=3, column=0, padx=10, pady=5)
        entry_gender = tk.Entry(add_window)
        entry_gender.grid(row=3, column=1, padx=10, pady=5)

        # Pildi laadimine
        def load_image():
            filename = filedialog.askopenfilename(initialdir="/", title="Vali Pilt",
                                                  filetypes=(("Image Files", "*.jpg *.png"), ("All Files", "*.*")))
            entry_image.delete(0, tk.END)
            entry_image.insert(0, filename)

        lbl_image = tk.Label(add_window, text="Pilt:")
        lbl_image.grid(row=4, column=0, padx=10, pady=5)
        entry_image = tk.Entry(add_window)
        entry_image.grid(row=4, column=1, padx=10, pady=5)
        btn_browse = tk.Button(add_window, text="Sirvi...", command=load_image)
        btn_browse.grid(row=4, column=2, padx=5, pady=5)

        # Salvestamise nupp
        btn_save = ttk.Button(add_window, text="Salvesta", command=lambda: self.save_lemmikloom(
            entry_name.get(), entry_species.get(), entry_age.get(), entry_gender.get(), entry_image.get()))
        btn_save.grid(row=5, columnspan=3, padx=10, pady=10)

    def view_lemmikloomad(self):
        # Funktsioon lemmikloomade vaatamiseks
        view_window = tk.Toplevel(self.root)
        view_window.title("Vaatamine")

        tree = ttk.Treeview(view_window, columns=("ID", "Nimi", "Liik", "Vanus", "Sugu", "Pilt"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Nimi", text="Nimi")
        tree.heading("Liik", text="Liik")
        tree.heading("Vanus", text="Vanus")
        tree.heading("Sugu", text="Sugu")
        tree.heading("Pilt", text="Pilt")
        tree.pack(fill="both", expand=True)

        if not self.lemmikloomad:
            lbl_no_data.pack(padx=10, pady=5)
        else:
            for i, lemmikloom in enumerate(self.lemmikloomad):
                # Generate a unique ID for each animal
                animal_id = i + 1  # Increment ID by 1 since IDs start from 1

                # Insert values into the treeview including the generated ID
                tree.insert("", tk.END, iid=i, values=(animal_id, lemmikloom["nimi"], lemmikloom["liik"], lemmikloom["vanus"], lemmikloom["sugu"], "Vaata"))
                tree.tag_bind(i, "<Double-1>", lambda event, row=i: self.show_animal_details(row))

    def show_animal_details(self, row):
        # Funktsioon looma detailide kuvamiseks
        details_window = tk.Toplevel(self.root)
        details_window.title("Looma Detailid")

        lemmikloom = self.lemmikloomad[row]

        lbl_info = tk.Label(details_window, text=f"Nimi: {lemmikloom['nimi']}\nLiik: {lemmikloom['liik']}\nVanus: {lemmikloom['vanus']}\nSugu: {lemmikloom['sugu']}")
        lbl_info.pack(padx=10, pady=5)

        if os.path.exists(lemmikloom["pilt"]):
            image = Image.open(lemmikloom["pilt"])
            image = image.resize((200, 200), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)

            lbl_image = tk.Label(details_window, image=photo)
            lbl_image.image = photo  # Keep reference
            lbl_image.pack()
        else:
            lbl_no_image = tk.Label(details_window, text="Pilti ei leitud")
            lbl_no_image.pack(padx=10, pady=5)
        else:
            for i, lemmikloom in enumerate(self.lemmikloomad):
                # Generate a unique ID for each animal
                animal_id = i + 1  # Increment ID by 1 since IDs start from 1

                # Insert values into the treeview including the generated ID
                tree.insert("", tk.END, iid=i, values=(animal_id, lemmikloom["nimi"], lemmikloom["liik"], lemmikloom["vanus"], lemmikloom["sugu"], "Vaata"))
                tree.tag_bind(i, "<Double-1>", lambda event, row=i: self.show_animal_details(row))

    def show_animal_details(self, row):
        # Funktsioon looma detailide kuvamiseks
        details_window = tk.Toplevel(self.root)
        details_window.title("Looma Detailid")

        lemmikloom = self.lemmikloomad[row]

        lbl_info = tk.Label(details_window, text=f"Nimi: {lemmikloom['nimi']}\nLiik: {lemmikloom['liik']}\nVanus: {lemmikloom['vanus']}\nSugu: {lemmikloom['sugu']}")
        lbl_info.pack(padx=10, pady=5)

        if os.path.exists(lemmikloom["pilt"]):
            image = Image.open(lemmikloom["pilt"])
            image = image.resize((200, 200), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)

            lbl_image = tk.Label(details_window, image=photo)
            lbl_image.image = photo  # Keep reference
            lbl_image.pack()
        else:
            lbl_no_image = tk.Label(details_window, text="Pilti ei leitud")
            lbl_no_image.pack(padx=10, pady=5)
        def view_lemmikloomad(self):
        # Funktsioon lemmikloomade vaatamiseks
        view_window = tk.Toplevel(self.root)
        view_window.title("Vaatamine")

        tree = ttk.Treeview(view_window, columns=("ID", "Nimi", "Liik", "Vanus", "Sugu", "Pilt"), show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Nimi", text="Nimi")
        tree.heading("Liik", text="Liik")
        tree.heading("Vanus", text="Vanus")
        tree.heading("Sugu", text="Sugu")
        tree.heading("Pilt", text="Pilt")
        tree.pack(fill="both", expand=True)

        if not self.lemmikloomad:
            lbl_no_data = tk.Label(view_window, text="Andmeid ei leitud!")
            lbl_no_data.pack(padx=10, pady=5)
        else:
            for i, lemmikloom in enumerate(self.lemmikloomad):
                # Generate a unique ID for each animal
                animal_id = i + 1  # Increment ID by 1 since IDs start from 1

                # Insert values into the treeview including the generated ID
                tree.insert("", tk.END, iid=i, values=(animal_id, lemmikloom["nimi"], lemmikloom["liik"], lemmikloom["vanus"], lemmikloom["sugu"], "Vaata"))
                tree.tag_bind(i, "<Double-1>", lambda event, row=i: self.show_animal_details(row))

    def show_animal_details(self, row):
        # Funktsioon looma detailide kuvamiseks
        details_window = tk.Toplevel(self.root)
        details_window.title("Looma Detailid")

        lemmikloom = self.lemmikloomad[row]

        lbl_info = tk.Label(details_window, text=f"Nimi: {lemmikloom['nimi']}\nLiik: {lemmikloom['liik']}\nVanus: {lemmikloom['vanus']}\nSugu: {lemmikloom['sugu']}")
        lbl_info.pack(padx=10, pady=5)

        if os.path.exists(lemmikloom["pilt"]):
            image = Image.open(lemmikloom["pilt"])
            image = image.resize((200, 200), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)

            lbl_image = tk.Label(details_window, image=photo)
            lbl_image.image = photo  # Keep reference
            lbl_image.pack()
        else:
            lbl_no_image = tk.Label(details_window, text="Pilti ei leitud")
            lbl_no_image.pack(padx=10, pady=5)

    def save_lemmikloom(self, name, species, age, gender, image_path):
        # Funktsioon lemmiklooma salvestamiseks
        if not name or not species or not age or not gender or not image_path:
            messagebox.showerror("Viga", "Palun täitke kõik väljad!")
            return

        lemmikloom = {
            "nimi": name,
            "liik": species,
            "vanus": age,
            "sugu": gender,
            "pilt": image_path
        }
        self.lemmikloomad.append(lemmikloom)
        self.save_data()  # Salvestame uuendatud andmed
        messagebox.showinfo("Info", "Lemmikloom on lisatud!")

    def save_data(self):
        # Salvestame andmed CSV faili
        with open("lemmikloomad.csv", mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["nimi", "liik", "vanus", "sugu", "pilt"])
            writer.writeheader()
            for lemmikloom in self.lemmikloomad:
                writer.writerow(lemmikloom)

    def load_data(self):
        # Laeme andmed CSV failist
        try:
            with open("lemmikloomad.csv", mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.lemmikloomad.append(row)
        except FileNotFoundError:
            # Kui faili pole veel loodud, siis ei tee midagi
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = LemmikloomadeVarjupaik(root)
    root.mainloop()
