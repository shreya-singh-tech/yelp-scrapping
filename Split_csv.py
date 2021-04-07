import pandas as pd


#csv file name to be read in 

in_csv = 'combined_reviews_info.csv'


#get the number of lines of the csv file to be read

number_lines = sum(1 for row in (open(in_csv,encoding='utf-8-sig')))


#size of rows of data to write to the csv, 

#you can change the row size according to your need

rowsize = 1000


#start looping through data writing it to a new file for each set

for i in range(1,number_lines,rowsize):

    df = pd.read_csv(in_csv,nrows = rowsize,skiprows=range(1,i))#skip rows that have been read


    #csv to write data to a new file with indexed name. input_1.csv etc.

    out_csv = 'combined_reviews_info' + str(i) + '.csv'
    df.to_csv(out_csv,index=False,mode='a',chunksize=rowsize,encoding='utf-8-sig')
    #size of data to append for each loop