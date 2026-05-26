import json

DATABASE_FILE = "data.json"

class DataManager:
    def __init__(self, filename=DATABASE_FILE):
        self.filename = filename

    def save_data(self, website: str, email: str, password: str) -> None:
        """Saves the new website credentials to the JSON database."""

        new_data = {
            website:{
                "email": email,
                "password": password
            }
        }

        #Catch Block
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)

        except (FileNotFoundError, json.JSONDecodeError):
            data = {}
        #---------------------------------------------------------#
        # Update and save back to the file
        data.update(new_data)
        with open(self.filename, "w") as file:
                json.dump(data, file, indent=4)

    def find_password(self, website):
        # Catch Block
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)

        except FileNotFoundError:
            return None # The file hasn't been created yet

        # Check if the website exists in our JSON dictionary
        if website in data:
            return data[website]  # Returns the {email: ..., password: ...} dict
        else:
            return None