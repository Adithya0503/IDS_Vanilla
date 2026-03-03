import pandas as pd
from sklearn.ensemble import IsolationForest


def detect_anomalies(file_path):
    df = pd.read_csv(file_path)

    numeric_df = df.select_dtypes(include=['number'])

    if numeric_df.empty:
        print("No numeric data available for anomaly detection.")
        return None, None, None

    model = IsolationForest(
        n_estimators=150,
        contamination=0.05,
        random_state=42
    )

    model.fit(numeric_df)
    predictions = model.predict(numeric_df)

    df["Anomaly"] = predictions
    df["Anomaly"] = df["Anomaly"].map({1: "Normal", -1: "Anomaly"})

    summary = df["Anomaly"].value_counts()

    # Extract anomaly rows
    anomaly_rows = df[df["Anomaly"] == "Anomaly"]

    output_file = file_path.replace(".csv", "_analyzed.csv")
    df.to_csv(output_file, index=False)

    return output_file, summary, anomaly_rows