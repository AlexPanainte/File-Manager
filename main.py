import functions 
from constants import DIR_TYPES, FILE_EXT_TYPES

if __name__ == '__main__':
    path = input('Insert the path or press Q to exit the program: ')
    if path.upper() == 'Q':
        exit()

    organizer = functions.FileOrganizer(path)
    
    if organizer.path_validation():
        print('The path is valid')
        selected_dirs = organizer.select_folders()
        organizer.create_dirs(selected_dirs)
        organizer.move_files_from_selected_dirs(selected_dirs)
    else:
        print('Invalid path. Exiting the program.')
