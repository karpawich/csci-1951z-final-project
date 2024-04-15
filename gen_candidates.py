from gen_utils import Row, Degree, Gender, Ethnicity, VeteranStatus, Job, WorkAuthorization, Disability, Date, generate_csv
import numpy as np
import pandas as pd
from datetime import date, timedelta

def random_date(start_date: date, end_date: date) -> date:
    # Calculate the range in days
    delta = (end_date - start_date).days

    # Generate a random number of days within the range
    random_days = np.random.randint(0, delta)

    # Add the random number of days to the start_date
    random_date = start_date + timedelta(days=random_days)

    return random_date


# utility function to generate candidates
def generate_candidates(num: int) -> Row:
    POSSIBLE_LOCATIONS = ["Miami", "Boston", "Providence", "San Francisco", "New York City"]
    POSSIBLE_SCHOOLS = ["Providence University", "State Providence College", "Providence School"]
    POSSIBLE_JOBS = ["Teaching Assistant", "Data Scientist", "Junior SWE", "Senior SWE", "Lawyer"]
    
    rows = []
    for i in range(num):
    
        degree = np.random.choice([Degree.BACHELORS, Degree.MASTERS, Degree.PHD], 
                                size=1, 
                                p=[0.5, 0.3, 0.2])[0]
        
        gender = np.random.choice([Gender.FEMALE, Gender.MALE, Gender.NOT_APPLICABLE], 
                                size=1, 
                                p=[0.49,0.48,0.03])[0]
        
        ethnicity = np.random.choice([Ethnicity.ASIAN,Ethnicity.BLACK,Ethnicity.NATIVE_AMERICAN,Ethnicity.PACIFIC_ISLANDER,Ethnicity.WHITE], 
                                    size=1, 
                                    p=[0.15,0.2,0.05,0.05,0.55])[0]
        
        veteran_status = np.random.choice([VeteranStatus.YES, VeteranStatus.NO, VeteranStatus.NOT_APPLICABLE],
                                        size=1,
                                        p=[0.2,0.7,0.1])[0]
        
        work_authorization = np.random.choice([WorkAuthorization.NO, WorkAuthorization.YES],
                                              size=1,
                                              p=[0.2, 0.8])[0]
        
        # samples uniformly from 2.0 -> 4.0 in 0.1 increments
        gpa = np.random.choice(np.arange(2.0,4.1,0.1),
                            size=1,)[0]
        gpa = np.round(gpa, 1)
        
        
        # uniform over POSSIBLE_LOCATIONS
        location = np.random.choice(POSSIBLE_LOCATIONS,
                                    size=1)[0]
        
        # uniform over POSSIBLE_SCHOOLS
        school_name = np.random.choice(POSSIBLE_SCHOOLS,
                                    size=1)[0]
        
        disability = np.random.choice([Disability.NO, Disability.YES, Disability.NOT_APPLICABLE],
                                    size=1,
                                    p=[0.8,0.1,0.1])[0]
        
        jobs = []
        num_jobs = np.random.randint(4)
        
        last_date = date(2024, 4, 1)
        longest_job_weeks = 52 * 10
        longest_gap_weeks = 52
        for j in range(3):
            if j >= num_jobs:
                jobs.append(Job())
                continue
                
            end = random_date(last_date - timedelta(weeks=longest_gap_weeks), last_date)
            start = random_date(end - timedelta(weeks=longest_job_weeks), last_date - timedelta(weeks=13))
            role = np.random.choice(POSSIBLE_JOBS, size=1)[0]
            
            start = Date(month=start.month, day=start.day) # ? the day might be a year?
            end = Date(month=end.month, day=end.day)
            
            jobs.append(Job(role, start, end))
        
        r = Row(school_name, gpa, degree, location, gender, veteran_status, work_authorization, disability, ethnicity, jobs)
        rows.append(r)
    return rows


if __name__ == "__main__":
    # generate 1000 candidates and output to csv
    rows = generate_candidates(10000)
    generate_csv("./datasets/synthetic", rows, for_candidate_evaluator=False)
    print("generated & wrote 10000 candidates to datasets/synthetic.csv")
    