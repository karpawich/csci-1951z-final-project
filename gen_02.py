from utils import Row, Degree, Gender, Ethnicity, VeteranStatus, Job, WorkAuthorization, Disability, Date, generate_csv
import numpy as np
import pandas as pd
from datetime import date, timedelta


# utility function to generate candidates
def generate_candidates(num: int) -> Row:
    rows = []
    for _ in range(num):
        degree = np.random.choice(
            [Degree.BACHELORS, Degree.MASTERS, Degree.PHD], 
            size=1,
        )[0]
        
        gender = np.random.choice(
            [Gender.FEMALE, Gender.MALE, Gender.NOT_APPLICABLE], 
            size=1, 
        )[0]
        
        ethnicity = np.random.choice(
            [Ethnicity.ASIAN,Ethnicity.BLACK,Ethnicity.NATIVE_AMERICAN,Ethnicity.PACIFIC_ISLANDER,Ethnicity.WHITE], 
            size=1, 
        )[0]
        
        veteran_status = np.random.choice(
            [VeteranStatus.YES, VeteranStatus.NO, VeteranStatus.NOT_APPLICABLE],
            size=1,
        )[0]
        
        work_authorization = np.random.choice(
            [WorkAuthorization.NO, WorkAuthorization.YES],
            size=1,
        )[0]
        
        # samples uniformly from 2.0 -> 4.0 in 0.1 increments
        gpa = np.random.choice(
            np.arange(2.0,4.1,0.1),
            size=1
        )[0]
        gpa = np.round(gpa, 1)
        
        # uniform over POSSIBLE_LOCATIONS
        location = ""
        
        # uniform over POSSIBLE_SCHOOLS
        school_name = ""
        
        disability = np.random.choice(
            [Disability.NO, Disability.YES, Disability.NOT_APPLICABLE],
            size=1,
        )[0]
        
        jobs = [Job(), Job(), Job()]
        
        r = Row(school_name, gpa, degree, location, gender, veteran_status, work_authorization, disability, ethnicity, jobs)
        rows.append(r)
    return rows


if __name__ == "__main__":
    # generate 1000 candidates and output to csv
    rows = generate_candidates(1500)
    generate_csv("./datasets/synthetic", rows, for_candidate_evaluator=False)
    print("generated & wrote 1500 candidates to datasets/synthetic.csv")
    