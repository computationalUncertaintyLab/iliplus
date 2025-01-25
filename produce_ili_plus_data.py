#mcandrew

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == "__main__":

    #--ILI data
    ili_data = pd.read_csv("ilidata.csv")
    ili_data["week"] = [ int(str(x)[-2:]) for x in ili_data.epiweek]

    #--lab data
    lab_data = pd.read_csv("./clinical_and_public_lab_data__formatted.csv")

    ili_augmented = lab_data.merge(ili_data, on = ["state","epiweek","week"])
    
    ili_augmented["ili_plus"]        = ili_augmented.num_ili*(ili_augmented.percent_positive/100)
    ili_augmented["ili_plus_a"]      = ili_augmented.num_ili*(ili_augmented.percent_a/100)
    ili_augmented["ili_plus_b"]      = ili_augmented.num_ili*(ili_augmented.percent_b/100)

    ili_augmented = ili_augmented.rename(columns = {"region":"location_name"})

    keep = ["location","location_name","season","year","week","epiweek","wili","ili_plus","ili_plus_a","ili_plus_b"] 
    ili_augmented = ili_augmented[keep]

    ili_augmented.to_csv("ili_plus.csv",index=False)
