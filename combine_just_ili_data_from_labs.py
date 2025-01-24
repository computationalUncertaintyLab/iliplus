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

    pa_ili_augmented = ili_augmented.loc[ili_augmented.location=="42"]

    pa_ili_augmented["num_ili_scaled"] = pa_ili_augmented.num_ili*(pa_ili_augmented.percent_positive/100)
    
    pa_ili_augmented.to_csv("./pa_ili_augmented.csv",index=False)

