import numpy as np
import pandas as pd


def get_rating_matrix(filename, dtype=np.float32):
    df = pd.read_csv(filename)
    return df.groupby(["source", "target"])["rating"].sum().unstack().fillna(0)

def get_frequent_matrix(filename, dtype=np.float32):
    df = pd.read_csv(filename)
    df["rating"] = 1
    return df.groupby(["source", "target"])["rating"].sum().unstack().fillna(0)
