import tkinter as tk
from datetime import datetime

class FuneralServiceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Funeral Service App")
        self.current_window = None
        self.submissions = []
        self.set_size(700, 400)
        self.bg_image = tk.PhotoImage(file="C:\\Users\\Francise Grace\\Downloads\\Analgor_application_exam_funeral\\file.png")
        self.bg_label = tk.Label(root, image=self.bg_image)
        self.bg_label.place(relwidth=1, relheight=1)  # Place the background image first
        self.create_widgets()  # Then create widgets

    def set_size(self, width, height):
        self.root.geometry(f"{width}x{height}")

    def create_widgets(self):
        button_width = 8

        self.home_button = tk.Button(self.root, text="Home", command=self.show_home, width=10, bg="gray", fg="white")
        self.home_button.pack(side="top", fill="x", padx=10, pady=5, anchor="center")
        self.add_button_effects(self.home_button)

        self.services_button = tk.Button(self.root, text="Services", command=self.show_services_window, width=button_width, bg="gray", fg="white")
        self.services_button.pack(side="top", fill="x", padx=10, pady=5, anchor="center")
        self.add_button_effects(self.services_button)

        self.handbook_button = tk.Button(self.root, text="Handbook", command=self.show_handbook, width=button_width, bg="gray", fg="white")
        self.handbook_button.pack(side="top", fill="x", padx=10, pady=5, anchor="center")
        self.add_button_effects(self.handbook_button)

        self.about_button = tk.Button(self.root, text="About", command=self.show_about, width=button_width, bg="gray", fg="white")
        self.about_button.pack(side="top", fill="x", padx=10, pady=5, anchor="center")
        self.add_button_effects(self.about_button)

    def add_button_effects(self, button):
        button.bind("<Enter>", self.on_enter)
        button.bind("<Leave>", self.on_leave)

    def on_enter(self, event):
        event.widget.config(font=('Helvetica', 10, 'bold'))

    def on_leave(self, event):
        event.widget.config(font=('Helvetica', 9))

    def hide_current_window(self):
        if self.current_window:
            self.current_window.destroy()

    def show_home(self):
        self.hide_current_window()
        home_window = tk.Toplevel(self.root)
        home_window.title("Home")

        home_canvas = tk.Canvas(home_window, width=700, height=400)
        home_canvas.pack(fill="both", expand=True)

        home_bg_image = tk.PhotoImage(file="C:\\Users\\Francise Grace\\Downloads\\Analgor_application_exam_funeral\\file.png")
        home_canvas.create_image(0, 0, image=home_bg_image, anchor="nw")

        description_text = (
            "Welcome to the Funeral Service App!\n\n"
            "We offer a range of funeral services to help you honor and remember your loved ones. "
            "Here's a brief overview of our main offerings:\n\n"
            "1. Funeral Home Service: Our funeral home service provides a comfortable and dignified "
            "setting for memorial services and gatherings. Our experienced staff will assist you "
            "in planning a meaningful tribute that reflects the life of your loved one.\n\n"
            "2. Burial Service: For families choosing traditional burial, we offer comprehensive "
            "burial services to ensure that your loved one is laid to rest with care and respect. "
            "From coordinating with cemeteries to arranging graveside ceremonies, we are here to "
            "support you every step of the way.\n\n"
            "3. Cremation Service: Cremation provides a flexible and environmentally-friendly "
            "option for honoring your loved one's wishes. Our cremation services include personalized "
            "memorial ceremonies and assistance with scattering or interring ashes as desired.\n\n"
            "Our dedicated team is committed to providing compassionate support and guidance "
            "during this difficult time. Please explore our services and feel free to reach out "
            "with any questions or concerns."
        )
        description_label = tk.Label(home_window, text=description_text, bg="gray", fg="white", justify="left", wraplength=650)
        home_canvas.create_window(350, 200, window=description_label)

        back_button = tk.Button(home_window, text="Back", command=self.navigate_back, bg= "gray", fg= "white")
        home_canvas.create_window(350, 370, window=back_button)  # Adjusted y-coordinate for the back button
        self.add_button_effects(back_button)

        self.current_window = home_window
        self.current_window.bg_image = home_bg_image  # Keep a reference to avoid garbage collection

    def show_services_window(self):
        self.hide_current_window()
        services_window = tk.Toplevel(self.root)
        services_window.title("Services")
        self.set_size(700, 400)
    
        services_canvas = tk.Canvas(services_window, width=700, height=400)
        services_canvas.pack(fill="both", expand=True)

        services_bg_image = tk.PhotoImage(file="C:\\Users\\Francise Grace\\Downloads\\Analgor_application_exam_funeral\\file.png")
        services_canvas.create_image(0, 0, image=services_bg_image, anchor="nw")

        services = [
            "Funeral Home Service",
            "Burial Service",
            "Cremation Service"
        ]

        y_position = 100  # Initial y-coordinate for the buttons
        for service in services:
            service_button = tk.Button(services_window, text=service, command=lambda s=service: self.show_service_form_window(s, services_window), width=20, bg="gray", fg="white")
            services_canvas.create_window(350, y_position, window=service_button)  # Center the buttons horizontally
            self.add_button_effects(service_button)
            y_position += 50  # Increment y-coordinate for the next button

        back_button = tk.Button(services_window, text="Back", command=lambda: (services_window.destroy(), self.navigate_back()), bg="gray", fg="white")
        services_canvas.create_window(350, y_position + 50, window=back_button)
        self.add_button_effects(back_button)

        self.current_window = services_window
        self.current_window.bg_image = services_bg_image


    def show_service_form_window(self, service, services_window):
        services_window.withdraw()

        service_form_window = tk.Toplevel(self.root)
        service_form_window.title(f"{service} Form")

        service_label = tk.Label(service_form_window, text=f"{service} Form:")
        service_label.pack(pady=10)

        name_label = tk.Label(service_form_window, text="Full Name of the Deceased: ")
        name_label.pack()
        name_entry = tk.Entry(service_form_window)
        name_entry.pack()

        date_of_birth_label = tk.Label(service_form_window, text="Date of Birth (YYYY-MM-DD): ")
        date_of_birth_label.pack()
        date_of_birth_entry = tk.Entry(service_form_window)
        date_of_birth_entry.pack()

        date_of_death_label = tk.Label(service_form_window, text="Date of Death (YYYY-MM-DD): ")
        date_of_death_label.pack()
        date_of_death_entry = tk.Entry(service_form_window)
        date_of_death_entry.pack()

        gender_label = tk.Label(service_form_window, text="Gender: ")
        gender_label.pack()
        gender_entry = tk.Entry(service_form_window)
        gender_entry.pack()

        next_of_kin_name_label = tk.Label(service_form_window, text="Name of Kin: ")
        next_of_kin_name_label.pack()
        next_of_kin_name_entry = tk.Entry(service_form_window)
        next_of_kin_name_entry.pack()

        relationship_to_deceased_label = tk.Label(service_form_window, text="Relationship to Deceased: ")
        relationship_to_deceased_label.pack()
        relationship_to_deceased_entry = tk.Entry(service_form_window)
        relationship_to_deceased_entry.pack()

        next_of_kin_contact_label = tk.Label(service_form_window, text="Kin Contact Information: ")
        next_of_kin_contact_label.pack()
        next_of_kin_contact_entry = tk.Entry(service_form_window)
        next_of_kin_contact_entry.pack()

        service_location_label = tk.Label(service_form_window, text="Service Location: ")
        service_location_label.pack()
        service_location_entry = tk.Entry(service_form_window)
        service_location_entry.pack()

        casket_or_urn_choice_label = tk.Label(service_form_window, text="Choice of Casket or Urn: ")
        casket_or_urn_choice_label.pack()
        casket_or_urn_choice_entry = tk.Entry(service_form_window)
        casket_or_urn_choice_entry.pack()

        service_date_label = tk.Label(service_form_window, text="Service date: ")
        service_date_label.pack()
        service_date_label_entry = tk.Entry(service_form_window)
        service_date_label_entry.pack()

        submit_button = tk.Button(service_form_window, text="Submit", command=lambda: self.submit_form(service,
                                                                                                      name_entry.get(),
                                                                                                      date_of_birth_entry.get(),
                                                                                                      date_of_death_entry.get(),
                                                                                                      gender_entry.get(),
                                                                                                      next_of_kin_name_entry.get(),
                                                                                                      relationship_to_deceased_entry.get(),
                                                                                                      next_of_kin_contact_entry.get(),
                                                                                                      service_location_entry.get(),
                                                                                                      casket_or_urn_choice_entry.get(),
                                                                                                      service_date_label_entry.get(),
                                                                                                      service_form_window), width=10)
        submit_button.pack(pady=10)
        self.add_button_effects(submit_button)

        back_button = tk.Button(service_form_window, text="Back", command=lambda: (service_form_window.destroy(), self.navigate_back()), width=10)
        back_button.pack(pady=5)
        self.add_button_effects(back_button)

        self.current_window = service_form_window

    def submit_form(self, service, name, date_of_birth, date_of_death, gender, next_of_kin_name,
                    relationship_to_deceased, next_of_kin_contact, service_location,
                    casket_or_urn_choice, service_date, service_form_window):
        submission_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        submission = {
            "name": name,
            "date_of_birth": date_of_birth,
            "date_of_death": date_of_death,
            "gender": gender,
            "next_of_kin_name": next_of_kin_name,
            "relationship_to_deceased": relationship_to_deceased,
            "next_of_kin_contact": next_of_kin_contact,
            "service_location": service_location,
            "casket_or_urn_choice": casket_or_urn_choice,
            "submission_time": submission_time,
            "service_date": service_date
        }
        self.submissions.append(submission)
        self.generate_handbook_entry(submission)
        service_form_window.destroy()

    def generate_handbook_entry(self, submission):
        with open("funeral_handbook.txt", "a") as file:
            file.write(f"Name: {submission['name']}\n")
            file.write(f"Date of Birth: {submission['date_of_birth']}\n")
            file.write(f"Date of Death: {submission['date_of_death']}\n")
            file.write(f"Gender: {submission['gender']}\n")
            file.write(f"Name of Kin: {submission['next_of_kin_name']}\n")
            file.write(f"Relationship to Deceased: {submission['relationship_to_deceased']}\n")
            file.write(f"Kin Contact Information: {submission['next_of_kin_contact']}\n")
            file.write(f"Service Location: {submission['service_location']}\n")
            file.write(f"Choice of Casket or Urn: {submission['casket_or_urn_choice']}\n")
            file.write(f"Submission Time: {submission['submission_time']}\n")
            file.write(f"Service Date: {submission['service_date']}\n")
            file.write("\n")

    def search_handbook(self, search_term):
        results = []
        with open("funeral_handbook.txt", "r") as file:
            entries = file.read().strip().split("\n\n")

        for entry in entries:
            lines = entry.split("\n")
            name_line = next((line for line in lines if line.startswith("Name:")), None)
            if name_line:
                name = name_line.split("Name: ")[1]
                if self.is_name_close(name, search_term):
                    results.append(entry)

        if results:
            self.display_results(results)
        else:
            self.display_results(["No matching entries found."])

    def is_name_close(self, name, search_term):
        # Check for exact or partial match
        if search_term.lower() in name.lower():
            return True

        # Calculate Levenshtein distance for fuzzy matching
        distance = self.levenshtein_distance(name.lower(), search_term.lower())
        return distance <= 3  # Adjust the threshold as needed

    def levenshtein_distance(self, s1, s2):
        if len(s1) < len(s2):
            return self.levenshtein_distance(s2, s1)

        if len(s2) == 0:
            return len(s1)

        previous_row = range(len(s2) + 1)
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row

        return previous_row[-1]

    def display_results(self, results):
        self.hide_current_window()
        results_window = tk.Toplevel(self.root)
        results_window.title("Search Results")

    # Background image
        results_bg_image = tk.PhotoImage(file="C:\\Users\\Francise Grace\\Downloads\\Analgor_application_exam_funeral\\file.png")
        results_canvas = tk.Canvas(results_window, width=700, height=400)
        results_canvas.pack(fill="both", expand=True)
        results_canvas.create_image(0, 0, image=results_bg_image, anchor="nw")

        y_position = 150  # Initial y-coordinate for the results
        if results:
            for result in results:
                result_label = tk.Label(results_window, text=result, bg="gray", fg="white", wraplength=600, justify="left")
                results_canvas.create_window(350, y_position, window=result_label)  # Center the labels horizontally
                y_position += result_label.winfo_reqheight() + 20  # Increment y-coordinate for the next label
        else:
            no_results_label = tk.Label(results_window, text="No matching entries found.", bg="gray", fg="white")
            results_canvas.create_window(350, y_position, window=no_results_label)  # Center the label horizontally
            y_position += no_results_label.winfo_reqheight() + 20  # Increment y-coordinate for the next label

        back_button = tk.Button(results_window, text="Back", command=self.navigate_back, width=10, bg="gray", fg="white")
        results_canvas.create_window(350, y_position, window=back_button)  # Adjusted y-coordinate for the back button
        self.add_button_effects(back_button)

        self.current_window = results_window
        self.current_window.bg_image = results_bg_image  # Keep a reference to avoid garbage collection

    def show_handbook(self):
        self.hide_current_window()
        handbook_window = tk.Toplevel(self.root)
        handbook_window.title("Handbook")

        # Get the size of the service window
        services_window_size = (700, 400)

    # Set the size of the handbook window to match the size of the service window
        handbook_window.geometry(f"{services_window_size[0]}x{services_window_size[1]}")

        search_label = tk.Label(handbook_window, text="Search by Name:")
        search_label.pack(pady=10)
        search_entry = tk.Entry(handbook_window)
        search_entry.pack()
        search_entry.bind("<KeyRelease>", lambda event: self.show_suggestions(event, search_entry.get()))

        search_button = tk.Button(handbook_window, text="Search", command=lambda: self.search_handbook(search_entry.get()), width=10)
        search_button.pack(pady=10)
        self.add_button_effects(search_button)

        self.suggestions_listbox = tk.Listbox(handbook_window)
        self.suggestions_listbox.pack(pady=10)

        back_button = tk.Button(handbook_window, text="Back", command=self.navigate_back, width=10)
        back_button.pack(pady=5)
        self.add_button_effects(back_button)

        self.current_window = handbook_window

    def show_suggestions(self, event, search_term):
        suggestions = self.get_suggestions(search_term)
        self.suggestions_listbox.delete(0, tk.END)
        for suggestion in suggestions:
            self.suggestions_listbox.insert(tk.END, suggestion)

    def get_suggestions(self, search_term):
        suggestions = []
        with open("funeral_handbook.txt", "r") as file:
            entries = file.read().strip().split("\n\n")

        for entry in entries:
            lines = entry.split("\n")
            name_line = next((line for line in lines if line.startswith("Name:")), None)
            if name_line:
                name = name_line.split("Name: ")[1]
                if search_term.lower() in name.lower() or self.levenshtein_distance(name.lower(), search_term.lower()) <= 3:
                    suggestions.append(name)

        return suggestions

    def show_about(self):
        self.hide_current_window()
        about_window = tk.Toplevel(self.root)
        about_window.title("About")

    # Set up a canvas with gray background
        about_canvas = tk.Canvas(about_window, width=700, height=400, bg="gray")
        about_canvas.pack(fill="both", expand=True)

        about_text = (
            "About Funeral Service App\n\n"
            "Version: 1.0\n\n"
            "Developed by: [Francise Grace E. Gabriel and MA. Lykha Margarette Salustiano]\n\n"
            "This application helps users manage funeral services and keeps a record of service details in the funeral handbook."
        )
        about_label = tk.Label(about_canvas, text=about_text, bg="gray", fg="white")
        about_label.place(relx=0.5, rely=0.5, anchor="center")

        back_button = tk.Button(about_canvas, text="Back", command=self.navigate_back, width=10, bg="gray", fg="white")
        back_button.place(relx=0.5, rely=0.9, anchor="center")
        self.add_button_effects(back_button)

        self.current_window = about_window

    def navigate_back(self):
        if self.current_window == self.root:  
            self.hide_current_window()  
        elif self.current_window and self.current_window.winfo_exists():  # Check if window exists
            if self.current_window.title() == "Home" or self.current_window.title() == "Services":  # Check for Home or Services window
                self.hide_current_window()
            else:
                self.hide_cu
