#!/usr/bin/env python
# coding: utf-8

# In[32]:


import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ",")
    csv_headers = next(csvreader)
    
    # Create empty dictionary to hold candidate names & vote tallies
    candidates = {}
    
    # loop through csv to make dictionary entries & tally votes
    for x in csvreader:
        if x[2] not in candidates:
            candidates[x[2]] = 1
        else:
            candidates[x[2]] +=1
    
    # total number of votes cast
    votes = sum(candidates.values())
    
    # finds popular vote winner
    max_votes = max(candidates.values())
    for k,v in candidates.items():
        if v == max_votes:
            key = k
    
    # print stuff
    print("Election Results \n ----------------------------")
    
    print(f"Total Votes: {votes} \n ----------------------------")
    
    # print name, percentage & vote count for each candidate
    for x in candidates:
        print(f"{x}: {round(candidates[x]*100/votes,2)}% ({candidates[x]}) \n")
    
    print(f"---------------------------- \n Winner: {key}")
    
    # create & write textfile
    csvoutput = os.path.join("analysis", "analysis.txt")
    
    with open(csvoutput,"a") as txtfile:
        txtfile.write("Election Results \n ---------------------------- \n")
        txtfile.write(f"Total Votes: {votes} \n ---------------------------- \n")
        for x in candidates:
            txtfile.write(f"{x}: {round(candidates[x]*100/votes,2)}% ({candidates[x]}) \n")
    
        txtfile.write(f"---------------------------- \n Winner: {key}")


# In[73]:


candidates


# In[88]:


counter


# In[6]:


candidates


# In[ ]:




