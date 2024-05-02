import spacy
import sys

from parse_subjectivity_results import get_subjectivity_values

def main(instance):
    nlp = spacy.load("en_core_web_sm")

    subjectivity_scores = get_subjectivity_values()
    adjectives = subjectivity_scores.keys()

    in_file = open(f"original_text/{instance}.txt", 'r')
    aan_file = open(f'adj-adj-noun_phrases_{instance}.txt', 'w')
    aan_file2 = open(f'adj-adj-noun_phrases_{instance}-annotated.txt', 'w')

    lines = in_file.readlines()

    for line in lines:
        line = line.strip()
        doc = nlp(line) # NLP spacy object for finding p.o.s.

        for i in range(len(doc)):
            # Iterate through words in the speech
            token = doc[i]
            if(token.text in adjectives): # Check for target adjective
                # Check for adj-adj-noun phrases
                
                if(i < len(doc) - 2):
                    if(doc[i+1].pos_ == 'ADJ' and doc[i+2].pos_ == 'NOUN'):
                        # target adj is in first position
                        aan_file.write(f"{token.text} {doc[i+1].text} {doc[i+2].text}\n")
                        aan_file2.write(f"{token.text} ({token.pos_}) {doc[i+1].text} ({doc[i+1].pos_}) {doc[i+2].text} ({doc[i+2].pos_})\n")

                if(i > 0 and i < len(doc) - 1):
                    if(doc[i-1].pos_ == 'ADJ' and doc[i+1].pos_ == 'NOUN'):
                        # target adj is in second postion
                        aan_file.write(f"{doc[i-1].text} {token.text} {doc[i+1].text}\n")
                        aan_file2.write(f"{doc[i-1].text} ({doc[i-1].pos_}) {token.text} ({token.pos_}) {doc[i+1].text} ({doc[i+1].pos_})\n")


    in_file.close()
    aan_file.close()

if __name__ == '__main__':
    instance = sys.argv[1]  
    main(instance)