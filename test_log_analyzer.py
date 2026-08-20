import os
from log_analyzer import extract_ip, count_failed_logins, flag_suspicious_ips

def test_extract_ip_basic():
    line = "2026-08-17 14:23:01 LOGIN_FAILED user=admin ip=192.168.1.50"
    result = extract_ip(line)
    assert result == "192.168.1.50"

def test_extract_ip_success_line():
    line = "2026-08-17 14:25:00 LOGIN_SUCCESS user=eunice ip=192.168.1.10"
    result = extract_ip(line)
    assert result == "192.168.1.10"

def test_count_failed_logins_no_failures():
    with open("temp_no_failures.log", "w") as file:
        file.write("2026-08-17 14:25:00 LOGIN_SUCCESS user=eunice ip=192.168.1.10\n")

    result = count_failed_logins("temp_no_failures.log")
    assert result == {}

    os.remove("temp_no_failures.log")

def test_flag_suspicious_ips_detects_threshold():
    counts = {"192.168.1.50": 5, "10.0.0.5": 1}
    result = flag_suspicious_ips(counts)
    assert result == {"192.168.1.50": 5}
