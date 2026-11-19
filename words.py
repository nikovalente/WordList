import numpy as np
def num_letters(num_rows,num_columns):
    return 2*num_columns+(num_rows-2)*2

assert num_letters(3,4)==10
print('Checking assertions.')
fhand=np.genfromtxt('loop1.csv',delimiter=',',dtype=str)
assert num_letters(fhand.shape[0],fhand.shape[1])==30
print('Fine')
fhand=np.genfromtxt('loop2.csv',delimiter=',',dtype=str)
assert num_letters(fhand.shape[0],fhand.shape[1])==12
print('Fine')
fhand=np.genfromtxt('loop3.csv',delimiter=',',dtype=str)
assert num_letters(fhand.shape[0],fhand.shape[1])==16
print('Fine')
fhand=np.genfromtxt('loop4.csv',delimiter=',',dtype=str)
assert num_letters(fhand.shape[0],fhand.shape[1])==22
print('Fine')


'''
part 3
'''
data=np.loadtxt('loop4.csv',delimiter=',',dtype=str,encoding='utf8')
words = [] 
rows, columns = data.shape
i=0
while i<columns:
    words.append(data[0,i])
    i+=1
i=1
while i<rows:
    words.append(data[i,columns-1])
    i+=1
i=columns-2
while i>=0:
    words.append(data[rows-1,i])
    i=i-1
i=rows-2
while i>=1:
    words.append(data[i,0])
    i=i-1
assert len(words) == num_letters(rows, columns)
print('Nice')

data=np.loadtxt('loop3.csv',delimiter=',',dtype=str,encoding='utf8')
words = [] 
rows, columns = data.shape
i=0
while i<columns:
    words.append(data[0,i])
    i+=1
i=1
while i<rows:
    words.append(data[i,columns-1])
    i+=1
i=columns-2
while i>=0:
    words.append(data[rows-1,i])
    i=i-1
i=rows-2
while i>=1:
    words.append(data[i,0])
    i=i-1
assert len(words) == num_letters(rows, columns)
print('Nice')

data=np.loadtxt('loop2.csv',delimiter=',',dtype=str,encoding='utf8')
words = [] 
rows, columns = data.shape
i=0
while i<columns:
    words.append(data[0,i])
    i+=1
i=1
while i<rows:
    words.append(data[i,columns-1])
    i+=1
i=columns-2
while i>=0:
    words.append(data[rows-1,i])
    i=i-1
i=rows-2
while i>=1:
    words.append(data[i,0])
    i=i-1
assert len(words) == num_letters(rows, columns)
print('Nice')

data=np.loadtxt('loop1.csv',delimiter=',',dtype=str,encoding='utf8')
words = [] 
rows, columns = data.shape
i=0
while i<columns:
    words.append(data[0,i])
    i+=1
i=1
while i<rows:
    words.append(data[i,columns-1])
    i+=1
i=columns-2
while i>=0:
    words.append(data[rows-1,i])
    i=i-1
i=rows-2
while i>=1:
    words.append(data[i,0])
    i=i-1
assert len(words) == num_letters(rows, columns)
print('Nice')


'''
part 4
'''
data=np.loadtxt('loop4.csv',delimiter=',',dtype=str,encoding='utf8')
rows, columns = data.shape
words_combo=[]
i=0
while i<columns-1:
    words_combo.append(data[0,i]+data[0,i+1])
    i+=1
i=0
while i<rows-1:
    words_combo.append(data[i,columns-1]+data[i+1,columns-1])
    i+=1
i=columns-1
while i>=1:
    words_combo.append(data[rows-1,i]+data[rows-1,i-1])
    i=i-1
i=rows-1
while i>=1:
    words_combo.append(data[i,0]+data[i-1,0])
    i=i-1
print(words_combo)

data=np.loadtxt('loop3.csv',delimiter=',',dtype=str,encoding='utf8')
rows, columns = data.shape
words_combo=[]
i=0
while i<columns-1:
    words_combo.append(data[0,i]+data[0,i+1])
    i+=1
i=0
while i<rows-1:
    words_combo.append(data[i,columns-1]+data[i+1,columns-1])
    i+=1
i=columns-1
while i>=1:
    words_combo.append(data[rows-1,i]+data[rows-1,i-1])
    i=i-1
i=rows-1
while i>=1:
    words_combo.append(data[i,0]+data[i-1,0])
    i=i-1
print(words_combo)

data=np.loadtxt('loop2.csv',delimiter=',',dtype=str,encoding='utf8')
rows, columns = data.shape
words_combo=[]
i=0
while i<columns-1:
    words_combo.append(data[0,i]+data[0,i+1])
    i+=1
i=0
while i<rows-1:
    words_combo.append(data[i,columns-1]+data[i+1,columns-1])
    i+=1
i=columns-1
while i>=1:
    words_combo.append(data[rows-1,i]+data[rows-1,i-1])
    i=i-1
i=rows-1
while i>=1:
    words_combo.append(data[i,0]+data[i-1,0])
    i=i-1
print(words_combo)

data=np.loadtxt('loop1.csv',delimiter=',',dtype=str,encoding='utf8')
rows, columns = data.shape
words_combo=[]
i=0
while i<columns-1:
    words_combo.append(data[0,i]+data[0,i+1])
    i+=1
i=0
while i<rows-1:
    words_combo.append(data[i,columns-1]+data[i+1,columns-1])
    i+=1
i=columns-1
while i>=1:
    words_combo.append(data[rows-1,i]+data[rows-1,i-1])
    i=i-1
i=rows-1
while i>=1:
    words_combo.append(data[i,0]+data[i-1,0])
    i=i-1
print(words_combo)
