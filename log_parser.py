import json

# Open the log file
with open("access.log", "r") as file:
    logs = file.readlines()

# Parse JSON log entries
for log in logs:
    try:
        data = json.loads(log)
        ip = data.get("remote_ip", "N/A")
        url = data.get("request", "N/A").split()[1] if "request" in data else "N/A"
        print(f"IP: {ip} | Requested: {url}")
    except json.JSONDecodeError:
        continue  # Skip lines that are not valid JSON
