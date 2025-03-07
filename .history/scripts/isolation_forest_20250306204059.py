'''
Train and return an isolation forest

Params:
    df: Input data
    features: List of column names
    n_estimator: Num of trees in the isolation forest
    contamination: Prop. of anomalies
    random_state: Random state seed (default will be 20)

Returns:
    df_results: Dataframe with added anomaly scores
    pipe: Trained pipeline with standard scaler and isolation forest

'''
def train_isolation_forest(df, features, n_estimators, contamination, random_state=20):

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

    return df_results, pipe
