import os
import shutil
from colorama import init, Fore

init(autoreset=True)


class DirectoryFileManager:
    def __init__(self):
        self.current_dir = os.getcwd()

    def print_working_directory(self) -> None:
        clear_screen()
        print_manager_name()
        print(f"Current Directory: \n{Fore.GREEN}{self.current_dir}")

    def print_directory_list(self) -> None:
        clear_screen()
        print_manager_name()
        for entry in os.listdir(self.current_dir):
            full_path = os.path.join(self.current_dir, entry)

            if os.path.isdir(full_path):
                count = len(os.listdir(full_path))
                print(f"- {entry} [{count} items]")
            elif os.path.isfile(full_path):
                size = os.path.getsize(full_path)
                print(f"- {entry} [{size} bytes]")
            else:
                print(f"- {entry} [unknown]")

    def create_file(self) -> None:
        """
        Prompts the user to enter a file name and attempts to create the file
        in the current working directory.

        - If the file does not exist, it is created as an empty file.
        - If the file already exists, a message is displayed.
        - Handles permission and unexpected errors gracefully.

        """
        clear_screen()
        print_manager_name()
        file_name = input(
            f"Enter the name of the file you want create (In Current Directory): \n>>> {Fore.BLUE}")
        path: str = os.path.join(self.current_dir, file_name)

        if os.path.exists(path):
            print(f"{Fore.RED}File {file_name} already exists")
            return

        try:
            with open(path, 'x') as file:
                pass
            print(f"{Fore.GREEN}File '{file_name}' successfully created")
        except PermissionError:
            print(f"{Fore.RED}Permission Error! The program lacks the necessary permissions to perform a file or directory operation")
        except Exception as error:
            print(f"{Fore.RED}An error ocured! \n {error}")

    def create_directory(self) -> None:
        """
        Prompts the user to enter a folder name and attempts to create the folder
        in the current working directory.

        - If the folder does not exist, it is created as an empty folder.
        - If the folder already exists, a message is displayed.
        - Handles permission and unexpected errors gracefully.

        """
        clear_screen()
        print_manager_name()
        folder_name = input(
            f"Enter the name of the folder you want create (In Current Directory): \n\n>>> {Fore.BLUE}")
        path: str = os.path.join(self.current_dir, folder_name)

        if os.path.isdir(path):
            print(f"{Fore.RED}Folder {folder_name} already exists")
            return

        try:
            os.mkdir(path)
            print(f"{Fore.GREEN}Folder '{folder_name}' successfully created")
        except PermissionError:
            print(f"{Fore.RED}Permission Error! The program lacks the necessary permissions to perform a file or directory operation")
        except Exception as error:
            print(f"{Fore.RED}An error ocured! \n {error}")

    def remove_file(self) -> None:
        """
        Delete a file from the current directory.

        Prompts for a filename, checks if it exists, and asks for confirmation
        before deleting. Handles permission and other errors gracefully.

        Returns:
            None
        """
        clear_screen()
        print_manager_name()
        file_name = input(
            f"Enter the name of the file you want delete (In Current Directory): \n>>> {Fore.BLUE}")
        path: str = os.path.join(self.current_dir, file_name)

        if not os.path.exists(path):
            print(f"{Fore.RED}File '{file_name}' doesn't exist")
            return

        print(
            f"{Fore.RED}Delete file '{file_name}'? The file is deleted permanently and cannot be recovered (y/n)")
        user_answer = input(f">>> {Fore.BLUE}")
        if user_answer.lower() == 'n':
            print("...")
            return

        try:
            os.remove(path)
            print(f"{Fore.GREEN}File successfully deleted")
        except PermissionError:
            print(f"{Fore.RED}Permission Error! The program lacks the necessary permissions to perform a file or directory operation")
        except Exception as error:
            print(f"{Fore.RED}An error ocured! \n {error}")

    def remove_directory(self) -> None:
        """
        Delete a directory from the current directory.

        Prompts for a directory name, checks if it exists, and asks for confirmation
        before deleting. Handles permission and other errors gracefully.

        Returns:
            None
        """
        clear_screen()
        print_manager_name()
        folder_name = input(
            f"Enter the name of the folder you want delete (In Current Directory): \n\n>>> {Fore.BLUE}")
        path: str = os.path.join(self.current_dir, folder_name)

        if not os.path.isdir(path):
            print(f"{Fore.RED}Folder '{folder_name}' doesn't exist")
            return

        print(
            f"{Fore.RED}Delete folder '{folder_name}'? The folder is deleted permanently and cannot be recovered (y/n)")
        user_answer = input(f">>> {Fore.BLUE}")
        if user_answer.lower() == 'n':
            print("...")
            return

        try:
            if os.listdir(path):
                shutil.rmtree(path)
            else:
                os.rmdir(path)
            print(f"{Fore.GREEN}Folder successfully deleted")
        except PermissionError:
            print(f"{Fore.RED}Permission Error! The program lacks the necessary permissions to perform a file or directory operation")
        except Exception as error:
            print(f"{Fore.RED}An error occurred! \n{error}")

    def rename_file(self) -> None:
        """
        Renames a file in the current directory.

        Prompts the user to enter the name of an existing file and a new name.
        If the file exists, it attempts to rename it.
        Handles errors such as missing files or permission issues.

        Returns:
            None
        """
        clear_screen()
        print_manager_name()
        file_name = input(
            f"Enter the name of the file you want rename (In Current Directory): \n>>> {Fore.BLUE}")
        new_name = input(
            f"{Fore.WHITE}Enter new name for the file: \n>>> {Fore.BLUE}")

        path: str = os.path.join(self.current_dir, file_name)
        new_path: str = os.path.join(self.current_dir, new_name)

        if os.path.exists(new_path):
            print(f"{Fore.YELLOW}A file named '{new_name}' already exists")
            return

        if not os.path.exists(path):
            print(f"{Fore.RED}File '{file_name}' doesn't exists")
            return

        try:
            os.rename(path, new_path)
            print(
                f"{Fore.GREEN}Successfully renamed '{file_name}' to '{new_name}'")
        except PermissionError:
            print(f"{Fore.RED}Permission Error! The program lacks the necessary permissions to perform a file or directory operation")
        except Exception as error:
            print(f"{Fore.RED}An error ocured! \n {error}")

    def rename_directory(self) -> None:
        """
        Renames a directory in the current directory.

        Prompts the user to enter the name of an existing directory and a new name.
        If the directory exists, it attempts to rename it.
        Handles errors such as missing files or permission issues.

        Returns:
            None
        """
        clear_screen()
        print_manager_name()
        folder_name = input(
            f"Enter the name of the folder you want rename (In Current Directory): \n>>> {Fore.BLUE}")
        new_name = input(
            f"Enter new name for the folder: \n>>> {Fore.BLUE}")

        path: str = os.path.join(self.current_dir, folder_name)
        new_path: str = os.path.join(self.current_dir, new_name)

        if os.path.isdir(new_path):
            print(f"{Fore.YELLOW}A folder named '{new_name}' already exists")
            return

        if not os.path.isdir(path):
            print(f"{Fore.RED}Folder '{folder_name}' doesn't exists")
            return

        try:
            os.rename(path, new_path)
            print(
                f"{Fore.GREEN}Successfully renamed '{folder_name}' to '{new_name}'")
        except PermissionError:
            print(f"{Fore.RED}Permission Error! The program lacks the necessary permissions to perform a file or directory operation")
        except Exception as error:
            print(f"{Fore.RED}An error ocured! \n {error}")

    def find_file(self) -> None:
        """
        Searches for files in the current directory that match a given name (partial or full).

        - Prompts the user for a filename or partial name.
        - Lists all files and filters matches (case-insensitive).
        - Displays matching filenames if found.
        - Notifies the user if no matches are found.

        Returns:
            None
        """
        clear_screen()
        print_manager_name()
        file_name = input(
            f"Enter the name of the file you want find (In Current Directory): \n>>> {Fore.BLUE}")
        files = os.listdir(self.current_dir)
        matches = [f for f in files if file_name.lower() in f.lower()]

        if matches:
            print(f"Matches found:")
            for match in matches:
                print(f"{Fore.GREEN} - {match}")
        else:
            print(f"{Fore.RED}No matches found.")

    def find_directory(self) -> None:
        """
        Searches for directory in the current directory that match a given name (partial or full).

        - Prompts the user for a directory name or partial name.
        - Lists all directories and filters matches (case-insensitive).
        - Displays matching directory name if found.
        - Notifies the user if no matches are found.

        Returns:
            None
        """
        clear_screen()
        print_manager_name()
        folder_name = input(
            f"Enter the name of the folder you want find (In Current Directory): \n>>> {Fore.BLUE}")
        folders = os.listdir(self.current_dir)
        matches = [f for f in folders if folder_name.lower() in f.lower()]

        if matches:
            print(f"Matches found:")
            for match in matches:
                print(f"{Fore.GREEN} - {match}")
        else:
            print(f"{Fore.RED}No matches found.")

    def change_directory(self) -> None:
        clear_screen()
        print_manager_name()

        new_path = input(
            f"Enter the full path to change directory:\n>>> {Fore.BLUE}")

        if not os.path.isdir(new_path):
            print(f"{Fore.RED}Path does not exist or is not a directory.")
            return

        try:
            os.chdir(new_path)
            self.current_dir = os.getcwd()
            print(f"{Fore.GREEN}Changed directory to:\n{self.current_dir}")
        except PermissionError:
            print(f"{Fore.RED}Permission denied.")
        except Exception as error:
            print(f"{Fore.RED}An error occurred:\n{error}")


