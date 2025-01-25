# Influenza-like illness Plus

Influenza-like illness Plus (ILI+) is defined as the proportion of patients diagnosed with ILI multiplied by the proportion of lab-confirmed tests positive for infliuenza. The data for ILI is collected from particpating Public labs and the data for confirmed positive tests is take from participating clinical labs. See the following link to FluView for more information = [FluView](https://gis.cdc.gov/grasp/fluview/fluportaldashboard.html). 
We used the delphi-epidata package (in Python) to download ILI data and the cdcfluview package (in R) to download the lab data. 

The dataset is updated every Tuesday and is called `iliplus.csv`

# Data dictionary 

| **Term**            | **Description**                                                                                           |
|---------------------|-----------------------------------------------------------------------------------------------------------|
| **location**        | The FIPS (at state level) where data is collected   |
| **location_name**   | The state name where data was collected                   |
| **season**          | The influenza season defined as epidemic week 40 of year Y until epidemic week 20 of year Y+1, or "Offseason" |
| **year**            | The calendar year in which the data is recorded .                                 |
| **week**            | The specific week of the year in which the data is recorded. |
| **epiweek**         | The epidemiological week, a standardized week numbering system used for public health surveillance.         |
| **wili**            | Weighted ILI (Influenza-Like Illness) rate, a measure of flu-like illness activity in the population.       |
| **ili_plus**        | ILI+ |
| **ili_plus_a**      | This is ILI times the proportion of lab posities for influenza A  |
| **ili_plus_b**      | This is ILI times the proportion of lab posities for influenza B         |

# Contact
Please contact mcandrew@lehigh.edu (https://compuncertlab.org) for information. Please submit pull requests to make modifications. 


