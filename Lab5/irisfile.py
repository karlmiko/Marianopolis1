'''Module for accessing the file iris.txt, containing
data used in the classic paper:

 Fisher,R.A. "The use of multiple measurements in taxonomic problems"
 Annual Eugenics, 7, Part II, 179-188 (1936)
'''

N_FIELDS = 5                    # number of items on each row in the file.

# This module will export a function that reads the data file into a list
# of lists.

def latin_name_to_number(name):
    '''This function converts the Latin scientific names in the file
    to a numeric code. The numeric code is used instead of the name
    in order to allow our code to compute correlations of each of
    the four measurements with the species.

    You will use this function in iris_data() to convert the name to
    a number.
    '''
    if name == 'Iris-setosa':
        return 0
    elif name == 'Iris-versicolor':
        return 1
    elif name == 'Iris-virginica':
        return 2
    else:
        print('Unrecognized species:', name)
        return -1

def extract_column(data, col):
    '''Extract a particular column of data from the data object.'''
    result = []
    for fields in data:
        result.append(fields[col])
    return result
    # Preview of a trick we can use in Python - this single line gives
    # The same result as the four lines above, by using something called
    # a 'list comprehension.'
    
    # return [fields[col] for fields in data]

def iris_data():
    '''Opens the data file and converts the contents into a Python "list
    of lists."

    Each data line in the file looks like this:

    5.0 3.3 1.4 0.2 Iris-setosa

    The 5 fields are as follows:
    1. the sepal length in cm
    2. the sepal width in cm
    3. the petal length in cm
    4. the petal width in cm. 
    5. the latin name of the species, either:
        Iris-setosa, Iris-versicolor, or Iris-virginica

    The file may also contain comment lines that begin with a '#'
    character. Your code must ignore these!

    '''
    file = open('iris.txt')
    data = []
    for line in file:

        if line.startswith('#'):
            continue

        fields = list(line.split())

        for i in range(N_FIELDS-1):
            fields[i] = float(fields[i])

        fields[N_FIELDS-1] = latin_name_to_number(fields[N_FIELDS-1])
        data.append(fields)

    file.close()
    return data
