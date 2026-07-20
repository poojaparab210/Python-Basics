# Use the value operator in a list comprehension to store lenghts of words from ["python","rock","ai"] in list while filtering out words shorter than 4 charaters

words = ["python","rock","ai"]
lengths = [n for w in words if(n:=len(w))>=4]
print(lengths)