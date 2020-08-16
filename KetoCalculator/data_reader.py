import pandas as pd
class DataReader:
    
    def LoadData(self,name_of_file="food_nutritional_values.csv"):
        self.DataSet = pd.read_csv(name_of_file);
        return self.DataSet

    def AddColumn(self,column_name,list):
         self.DataSet[column_name] = pd.Series(list, index=self.DataSet.index)
         return self.DataSet

    def SaveData(self,name_of_file="recommended.csv"):
         self.DataSet.to_csv(name_of_file, index=False)




