def function_with_unclosed_file(filename):
    file = open(filename, 'w')
    file.write("This is a test.")
    # Missing file.close() here!