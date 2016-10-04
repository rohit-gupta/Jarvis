import csv
import numpy as np

csv.register_dialect('semicolon', delimiter=';', doublequote=True, quotechar='"', quoting=csv.QUOTE_NONNUMERIC, strict=True)
Y = []
with open('final_data.ssv') as csvfile:
	reader = csv.DictReader(csvfile,dialect='semicolon')
	for row in reader:
		y_i = np.array([row['V6'],  row['V7'],  row['V8'],  row['V9'], row['V10'], row['V11'], row['V12'], row['V13'], row['V14'], row['V15'], \
			           row['V16'], row['V17'], row['V18'], row['V19'],row['V20'], row['V21'], row['V22'], row['V23'], row['V24'], row['V25'], row['V26']])
		Y.append(y_i)
	np.savez('genre_vector', np.array(Y))
		