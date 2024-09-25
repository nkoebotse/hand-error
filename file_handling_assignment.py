# file_handling_assignment.py

def main():
    # File Creation
    try:
        with open('my_file.txt', 'w') as file:
            file.write("Hello, World!\n")
            file.write("The answer to life is 42.\n")
            file.write("Python is great for file handling!\n")
        print("File 'my_file.txt' created and written successfully.")

    except Exception as e:
        print(f"An error occurred during file creation: {e}")

    # File Reading and Display
    try:
        with open('my_file.txt', 'r') as file:
            contents = file.read()
            print("\nContents of 'my_file.txt':")
            print(contents)

    except FileNotFoundError:
        print("Error: 'my_file.txt' not found.")
    except PermissionError:
        print("Error: Permission denied while trying to read 'my_file.txt'.")
    except Exception as e:
        print(f"An error occurred during file reading: {e}")

    # File Appending
    try:
        with open('my_file.txt', 'a') as file:
            file.write("Appending another line of text.\n")
            file.write("Here's a second appended line.\n")
            file.write("And finally, a third appended line.\n")
        print("New lines appended to 'my_file.txt' successfully.")

    except FileNotFoundError:
        print("Error: 'my_file.txt' not found.")
    except PermissionError:
        print("Error: Permission denied while trying to append to 'my_file.txt'.")
    except Exception as e:
        print(f"An error occurred during file appending: {e}")

if __name__ == "__main__":
    main()
