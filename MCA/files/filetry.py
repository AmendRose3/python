def display_content_and_count_lines(file_name):
    line_count = 0  # Initialize line count
    file = None  # Initialize file variable

    try:
        # Open the file in read mode
        file = open(file_name, 'r')
        content = file.read().split(".")  # Split content by periods

        # Iterate over each sentence and display content
        for line in content:
            print(line.strip())  # Print each sentence
            line_count += 1  # Increment line count for each sentence

        print(f'\nTotal number of lines in "{file_name}": {line_count}')

    except FileNotFoundError:
        print(f'Error: File "{file_name}" not found.')
    finally:
        # Close the file if it was opened
        if file:
            file.close()

# Get file name from the user
file_name = input("Enter the file name: ")

# Call the function to display content line by line and count lines
display_content_and_count_lines(file_name)
