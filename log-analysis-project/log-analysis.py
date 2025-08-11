#!/usr/bin/env python3
# This script reads a web server log file and finds IPs with 3 or more failed login attempts (HTTP STATUS 401)

import re
from collections import defaultdict

def parse_failed_logins(logfile="sample-log.txt", threshold=3):
    failed_logins = defaultdict(int)

    # Regex to extract IP, endpoint, and status code
    log_pattern = re.compile(
        r'(?P<ip>\d+\.\d+\.\d+\.\d+).*?"\S+\s(?P<endpoint>\S+)\s\S+"\s(?P<status>\d{3})'
    )

    with open(logfile, 'r') as file:
        for line in file:
            match = log_pattern.search(line)
            if not match:
                continue

            ip = match.group("ip")
            endpoint = match.group("endpoint")
            status = match.group("status")

            # Match any endpoint containing '/login' and a 401 response
            if "/login" in endpoint and status == "401":
                failed_logins[ip] += 1

    return failed_logins

def report_suspicious_ips(failed_logins, threshold=3):
    print(f"IPs with {threshold} or more failed login attempts:")
    for ip, count in failed_logins.items():
        if count >= threshold:
            print(f"{ip} - {count} failed attempts")

if __name__ == "__main__":
    logfile = "sample-log.txt"
    failed_logins = parse_failed_logins(logfile)
    report_suspicious_ips(failed_logins)

print("Script finished running.")

