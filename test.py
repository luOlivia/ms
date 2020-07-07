import glob
import os
import fnmatch

matches = []
sep = {}
for root, dirnames, filenames in os.walk('EVTX-ATTACK-SAMPLES'):
    thedir = root.split(os.path.sep)[-1]
    #print(root)
    sep[thedir] = []
    for filename in fnmatch.filter(filenames, '*.evtx'):
        matches.append(os.path.join(root, filename))
        sep[thedir].append(os.path.join(root, filename))

for k,v in sep.items():
    if v != []:
        print("Key is:\n ", k)
        print("files are:\n")
        for f in v:
            print(f)
        print("\n")
        print("\n")

#print(sep["Other"])
#print(matches)


#print(glob.glob("/EVTX-ATTACK-SAMPLES/"))
