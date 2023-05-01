def serialize_list_of_strings(strings, filename):
    with open(filename, 'w') as file:
        for string in strings:
            file.write(string + '\n')

def deserialize_list_of_strings(filename):
    with open(filename, 'r') as file:
        strings = file.read().splitlines()
    return strings



strings = ['banana', 'cherry', 'banana', 'limon']
serialize_list_of_strings(strings, 'filestrings')
print(deserialize_list_of_strings('filestrings'))

