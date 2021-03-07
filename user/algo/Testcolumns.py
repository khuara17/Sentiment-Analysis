import pandas
colnames = ['id', 'prices', 'reviews.text', 'reviews.username', 'reviews.title']
data = pandas.read_csv('7817_1.csv', names=colnames)


print(data.shape)

#print(data['id'])

#print(data.iloc[0])

#print(data.iloc[:,0])

print(data.iloc[0:4]) # first five rows of dataframe
#data.iloc[:, 0:2] # first two columns of data frame with all rows
#data.iloc[[0,3,6,24], [0,5,6]] # 1st, 4th, 7th, 25th row + 1st 6th 7th columns.
#data.iloc[0:5, 5:8] # first 5 rows and 5th, 6th, 7th columns of data frame (county -> phone1).