import os
import sys
import configparser
import shutil
import datetime
from win11toast import toast

def copy_wtf():
    try:
        # Get the directory of the executable
        exe_dir = getattr(sys, '_MEIPASS', os.path.dirname(sys.executable))
        active_dir = os.path.dirname(sys.executable)
        icon_path = os.path.join(exe_dir, 'icon.ico')

        title = 'WTF Folder AutoSaver'
        error_title = 'WTF Folder AutoSaver Error'

        # Validate the directory
        if not os.path.exists(active_dir):
            toast(error_title, 'Unable to determine active directory. Please check your installation.', icon=icon_path)
            return

        # Read options.ini file
        config = configparser.ConfigParser()

        # Read the configuration file
        config_path = os.path.join(active_dir, 'options.ini')
        try:
            config.read(config_path)
        except configparser.Error as e:
            toast(error_title, f'Error reading configuration file ({config_path}): {e}', icon=icon_path)
            return

        # Validate the configuration format
        if not config.has_section('Settings') or not config.has_option('Settings', 'SaveDirectory'):
            toast(error_title, 'Invalid configuration format. Please check your options.ini file.', icon=icon_path)
            return

        # Get the path to the WoW folder from options.ini
        save_directory = config.get('Settings', 'SaveDirectory')
        wtf_folder = os.path.join(save_directory, 'WTF')

        # Check if the WoW folder exists at the given path
        if os.path.exists(wtf_folder):
            # Get the current date for the folder name
            current_date = datetime.datetime.now().strftime('%d-%m-%Y')
            
            # Target for saved WTFs (folder for the current date)
            saved_wtfs_folder = os.path.join(active_dir, 'Saved WTFs', f"WTF_{current_date}")

            # Check if the folder for today's date already exists
            index = 0
            while os.path.exists(saved_wtfs_folder):
                index += 1
                saved_wtfs_folder = os.path.join(active_dir, 'Saved WTFs', f"WTF_{current_date} -{index}")

            # Copy the entire WTF folder into Saved WTFs
            shutil.copytree(wtf_folder, saved_wtfs_folder)

            # Success notification
            toast(title, f'WTF Folder saved successfully as {os.path.basename(saved_wtfs_folder)}.', icon=icon_path)

        else:
            # Trigger notification for error if the WoW folder is not found
            toast(error_title, 'WTF Folder not found. Change the Path to the WoW Folder.', icon=icon_path)
    
    except Exception as e:
        # If an error occurs, show a general error message for debugging
        toast(error_title, f"An error occurred: {str(e)}", icon=icon_path)

copy_wtf()
