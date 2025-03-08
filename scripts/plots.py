# IMPORTS
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


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

''' 
Used to display the relationship between total transactions and total value sent, specifically
to be used with the `transaction_rate.csv` file

Params:
    df: SHOULD ONLY BE df made from `transaction_rate.csv`

Returns nothing
'''
def transaction_outlier_plot(flagged_data, x_axis, y_axis):
    plt.figure(figsize=(10,6))
    plt.scatter(x_axis, 
                y_axis, 
                c=flagged_data, 
                cmap='coolwarm', 
                edgecolors=['0'],
                alpha=0.7)
    plt.xlabel("Total Transactions")
    plt.ylabel("Total Value Sent (ETH)")
    plt.title("Transaction Count vs. Total Value Sent (Anomalies)")
    plt.show()
