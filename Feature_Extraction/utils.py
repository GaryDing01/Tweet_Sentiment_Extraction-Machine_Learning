# 函数库
import csv

def MaxMinNormalization(x):
	Max=max(x)
	Min=min(x)
	x = (x - Min) / (Max - Min)
	return x

def list2csv(path, result):
	with open(path, mode='w', newline='') as predict_file:
		csv_writer = csv.writer(predict_file)
		for row in range(len(result)):
			csv_writer.writerow(result[row])
