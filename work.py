
input_filename = input("Enter the filename to read: ")
try:
    with open(input_filename, 'r') as infile:
        lines = infile.readlines()
except FileNotFoundError:
    print(f"Error: File '{input_filename}' not found.")
    return
except IOError:
    print(f"Error: Could not read file '{input_filename}'.")
    return

modified_lines = [line.upper() for line in lines]

output_filename = input("Enter the filename to write the modified content: ")
try:
    with open(output_filename, 'w') as outfile:
        outfile.writelines(modified_lines)
    print(f"Modified content written to '{output_filename}'.")
except IOError:
    print(f"Error: Could not write to file '{output_filename}'.")

