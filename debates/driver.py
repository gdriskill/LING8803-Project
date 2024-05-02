import clean_results
import get_aan_phrase
import sys

program = sys.argv[1]

instances = ["2000BushMaster", "2000GoreMaster", "2000McCainMaster", "2004BushMaster", 
            "2004KerryMaster", "2008ClintonMaster", "2008McCainMaster", "2008ObamaMaster",
            "2008RomneyMaster", "2012ObamaMaster", "2012RomneyMaster", "2016ClintonMaster",
            "2016SandersMaster", "2016TrumpMaster"]

for instance in instances:
    print(f"running {instance}")
    if(program == 'get_aan_phrases'):
        get_aan_phrase.main(instance)