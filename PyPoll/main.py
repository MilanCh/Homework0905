import csv
import os



file_path=os.path.join("election_data.csv")

with open(file_path,newline="") as data_file:
    csvreader=csv.reader(data_file,delimiter=",")
    next(csvreader)
    i=0
    Votes=[] 
    for row in csvreader:
         Votes.append(row[2])
    
    f=open('election_result.txt','w')

    print("Election Results")
    f.write("Election Results\n")
    print("------------------")
    f.write("------------------\n")
    total=len(Votes)
    print("Total Votes:{}".format(total))
    f.write("Total Votes:{}\n".format(total))
    print("------------------")
    f.write("------------------\n")
    candidates = set(Votes)
    print(f"candidates: {candidates}")
    f.write(f"candidates: {candidates}\n")
    
    winner=list(candidates)[0]
    i0=Votes.count(winner)
    for name in candidates:
        i=Votes.count(name)
        i1=i/total
        print(f"{name}: "+ "{0:.000%}".format(i1)+f" ({i})")
        f.write(f"{name}: "+ "{0:.000%}".format(i1)+f" ({i})\n")
        if i>i0:
            winner=name
            i0=i
    print("------------------")
    f.write("------------------\n")
    print(f"Winner:  {winner}")
    f.write(f"Winner:  {winner}\n")
    print("------------------")
    f.write("------------------\n")
    f.close()