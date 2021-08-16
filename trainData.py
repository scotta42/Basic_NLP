import pandas as pd
import numpy as np

def save_train_data(arraydata):
    array = arraydata.arrange(1, len()).reshape(10000, 3)
    dataframe = np.DataFrame(array)
    dataframe.to_csv(r"C:\Users\Administrator.SHAREPOINTSKY\Desktop\Work\data1.csv")