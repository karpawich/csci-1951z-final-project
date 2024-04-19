from utils import Degree, Row, generate_csv, read_csv
import numpy as np
import argparse
import pandas as pd

# compute feature importances across dataset
def generate_master_rows(feature_enum, feature_name, rows):
    # create a dataset for each value feature can take
    # all the same except for the feature value
    values = [e for e in feature_enum]
    
    master_rows = []
    for v in values:
        new_rows = rows.copy()
        for r in new_rows:
            setattr(r, feature_name, v)
        master_rows.extend(new_rows)
            
    return master_rows
    
# mean the selection rate of each
def measure_selection_rate(feature_enum, feature_name, master_rows, results):
    values = [e.value for e in feature_enum]
    
    # split df into each
    n_each = len(master_rows) // len(values)
        
    selection_rates = {}
    for i, v in enumerate(values):
        start, end = i*n_each, i*n_each+n_each
        sub_rows = results[start:end]
        selection_rates[v] = sub_rows["score"].mean()

    return selection_rates


parser = argparse.ArgumentParser(description='')

# parser.add_argument('--synthetic', type=str,
#                     help='the filepath of the synthetic dataset', default="datasets/synthetic.csv")
parser.add_argument('--result', type=str,
                    help='the filepath to read results', default="datasets/result.csv")
parser.add_argument('--task', choices=['gen_test_data', 'measure_selection_rates'],
                    help="Task to perform: 'gen_test_data' or 'measure_selection_rates'")
parser.add_argument("--model", choices=[1, 2],
                    help="Which model to evaluate: resume scorer (1) or interview decider (2)")


if __name__ == "__main__":
    args = parser.parse_args()
    
    feature_enum = Degree
    feature_name = "degree"
    synthetic_fpath = "datasets/synthetic.csv" if args.model == 1 else "datasets/synthetic_with_score.csv"
    
    if args.task == 'gen_test_data':
        rows = read_csv(args.synthetic)
        master_rows = generate_master_rows(Degree, feature_name, rows)
        fname = f"datasets/test_df_{feature_name}"
        generate_csv(fname, master_rows, for_candidate_evaluator=False)
        print(f"generated csv to uploat @ {fname}")
    else:
        master_rows = read_csv(f"datasets/test_df_{feature_name}.csv")
        results = pd.read_csv(args.result, dtype=np.float64)
        selection_rates = measure_selection_rate(feature_enum, feature_name, master_rows, results)
        print("selection rates:", selection_rates)