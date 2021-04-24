import numpy as np
import pandas as pd
import json

class DummyFrame:
    def __init__(self):
        self.cols = []
    
    def create_numeric(self,col_name,data_length):
        self.cols.append(self.Numeric(col_name,data_length).publish())
        return
    
    def create_categorical(self,col_name,data_length):
        self.cols.append(self.Categorical(col_name,data_length).publish())
        return
    
    def edit_numeric(self,col_name,series):
        pass
    
    def edit_categorical(self,col_name,series):
        pass
    
    def delete_numeric(self,col_name,data_length):
        pass
    
    def delete_categorical(self,col_name,data_length):
        pass
    
    
    def publish(self):
        self.dummy_frame = pd.DataFrame(self.cols).transpose()
        return self.dummy_frame
        
    class Numeric:
        def __init__(self,col_name,data_length):
            self.line = pd.Series(np.ones(data_length), name = col_name, dtype='float64')
        def publish(self):
            return self.line
    
    class Categorical:
        def __init__(self,col_name,data_length):
            self.line = pd.Series(np.ones(data_length), name = col_name, dtype='float64')
        def publish(self):
            return self.line



