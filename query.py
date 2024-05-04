import requests
import csv
import json
import shap
import pandas as pd

resume_scorer_endpoint = "https://jennjwang.pythonanywhere.com"
candidate_evaluator_endpoint = "https://heonlee.pythonanywhere.com"

def csv_to_json(fname):     
    with open(fname, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
         
        data = [row for row in csvReader] 
    
    return json.dumps(data)

def query(endpoint, json):
    response = requests.post(endpoint, data=json, headers={
        "Content-Type": "application/json"
    })
    
    if response.status_code == 200:
        print("hello", response)
        return response.json()
    else:
        print(f"error on post to {endpoint}, {response}")

class ResumeScorerModel:
    def __call__(self, *args):
        print(*args)
        return 5.0
        

if __name__ == "__main__":
    # json_string = csv_to_json("datasets/resume_scorer.csv")
    # print(json_string)
    # result = query(resume_scorer_endpoint, json_string)
    # print(result)
    dataset = pd.read_csv("datasets/synthetic.csv")
    print(dataset)
    model = ResumeScorerModel()
    model(dataset[0])
    # explainer = shap.Explainer(model, dataset)
    
    # shap_values = explainer(dataset[0])
    # shap.plots.waterfall(shap_values[0])

    
    
# https://shap.readthedocs.io/en/latest/generated/shap.Explainer.html