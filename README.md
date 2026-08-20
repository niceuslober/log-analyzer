# Log Analyzer 🔍

A Python tool I built to parse log files and detect suspicious patterns, such as brute-force login attempts, by tracking failed login counts per IP address.

I created this to practice log analysis — the kind of pattern detection SOC analysts and DevSecOps engineers do daily — as a follow-up to my permission-auditor project, moving from file-system security into behavioral/log-based security.

### What it checks:
* **Failed Login Attempts:** Tracks how many times each IP address has a failed login in the log file.
* **Suspicious IPs:** Flags any IP that hits or exceeds a threshold (default: 3+ failed attempts), a common sign of a brute-force attack.

### Features:
* **Error Handling:** Won't crash if the log file is missing — prints a clean error message instead.
* **Summary Report:** Prints the total number of unique IPs with failed logins and lists all flagged/suspicious ones.
* **Unit Tested:** Core logic (IP extraction, failed login counting, suspicious flagging) is covered by automated tests using pytest.

### How to run it:
1. Clone the repo: git clone https://github.com/YOUR_USERNAME/log-analyzer.git
2. Go to the folder: cd log-analyzer
3. Run it: python3 log_analyzer.py

### Running tests:
pip install pytest
python3 -m pytest test_log_analyzer.py -v

### Why this matters:
Brute-force login attacks are one of the most common threats security teams monitor for. This tool automates the manual process of scanning through log files to catch repeated failed login attempts early, similar to what real SOC/DevSecOps monitoring tools do at a larger scale.

### Sample Output:
```
=== Log Analyzer Report ===
Total unique IPs with failed logins: 2
⚠️  Suspicious IPs detected (possible brute-force):
192.168.1.50: 5 failed attempts
