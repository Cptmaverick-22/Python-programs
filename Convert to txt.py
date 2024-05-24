import os

# Get a list of all the Python files in the current directory
python_files = [f for f in os.listdir('Suggestions') if f.endswith('.py')]

# Convert each Python file to a text file
for python_file in python_files:
    text_file = python_file.replace('.py', '.txt')
    with open(python_file, 'r') as f_in, open(text_file, 'w') as f_out:
        f_out.write(f_in.read())

# Print a message to the user
print('All Python files have been converted to text files.')