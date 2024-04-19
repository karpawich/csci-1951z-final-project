from utils import Row, Degree, Gender, Ethnicity, VeteranStatus, Job, WorkAuthorization, Disability, Date, generate_csv
import numpy as np
import pandas as pd
from datetime import date, timedelta
from sklearn.model_selection import ParameterGrid

categorical = {
    "degree": Degree, 
    "gender": Gender, 
    "ethnicity": Ethnicity, 
    "veteran_status": VeteranStatus, 
    "work_authorization": WorkAuthorization,
    "disability": Disability,
    "gpa": np.arange(2,4,0.1)
}

# generates every possible combination of features, leaving school and location as empty strings
def generate_combinations():
    grid = {}
    for key in categorical.keys():
        grid[key] = [e for e in categorical[key]]
    
    X = list(ParameterGrid(grid))
    rows = []
    for x in X:
        jobs = [Job(), Job(), Job()]
        r = Row("", np.round(x["gpa"], 1), x["degree"], "", x["gender"], x["veteran_status"], x["work_authorization"], x["disability"], x["ethnicity"], jobs)
        rows.append(r)
    return rows
    
    
if __name__ == "__main__":
    rows = generate_combinations()
    generate_csv("datasets/synthetic", rows, for_candidate_evaluator=False)