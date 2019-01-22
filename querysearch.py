import argparse


_parser = argparse.ArgumentParser(description='Search your keyword ex: querycheck.py andsearch general,population,Alzheimer')
_parser.add_argument('searchtype', type=str, help='Search type orsearch and andsearch only ')
_parser.add_argument('Value', type=str, help='Parameter to search')

args = _parser.parse_args()
param =""
finallist=[]
counter = 0

if args.searchtype == "orsearch":
    _prasplit = args.Value.split(",")
    with open("hscic-news", "r") as newsfile:
        ncontent = newsfile.readlines()
        for x in range(len(ncontent)):
            for y in _prasplit:
                if y in ncontent[x]:
                    finallist.append(x)
#    print (list(set(finallist)))
    finallist = list(set(finallist))
    result = " ".join(str(x) for x in finallist)
    print(result)


elif args.searchtype == "andsearch" :
    _prasplit = args.Value.split(",")
    with open("hscic-news", "r") as newsfile:
        ncontent = newsfile.readlines()
        for x in range(len(ncontent)):
            for y in _prasplit:
                if y in ncontent[x]:
                    counter += 1
                else:
                    counter = 0
                if counter == len(_prasplit) :finallist.append(x)

#    print (list(set(finallist)))
    finallist = list(set(finallist))
    result = " ".join(str(x) for x in finallist)
    print(result)


else:
    print ("Please enter only or/and for search type ")
    exit(1)


