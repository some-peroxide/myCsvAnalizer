import pandas as pd

loaded_csv = pd.read_csv("D:/test/publisherResult8.csv")
loaded_csv["timeStamp"] = pd.to_datetime(loaded_csv["timeStamp"], unit='ms')
loaded_csv.drop("label", inplace=True, axis=1)
loaded_csv.drop("responseCode", inplace=True, axis=1)
loaded_csv.drop("responseMessage", inplace=True, axis=1)
loaded_csv.drop("threadName", inplace=True, axis=1)
loaded_csv.drop("dataType", inplace=True, axis=1)
loaded_csv.drop("success", inplace=True, axis=1)
loaded_csv.drop("failureMessage", inplace=True, axis=1)
loaded_csv.drop("bytes", inplace=True, axis=1)
loaded_csv.drop("sentBytes", inplace=True, axis=1)
loaded_csv.drop("grpThreads", inplace=True, axis=1)
loaded_csv.drop("allThreads", inplace=True, axis=1)
loaded_csv.drop("URL", inplace=True, axis=1)
loaded_csv.drop("Latency", inplace=True, axis=1)
loaded_csv.drop("IdleTime", inplace=True, axis=1)
loaded_csv.drop("Connect", inplace=True, axis=1)
loaded_csv.sort_values(by='timeStamp', axis=0, inplace=True)

loaded_csv.to_csv("D:/publisher06SEP.csv", index=False)
