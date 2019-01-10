#LAB 5 FILE

# Import the functions mean and stdev from the builtin statistics module.
# Import the function correlation from the correlation module.
# Import the useful functions and data from the irisfile module.

from irisfile import iris_data, N_FIELDS, extract_column
from statistics import mean, stdev
from correlation import correlation

data = iris_data()
labels = extract_column(data, -1)

column_names = ['sepal length', 'sepal width', 'petal length', 'petal width']

for i in range(N_FIELDS-1):

    dependent_var = extract_column(data, i)
    list_results_of_column = []
    
    #1
    list_results_of_column.append(str(min(dependent_var)))
    #2
    list_results_of_column.append(str(max(dependent_var)))
    #3
    list_results_of_column.append(str(round(mean(dependent_var), 2)))
    #4
    list_results_of_column.append(str(round(stdev(dependent_var), 2)))
    #5
    list_results_of_column.append(str(round(correlation(dependent_var, labels), 4)))

    string_to_print = column_names[i] + ': ' + ' '.join(list_results_of_column)

    print(string_to_print)
