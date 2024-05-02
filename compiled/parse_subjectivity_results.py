import pandas as pd
import os

# TODO replace with built in func? pandas func?
def average(list):
    '''
    Calcuates the average of a list of floats
    '''
    sum = 0.0
    for val in list:
        sum+=val
    return sum/len(list)

def parse_subjectivity_results():
    df = pd.read_csv("subjectivity-expanded_results.csv")

    # Create dictionary adjective -> list of responses
    responses = {}
    for index, row in df.iterrows():
        adj = row['predicate']
        response = row['response'] 
        if(adj in responses.keys()):
            responses[adj].append(response)
        else:
            responses[adj] = [response]

    subjectivity_average_file = open("subjectivity-average_results.csv", 'w')
    subjectivity_average_file.write(f"Adjective,Subjectivity\n")
    # Create dictionary adjective -> average response
    subjective_values = {}
    for key, value in responses.items():
        subjectivity = average(value)
        subjective_values[key] = subjectivity

        subjectivity_average_file.write(f"{key}, {subjectivity}\n")

    return subjective_values

def get_subjectivity_values():
    if(not os.path.isfile("subjectivity-average_results.csv")):
       return parse_subjectivity_results()
    else:
        df = pd.read_csv("subjectivity-average_results.csv")
        # Create dictionary adjective -> average response
        subjective_values = {}
        for index, row in df.iterrows():
            adjective = row['Adjective']
            subjectivity = row['Subjectivity']
            subjective_values[adjective] = subjectivity

        return subjective_values    
