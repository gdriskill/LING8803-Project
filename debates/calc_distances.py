from parse_subjectivity_results import parse_subjectivity_results

# TODO replace with built in func? pandas func?
def average(list):
    '''
    Calcuates the average of a list of floats
    '''
    sum = 0.0
    for val in list:
        sum+=val
    return sum/len(list)

subjectivity_scores = parse_subjectivity_results()
adjectives = subjectivity_scores.keys()
 
in_file = open('adj-adj-noun_phrases_debates-compiled.txt', 'r')
examples_file = open('interesting_examples_debates.txt', 'w')
distances_file = open('distance_scores_debates.csv', 'w')
scores_both_file = open('scores_both_debates.txt', 'w')

positions = {}
lines = in_file.readlines()

for line in lines:
    words = line.strip().split()

    if(words[0] in adjectives):
    # Target adjective in first position (further from noun)
        if(not words[0] in positions.keys()):
            positions[words[0]] = []
        positions[words[0]].append(1)

        if(subjectivity_scores[words[0]] < 0.5):
            examples_file.write(line)



    if(words[1] in adjectives):
    # Target adjective in second position (closer to noun)
        if(not words[1] in positions.keys()):
            positions[words[1]] = []
        positions[words[1]].append(0)
    
        if(subjectivity_scores[words[1]] > 0.5):
            examples_file.write(line)

    
    if(words[0] in adjectives and words[1] in adjectives):
    # Both adjectives are target adjectives
        scores_both_file.write(line)

distances_file.write("adjective, subjectivity, naturalness, count \n")
for key, value in positions.items():
    distance = average(value)
    distances_file.write(f"{key}, {subjectivity_scores[key]}, {distance}, {len(value)} \n")


in_file.close()
examples_file.close()
scores_both_file.close()
distances_file.close()