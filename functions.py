import os
import shutil
import constants as c

class FileOrganizer:

    def __init__(self, path):
        self.path = path

    def path_validation(self):
        return os.path.isdir(self.path)

    def create_dirs(self, selected_dirs):
        for dir in selected_dirs:
            dir_path = os.path.join(self.path, dir)
            if not os.path.isdir(dir_path):
                os.mkdir(dir_path)

    def list_all_files(self):
        files = [file for file in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, file))]
        return files

    @staticmethod
    def extract_file_extension(file):
        _, extension = os.path.splitext(file)
        return extension.lower()

    def map_extension_to_folder(self):
        extension_mapping = {}
        for i, dir in enumerate(c.DIR_TYPES):
            for ext in c.FILE_EXT_TYPES[i]:
                extension_mapping[ext.lower()] = os.path.join(self.path, dir)
        return extension_mapping

    @staticmethod
    def move_file(source, destination):
        try:
            shutil.move(source, destination)
            return True
        except Exception as e:
            print(f"Error moving {source} to {destination}: {str(e)}")
            return False

    def move_files_from_selected_dirs(self, selected_dirs):
        mapping = self.map_extension_to_folder()
        files = self.list_all_files()

        for file in files:
            file_extension = self.extract_file_extension(file)
            destination = mapping.get(file_extension)
            if destination and destination.split(os.sep)[-1] in selected_dirs:
                source_path = os.path.join(self.path, file)
                destination_path = os.path.join(destination, file)
                self.move_file(source_path, destination_path)

    def select_folders(self):
        print("Select the folders you want to create (enter folder numbers separated by space):")
        for i, folder in enumerate(c.DIR_TYPES):
            print(f"{i + 1}. {folder}")
        
        while True:
            try:
                folder_numbers = input("Enter folder numbers (e.g., '1 3 5') or press Enter to create all: ")
                if not folder_numbers:
                    return c.DIR_TYPES  # Create all folders
                folder_numbers = [int(num) - 1 for num in folder_numbers.split()]
                selected_folders = [c.DIR_TYPES[i] for i in folder_numbers]
                return selected_folders
            except ValueError:
                print("Invalid input. Please enter valid folder numbers or press Enter.")

