def file_operations():
    """
    This program reads a file, modifies its content, and writes to a new file.
    It includes comprehensive error handling for various file operations.
    """
    
    # Get filename from user with validation
    while True:
        try:
            filename = input("Enter the filename to read: ").strip()
            if not filename:
                raise ValueError("Filename cannot be empty.")
            break
        except ValueError as ve:
            print(f"Error: {ve}")
        except KeyboardInterrupt:
            print("\nOperation cancelled by user.")
            return
        except Exception as e:
            print(f"Unexpected error: {e}")
            return
    
    # Read and process the file
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            
        print(f"Successfully read {len(content)} characters from '{filename}'")
        
        # Modify the content (example: convert to uppercase and add line numbers)
        modified_content = modify_content(content)
        
        # Get output filename from user
        while True:
            try:
                output_filename = input("Enter the output filename: ").strip()
                if not output_filename:
                    raise ValueError("Output filename cannot be empty.")
                if output_filename == filename:
                    raise ValueError("Output filename cannot be the same as input filename.")
                break
            except ValueError as ve:
                print(f"Error: {ve}")
            except KeyboardInterrupt:
                print("\nOperation cancelled by user.")
                return
            except Exception as e:
                print(f"Unexpected error: {e}")
                return
        
        # Write modified content to new file
        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write(modified_content)
            
        print(f"Successfully wrote modified content to '{output_filename}'")
        
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied to read '{filename}'.")
    except UnicodeDecodeError:
        print(f"Error: Could not decode '{filename}'. Try specifying a different encoding.")
    except IsADirectoryError:
        print(f"Error: '{filename}' is a directory, not a file.")
    except OSError as ose:
        print(f"Operating System Error: {ose}")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def modify_content(content):
    """
    Modify the file content according to specific rules.
    This example converts text to uppercase and adds line numbers.
    """
    lines = content.split('\n')
    modified_lines = []
    
    for i, line in enumerate(lines, 1):
        # Add line number and convert to uppercase
        modified_line = f"{i:03d}. {line.upper()}"
        modified_lines.append(modified_line)
    
    return '\n'.join(modified_lines)


def display_file_info(filename):
    """
    Display information about a file if it exists
    """
    import os
    try:
        if os.path.exists(filename):
            size = os.path.getsize(filename)
            print(f"File '{filename}' exists with size {size} bytes")
        else:
            print(f"File '{filename}' does not exist")
    except OSError as ose:
        print(f"Error getting file info: {ose}")


if __name__ == "__main__":
    print("=" * 50)
    print("FILE READ/WRITE PROGRAM WITH ERROR HANDLING")
    print("=" * 50)
    
    # Run the main program
    file_operations()
    
    print("\n" + "=" * 50)
    print("PROGRAM COMPLETED")
    print("=" * 50)