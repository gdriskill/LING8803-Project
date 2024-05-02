from parse_subjectivity_results import get_subjectivity_values

def main():
    subjectivity_scores = get_subjectivity_values()

    instance = "all"
    in_file = open(f"scores_both_{instance}.txt", 'r')
    out_file = open(f"subjectivity-difference_{instance}.csv", 'w')

    out_file.write(f"Phrase,Subjectivity Difference\n")

    lines = in_file.readlines()
    for line in lines:
        words = line.strip().split()
        adj1 = words[0]
        adj2 = words[1]

        subjectivity_1 = subjectivity_scores[adj1]
        subjectivity_2 = subjectivity_scores[adj2]

        difference = subjectivity_1 - subjectivity_2

        out_file.write(f"{line.strip()}, {difference}\n")
    
    in_file.close()
    out_file.close()






if __name__ == '__main__':
    main()