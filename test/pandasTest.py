import pandas as pd
import datetime
# df=pd.DataFrame(data=['20200901'],columns=['date'])
# df['date']=df.to_datetime(df['date'])
row_index = pd.date_range(datetime.datetime(2012, 2, 1), periods=6, freq='BM')
print(row_index)
pass