def clear_screen() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def print_manager_name() -> None:
    print(
        f"""{Fore.BLUE}
     _____  ______ __  __                                   
    |  __ \|  ____|  \/  |                                  
    | |  | | |__  | \  / | __ _ _ __   __ _  __ _  ___ _ __ 
    | |  | |  __| | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|
    | |__| | |    | |  | | (_| | | | | (_| | (_| |  __/ |   
    |_____/|_|    |_|  |_|\__,_|_| |_|\__,_|\__, |\___|_|   
                                             __/ |          
                                            |___/           

    """
    )


dfm = DirectoryFileManager()


def main():
    clear_screen()
    while True:
        print(f"{Fore.CYAN}-------- MENU --------")
        print("1. Print Working Directory List")
        print("2. Print Working Directory")
        print("3. Create File")
        print("4. Create Folder")
        print("5. Remove File")
        print("6. Remove Folder")
        print("7. Rename File")
        print("8. Rename Folder")
        print("9. Find File")
        print("10. Find Folder")
        print("11. Change Directory")
        print("12. Exit")

        choice = input(f">>> {Fore.BLUE}")

        match choice:
            case '1':
                print(f"{Fore.CYAN}Choice: Print Directory List")
                dfm.print_directory_list()
            case '2':
                print(f"{Fore.CYAN}Choice: Print Working Directory")
                dfm.print_working_directory()
            case '3':
                print(f"{Fore.CYAN}Choice: Create File")
                dfm.create_file()
            case '4':
                print(f"{Fore.CYAN}Choice: Create Folder")
                dfm.create_directory()
            case '5':
                print(f"{Fore.CYAN}Choice: Remove File")
                dfm.remove_file()
            case '6':
                print(f"{Fore.CYAN}Choice: Remove Folder")
                dfm.remove_directory()
            case '7':
                print(f"{Fore.CYAN}Choice: Rename file")
                dfm.rename_file()
            case '8':
                print(f"{Fore.CYAN}Choice: Rename Folder")
                dfm.rename_directory()
            case '9':
                print(f"{Fore.CYAN}Choice: Find File")
                dfm.find_file()
            case '10':
                print(f"{Fore.CYAN}Choice: Find Directory")
                dfm.find_directory()
            case '11':
                print(f"{Fore.CYAN}Choice: Change Directory")
                dfm.change_directory()
            case '12':
                print("...")
                break
            case _:
                print(f"{Fore.RED}Incorrect Input")


if __name__ == '__main__':
    main()
