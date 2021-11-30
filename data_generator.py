import random
import csv

class DataGenerator():
    def __init__(self):
        raw_data=[]
        packed_data=[]

    def generateData():
        for _ in range(50):
            raw_data.append([random.randint(1,30),random.randint(100,200),random.randint(1000,1500)])
    
    def packData():
        if raw_data==[]:
            print("First,you need to generate data")
            return
        for item in raw_data:
            bin_str="010"
            for sayı in item:
                binary=bin(sayı)[2:]
                bin_str=bin_str+"0"*(16-len(binary))+binary
            bin_str+="010"
            packed_data.append(bin_str)

    def unpack():
        #Unpack data : Tanel
        pass

    def extractCsv(file_name,arr):
        with open(file_name,mode="w",newline="") as file:
        writer=csv.writer(file)
        for row in arr:
            print(row)
            if type(row)==str:
                writer.writerow([row])
            else:
                writer.writerow(row)