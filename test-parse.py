import re

log_pattern = re.compile(
    r'(?P<ip>\d+\.\d+\.\d+\.\d+) .* "\S+ (?P<endpoint>\S+) \S+" (?P<status>\d{3})'
)

with open("sample-log.txt", "r") as f:
    for line in f:
        match = log_pattern.search(line)
        if match:
            print(f"MATCH: IP={match.group('ip')}, ENDPOINT={match.group('endpoint')}, STATUS={match.group('status')}")
        else:
            print("NO MATCH:", line.strip())
