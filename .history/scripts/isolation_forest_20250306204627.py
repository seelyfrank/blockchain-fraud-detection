# IMPORTS
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest


'''
Train and return an isolation forest

Params:
    df: Input data
    features: List of column names
    n_estimator: Num of trees in the isolation forest
    contamination: Prop. of anomalies
    inplace: 
    random_state: Random state seed (default will be 20)

Returns:
    df_results: Dataframe with added anomaly scores
    pipe: Trained pipeline with standard scaler and isolation forest

'''
def train_isolation_forest(df, features, n_estimators, contamination, inplace=False, random_state=20):

    df_features = df[features].copy()

    pipe = Pipeline([('scaler', StandardScaler()),
                     ('isolation_forest', IsolationForest(n_estimators=n_estimators,
                                                         contamination=contamination,
                                                         random_state=random_state))])
    
    # feature dataframe
    df_results = df.copy()
    df_results['anomaly_score'] = pipe.fit_predict(df_features)

    # give back some info on the (non)anomaly counts
    num_anomalies = len(df_results[df_results['anomaly_score'] == -1])
    num_normal = len(df_results[df_results['anomaly_score'] != -1])
    print(f'Number of anomalies flagged: {num_anomalies}')
    print(f'Number of unflagged points: {num_normal}')

    # get scores
    scores = pipe.named_steps['isolation_forest'].decision_function(df_features)

    # plot anomaly scores
    plt.figure(figsize=(12, 6))
    sns.histplot(scores, bins=25, kde=True, color='blue')

    plt.xlabel("Anomaly Score", fontsize=14)
    plt.ylabel("Frequency", fontsize=14)
    plt.title("Distribution of Anomaly Scores", fontsize=16, fontweight="bold")

    plt.grid(True, linestyle="--", alpha=0.5)
    plt.show()

    print(f"Min: {np.min(scores)}\nMax: {np.max(scores)}\nMean: {np.mean(scores)}\nStd Dev: {np.std(scores)}")

    if inplace:
        

    return df_results, pipe



''' 
Creates a scatter plot of all anomalies in the dataframe (red is anomaly and green is non-anomaly)

Params:
    isolation_df: dataframe expecting an 'anomaly_score' column and a 'value' column

Returns nothing
'''
def scatter_plot_anomalies(isolation_df):
    anomaly_values = isolation_df[isolation_df['anomaly_score'] == -1]['value']
    normal_values = isolation_df[isolation_df['anomaly_score'] != -1]['value']
    print(anomaly_values)

    index_anomaly = anomaly_values.index
    index_normal = normal_values.index

    sns.set_style("whitegrid")
    plt.figure(figsize=(20, 10), facecolor="whitesmoke")

    plt.scatter(index_normal, normal_values, 
                linestyle='-', marker='o', 
                s=15, alpha=0.5, 
                color='green', edgecolor='black', 
                label="Normal Transactions")

    plt.scatter(index_anomaly, anomaly_values, 
                linestyle='-', marker='o', 
                s=30, alpha=0.8, 
                color='red', edgecolor="black", 
                label="Anomalous Transactions")

    plt.yscale("log")
    plt.xticks(np.linspace(0, len(isolation_df), num=11, dtype=int), fontsize=12)
    plt.yticks(fontsize=12)
    plt.xlabel('Transaction Index', fontsize=14, fontweight='bold')
    plt.ylabel('Transaction Value (Log Scale)', fontsize=14, fontweight='bold')
    plt.title('Anomalies vs. Normal Transactions', fontsize=16, fontweight='bold', color="black")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend(fontsize=12, frameon=True, facecolor="whitesmoke", edgecolor="black", loc="upper right")
    plt.show()
