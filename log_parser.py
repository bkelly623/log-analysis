import json
import re
from collections import defaultdict

# Open the log file
with open("access.log", "r") as file:
    logs = file.readlines()

# Dictionary to track failed logins per IP
failed_logins = defaultdict(int)

# Define regex patterns
failed_login_pattern = r'401'  # HTTP 401 Unauthorized
ip_pattern = r'(\d+\.\d+\.\d+\.\d+)'  # Extract IP address

# Process each log entry
for log in logs:
    try:
        # Attempt to parse JSON
        data = json.loads(log)
        ip = data.get("remote_ip", "N/A")
        status_code = str(data.get("status", ""))  # Get HTTP status code
        
        # Detect failed login attempts (HTTP 401)
        if re.search(failed_login_pattern, status_code):
            failed_logins[ip] += 1

    except json.JSONDecodeError:
        continue  # Skip invalid log lines

# Display results
print("\n🔍 **Failed Login Attempts Detected:**")
for ip, count in sorted(failed_logins.items(), key=lambda x: x[1], reverse=True):
    print(f"IP: {ip} → {count} failed logins")

# Highlight potential brute-force attacks (5+ failed attempts)
print("\n🚨 **Potential Brute-Force Attacks:**")
for ip, count in failed_logins.items():
    if count >= 5:
        print(f"🚨 IP {ip} has {count} failed login attempts!")
