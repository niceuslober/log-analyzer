def read_log(filename):
    with open(filename, "r") as file:
        for line in file:
            print(line.strip())

def extract_ip(line):
    parts = line.split()
    last_part = parts[-1]
    ip = last_part.replace("ip=", "")
    return ip

def count_failed_logins(filename):
    ip_counts = {}
    with open(filename, "r") as file:
        for line in file:
            if "LOGIN_FAILED" in line:
                ip = extract_ip(line)
                if ip in ip_counts:
                    ip_counts[ip] = ip_counts[ip] + 1
                else:
                    ip_counts[ip] = 1
    return ip_counts

def flag_suspicious_ips(ip_counts, threshold=3):
    suspicious = {}
    for ip in ip_counts:
        if ip_counts[ip] >= threshold:
            suspicious[ip] = ip_counts[ip]
    return suspicious

def main():
    filename = "sample.log"

    try:
        counts = count_failed_logins(filename)
        suspicious = flag_suspicious_ips(counts)

        print("=== Log Analyzer Report ===")
        print(f"Total unique IPs with failed logins: {len(counts)}")
        print()

        if suspicious:
            print("⚠️  Suspicious IPs detected (possible brute-force):")
            for ip in suspicious:
                print(f"  - {ip}: {suspicious[ip]} failed attempts")
        else:
            print("No suspicious activity detected.")

    except FileNotFoundError:
        print(f"Error: Could not find the log file '{filename}'.")

if __name__ == "__main__":
    main()
