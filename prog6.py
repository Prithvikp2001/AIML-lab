import pandas as pd
data=pd.read_csv('/home/cn5/Desktop/Dataset/tennis.csv')
te=len(data)
np=len(data.iloc[data[data.columns[-1]]=='yes'])
nn=te-np
training=data.sample(frac=0.75,replace=False)
test=pd.concat([data,training,training]).drop_duplicates(keep=False)
print('training set:',training)
print('\ntest set:',test)
prob={}
for col in training.columns[:-1]:
    prob[col]={}
    vals=set(data[col])
    for val in vals:
        temp=training.loc[training[col]==val]
        pe=len(temp.iloc[temp[temp.columns[-1]]=='yes'])
        ne=len(temp)-pe
        prob[col][val]=[pe/np,ne/nn]
prediction=[]
right_prediction=0
for i in range(len(test)):
    row= test.iloc[i,:]
    fpp=np/te
    fpn=nn/te
    for col in test.columns[:-1]:
        fpp*=prob[col][row[col]][0]
        fpn*=prob[col][row[col]][1]
    if fpp>fpn:
        prediction.append('Yes')
    else:
        prediction.append('No')
    if prediction[-1]==row[-1]:
        right_prediction+=1
print('\nactual values:\n',list(test[test.coloumns[-1]]))
print('\npredicted: ',prediction)
print('\naccuracy: ',right_prediction/len(test))