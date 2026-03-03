import os
import csv
import socket
import platform
import psutil
from datetime import datetime


def create_audit_file():
    folder = os.path.join(os.getcwd(), "AuditReports")
    if not os.path.exists(folder):
        os.makedirs(folder)

    hostname = socket.gethostname()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    filename = os.path.join(folder, f"{hostname}_{timestamp}.csv")

    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Type", "Value1", "Value2", "Value3"])

    return filename


def collect_system_data(filename):
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)

        # System Info
        writer.writerow(["CPU_Count", psutil.cpu_count(), "", ""])
        writer.writerow(["Memory_MB", psutil.virtual_memory().total // (1024 * 1024), "", ""])
        writer.writerow(["Disk_Usage_%", psutil.disk_usage('/').percent, "", ""])

        # Running Processes
        for proc in psutil.process_iter(['pid', 'cpu_percent', 'memory_percent']):
            try:
                writer.writerow([
                    "Process",
                    proc.info['pid'],
                    proc.info['cpu_percent'],
                    round(proc.info['memory_percent'], 2)
                ])
            except:
                continue

        # Open Ports
        for conn in psutil.net_connections(kind='inet'):
            if conn.status == psutil.CONN_LISTEN:
                writer.writerow([
                    "OpenPort",
                    conn.laddr.port,
                    conn.pid,
                    ""
                ])


def run_audit():
    filename = create_audit_file()
    collect_system_data(filename)
    return filename