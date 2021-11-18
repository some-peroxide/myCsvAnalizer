import pandas as pd
 
df = pd.read_csv('D:/subscriber27AUG.csv')
df["timeStamp"] = pd.to_datetime(df["timeStamp"])
 
tempTimeOnlySecond = df["timeStamp"].dt.second
listToMakeTotalElapsedColumn = []
listToMakeTotalMessageColumn = []
listToMakeAverageElapsedColumn = []
sumOfMSToArray = 0
sumOfMessageToArray = 0
tempIndex = 1

for elpsdms in df["elapsed"]:
    if tempIndex >= len(tempTimeOnlySecond): break
    sumOfMSToArray += elpsdms
    sumOfMessageToArray += 1
    if tempTimeOnlySecond[tempIndex - 1] != tempTimeOnlySecond[tempIndex]:
        listToMakeTotalElapsedColumn.append(sumOfMSToArray)
        listToMakeTotalMessageColumn.append(sumOfMessageToArray)
        sumOfMSToArray = 0
        sumOfMessageToArray = 0
    tempIndex += 1
 
for i in range(len(listToMakeTotalElapsedColumn)):
    listToMakeAverageElapsedColumn.append(listToMakeTotalElapsedColumn[i] / listToMakeTotalMessageColumn[i])
 
tempTimeLine = df['timeStamp'].dt.strftime('%Y-%m-%d %H:%M:%S')
tempSet = set(tempTimeLine)
grafanaTimeLine = list(tempSet)
grafanaTimeLine.sort()
grafanaTimeLine.pop()
 
df2 = pd.DataFrame({'Time': grafanaTimeLine,
                  'Average Sent Messages' : listToMakeTotalMessageColumn,
                  'Average Elapsed' : listToMakeAverageElapsedColumn})

df2.to_csv('D:/final-result/resultSubscriber27AUG.csv', index=False)

# ax1 = df2.plot(kind = 'line', x = 'Time', y = 'Average Sent Messages', color = 'blue')
# ax2 = df2.plot(kind = 'line', x = 'Time', y = 'Average Elapsed', secondary_y=True, color = 'green', ax=ax1)
# ax1.set_ylabel('Average Sent Messages')
# ax2.set_ylabel('Average Elapsed(ms)')
