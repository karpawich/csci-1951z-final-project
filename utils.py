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

class InterviewDecision(Enum):
    YES="1"
    NO="0"

class Date:

    def __init__(self, month:int=-1, day:int=-1, not_applicable=False):
        self.not_applicable = not_applicable
        self.month = month
        self.day = day

    def __str__(self):
        if self.not_applicable:
            return "N/A"
        else:
            return str(self.month) + "/" + str(self.day)
        
    @classmethod  
    def from_str(cls, date_str):
        if date_str == "N/A":
            return cls(not_applicable=True)
        else:
            month, day = map(int, date_str.split("/"))
            return cls(month, day)

class Job:
    def __init__(self, role="N/A", start=Date(not_applicable=True), end=Date(not_applicable=True)):
        self.role = role
        self.start = start
        self.end = end

class Row:
    _applicant_id = 1

    def __init__(self,school_name:str, gpa:float, degree:Degree, location:str, gender:Gender, veteran_status:VeteranStatus, work_authorization:WorkAuthorization, disability:Disability, ethnicity:Ethnicity, jobs: list[Job], resume_score:int = None, interview_decision:InterviewDecision = None):
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
        self.interview_decision = interview_decision

def generate_csv(file_name, rows: list[Row], for_candidate_evaluator):
    field_names = ["Applicant ID", "School Name", "GPA", "Degree", "Location", "Gender", "Veteran status", "Work authorization", "Disability", "Ethnicity", "Role 1", "Start 1", "End 1", "Role 2", "Start 2", "End 2", "Role 3", "Start 3", "End 3"]
    if (for_candidate_evaluator):
        field_names.append("Resume score")
    with open(file_name + ".csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names, lineterminator="\n")
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
            }
            for i, job in enumerate(row.jobs):
                csv_row["Role " + str(i + 1)] = job.role
                csv_row["Start " + str(i + 1)] = str(job.start)
                csv_row["End " + str(i + 1)] = str(job.end)
            if for_candidate_evaluator:
                csv_row["Resume score"] = row.resume_score
            writer.writerow(csv_row)
    with open(file_name + ".csv", "rb+") as csvfile:
        csvfile.seek(-2, 2)
        csvfile.truncate()

def read_csv(file_name):
    rows = []
    with open(file_name, 'r') as csvfile:
        reader = csv.DictReader(csvfile)

        for row_dict in reader:
            # Parse basic fields
            school_name = row_dict["School Name"]
            gpa = float(row_dict["GPA"])
            degree = Degree(row_dict["Degree"])
            location = row_dict["Location"]
            gender = Gender(row_dict["Gender"])
            veteran_status = VeteranStatus(row_dict["Veteran status"])
            work_authorization = WorkAuthorization(row_dict["Work authorization"])
            disability = Disability(row_dict["Disability"])
            ethnicity = Ethnicity(row_dict["Ethnicity"])

            # Parse jobs
            jobs = []
            for i in range(1, 4):  # Assume up to 3 job entries
                role = row_dict.get(f"Role {i}", "N/A")  
                start_str = row_dict.get(f"Start {i}")
                end_str = row_dict.get(f"End {i}")

                start = Date.from_str(start_str)
                end = Date.from_str(end_str)
                jobs.append(Job(role, start, end))

            # Parse resume score (if it exists)
            resume_score = row_dict.get("Resume score", None)
            if resume_score != None:
                resume_score = int(resume_score)

            # Parse interview decision
            interview_decision = row_dict.get("Interview decision", None)
            if interview_decision != None:
                interview_decision = InterviewDecision(interview_decision)

            # Create Row object
            row = Row(school_name, gpa, degree, location, gender, 
                      veteran_status, work_authorization, disability, ethnicity, 
                      jobs, resume_score, interview_decision)
            rows.append(row)

    return rows