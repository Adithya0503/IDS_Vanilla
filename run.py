import os
import socket
from datetime import datetime
from audit_collector import run_audit
from anomaly_detector import detect_anomalies


def generate_text_report(hostname, summary, anomaly_rows):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report_name = f"{hostname}_AI_Security_Report.txt"

    with open(report_name, "w") as file:
        file.write("=============================================\n")
        file.write("        WINDOWS AI SECURITY REPORT\n")
        file.write("=============================================\n\n")

        file.write(f"Machine Name   : {hostname}\n")
        file.write(f"Scan Time      : {timestamp}\n\n")

        file.write("SUMMARY\n")
        file.write("---------------------------------------------\n")
        file.write(str(summary))
        file.write("\n\n")

        file.write("DETECTED ANOMALIES\n")
        file.write("---------------------------------------------\n")

        if anomaly_rows.empty:
            file.write("No anomalies detected.\n")
        else:
            for index, row in anomaly_rows.iterrows():
                file.write(f"\nType      : {row['Type']}\n")
                file.write(f"Value1    : {row['Value1']}\n")
                file.write(f"Value2    : {row['Value2']}\n")
                file.write(f"Value3    : {row['Value3']}\n")
                file.write("---------------------------------\n")

        file.write("\nExplanation:\n")
        file.write(
            "Anomalies represent statistically unusual system "
            "behavior detected by the Isolation Forest AI model.\n"
        )

    return report_name


def cleanup_files(*files):
    for file in files:
        if file and os.path.exists(file):
            os.remove(file)


def main():
    print("========================================")
    print("   WINDOWS AI SECURITY AUDIT SYSTEM")
    print("========================================\n")

    hostname = socket.gethostname()
    print(f"Scanning Machine: {hostname}\n")

    print("Collecting system data...")
    audit_file = run_audit()

    print("Running AI anomaly detection...")
    analyzed_file, summary, anomaly_rows = detect_anomalies(audit_file)

    anomalies = summary.get("Anomaly", 0)
    normals = summary.get("Normal", 0)

    print("\n================ RESULTS ================\n")
    print(f"Total Normal Records   : {normals}")
    print(f"Total Anomalies Found  : {anomalies}")

    if anomaly_rows is not None and not anomaly_rows.empty:
        print("\n⚠️  ANOMALIES DETECTED:\n")

        for index, row in anomaly_rows.iterrows():
            print(f"Type      : {row['Type']}")
            print(f"Value1    : {row['Value1']}")
            print(f"Value2    : {row['Value2']}")
            print(f"Value3    : {row['Value3']}")
            print("---------------------------------")
    else:
        print("\n✅ No anomalies detected.")

    report_file = generate_text_report(hostname, summary, anomaly_rows)

    print(f"\nReport Saved As: {report_file}")

    cleanup_files(audit_file, analyzed_file)

    print("\nTemporary scan files removed.")
    print("\nProcess Completed Successfully.")


if __name__ == "__main__":
    main()