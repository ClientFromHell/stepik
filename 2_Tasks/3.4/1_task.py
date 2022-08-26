import csv, pprint

crime_dictionary = {}
sorted_dict = {}

with open('Crimes.csv', 'r') as cfile:
    line = csv.reader(cfile)
    for l in line:
        if l[5] in crime_dictionary:
            crime_dictionary[l[5]] += 1
        else:
            crime_dictionary[l[5]] = 0

sorted_keys = sorted(crime_dictionary, key=crime_dictionary.get, reverse=True)

for i in sorted_keys:
    sorted_dict[i] = crime_dictionary[i]

print(sorted_dict)

pprint.pprint(crime_dictionary)
