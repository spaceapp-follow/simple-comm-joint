import random
import csv
from bitstring import BitArray as B_arr

class DataGenerator():
    def __init__(self):
        self.raw_data=[]
        self.packed_data=[]

    def generateFloatData(self):
        #generate data like [int, int, float]
        for _ in range(50):
            self.raw_data.append([random.randint(1,30),random.randint(100,200),round(random.uniform(0.0,10.0),3)])

    def generateData(self):
        for _ in range(50):
            self.raw_data.append([random.randint(1,30),random.randint(100,200),random.randint(1000,1500)])
    
    def packData(self):
        #takes raw data, converts it into bit strings and puts it in packed_data
        if self.raw_data==[]:
            print("First,you need to generate data")
            return
        self.packed_data.append('1'*54)
        for item in self.raw_data:
            bin_str="010"
            for sayı in item:
                binary=bin(sayı)[2:]
                bin_str=bin_str+"0"*(16-len(binary))+binary
            bin_str+="010"
            self.packed_data.append(bin_str)
        self.packed_data.append('0'*54)
      
    def packFloatData(self):
        #takes raw data which contains float, converts it into bit strings and puts it in packed_data
        if self.raw_data==[]:
            print("First you need to generate data")
            return
        self.packed_data.append('1'*102)
        for item in self.raw_data:
            bin_str="010"
            bin_str+=bin_str+B_arr(int=item[0],length=16).bin+B_arr(int=item[1],length=16).bin+B_arr(float=item[2],length=32).bin+bin_str
            self.packed_data.append(bin_str)
        self.packed_data.append('0'*102)

    def unpack(self):
        #unpacks the data in packed_data, puts the it in raw_data, only for ints
        for i in self.packed_data[1:len(self.packed_data)-1]:
            a=i[3:51]
            y=[]
            t=len(a)//3
            for k in range(3):
                b=a[(k*t):(k+1)*t]
                decimalnum=int(b,2)
                y.append(decimalnum)
            self.raw_data.append(y)

    def extractCsv(self,file_name,arr):
        #extracts an array to a specified csv file
        with open(file_name,mode="w",newline="") as file:
            writer=csv.writer(file)
        for row in arr:
            print(row)
            if type(row)==str:
                writer.writerow([row])
            else:
                writer.writerow(row)