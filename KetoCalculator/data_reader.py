import pandas as pd
class DataReader:
    
    def LoadData(self,name_of_file="food_nutritional_values.csv"):
        self.DataSet = pd.read_csv(name_of_file);
        return self.DataSet

    def AddColumn(self,df,column_name,list):
         df[column_name] = pd.Series(list, index=df.index)
         return self.DataSet

    def SaveData(self,df,name_of_file="recommended.csv"):
         df.to_csv(name_of_file, index=False)




