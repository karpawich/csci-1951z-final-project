import csv
from enum import Enum

class Degree(Enum):
    BACHELORS="Bachelors"
    MASTERS="Masters"
    PHD="Phd"

class Gender(Enum):
    MALE="M"
    FEMALE="F"
    NOT_APPLICABLE="N/A"

class VeteranStatus(Enum):
    YES="1"
    NO="0"
    NOT_APPLICABLE="N/A"

class WorkAuthorization(Enum):
    YES="1"
    NO="0"

class Disability(Enum):
    YES="1"
    NO="0"
    NOT_APPLICABLE="N/A"

# These numbers may be wrong
class Ethnicity(Enum):
    WHITE="0"
    BLACK="1"
    NATIVE_AMERICAN="2"
    ASIAN="3"
    PACIFIC_ISLANDER="4"

class Job:
    def __init__(self, role="N/A", start="N/A", end="N/A"):
        self.role = role
        self.start = start
        self.end = end

class Row:
    _applicant_id = 1

    def __init__(self,school_name:str, gpa:float, degree:Degree, location:str, gender:Gender, veteran_status:VeteranStatus, work_authorization:WorkAuthorization, disability:Disability, ethnicity:Ethnicity, jobs: list[Job], resume_score:int = 0):
        self.applicant_id = Row._applicant_id
        Row._applicant_id += 1

        self.school_name = school_name
        self.gpa = gpa
        self.degree = degree
        self.location = location
        self.gender = gender
        self.veteran_status = veteran_status
        self.work_authorization = work_authorization
        self.disability = disability
        self.ethnicity = ethnicity
        self.jobs = jobs
        self.resume_score = resume_score

def generate_csv(file_name, rows: list[Row], for_candidate_evaluator):
    field_names = ["Applicant ID", "School Name", "GPA", "Degree", "Location", "Gender", "Veteran status", "Work authorization", "Disability", "Ethnicity", "Role 1", "Start 1", "End 1", "Role 2", "Start 2", "End 2", "Role 3", "Start 3", "End 3"]
    if (for_candidate_evaluator):
        field_names.append("Resume score")
    with open(file_name + ".csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        for row in rows:
            csv_row = {
                "Applicant ID": row.applicant_id,
                "School Name": row.school_name,
                "GPA": row.gpa,
                "Degree": row.degree.value,
                "Location": row.location,
                "Gender": row.gender.value,
                "Veteran status": row.veteran_status.value,
                "Work authorization": row.work_authorization.value,
                "Disability": row.disability.value,
                "Ethnicity": row.ethnicity.value,
                "Role 1": row.jobs[0].role,
                "Start 1": row.jobs[0].start,
                "End 1": row.jobs[0].end,
                "Role 2": row.jobs[1].role,
                "Start 2": row.jobs[1].start,
                "End 2": row.jobs[1].end,
                "Role 3": row.jobs[2].role,
                "Start 3": row.jobs[2].start,
                "End 3": row.jobs[2].end,
            }
            if for_candidate_evaluator:
                csv_row["Resume score"] = row.resume_score
            writer.writerow(csv_row)
    with open(file_name + ".csv", "rb+") as csvfile:
        csvfile.seek(-2, 2)
        csvfile.truncate()