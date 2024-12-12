def function_with_closed_file(filename):
    with open(filename, 'w') as file:
        file.write("This is a test.")