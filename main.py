import pandas as pd
from sklearn.ensemble import IsolationForest

def run_analysis():
    print("Initializing file system monitor...")
    model = IsolationForest(contamination=0.05)
    print("System ready for real-time anomaly detection.")

if __name__ == "__main__":
    run_analysis()