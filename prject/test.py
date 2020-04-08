import csv
import timeit

def get_data():
	with open('clean_tweet.csv','r',encoding='ISO-8859-1') as csv_file:
		csv_reader = csv.DictReader(csv_file)
		for row in csv_reader:
			yield row
start = timeit.default_timer()
get_data()
stop = timeit.default_timer()
time = stop  - start
print(time)
