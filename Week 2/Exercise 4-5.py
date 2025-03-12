import re
import subprocess

def parse_traceroute_output(output):
    """
    Parses traceroute output to extract hop number and RTT values.
    Returns a list of tuples: (hop_number, average_RTT, full_line).
    """
    hops = []
    lines = output.splitlines()
    # The regex expects lines like:
    # " 1  192.168.1.1 (192.168.1.1)  1.123 ms  1.045 ms  1.032 ms"
    pattern = re.compile(r'^\s*(\d+)\s+.+?(\d+\.\d+)\s+ms\s+(\d+\.\d+)\s+ms\s+(\d+\.\d+)\s+ms')
    for line in lines:
        match = pattern.match(line)
        if match:
            hop_num = int(match.group(1))
            rtt1 = float(match.group(2))
            rtt2 = float(match.group(3))
            rtt3 = float(match.group(4))
            avg_rtt = (rtt1 + rtt2 + rtt3) / 3.0
            hops.append((hop_num, avg_rtt, line.strip()))
    return hops

def analyze_bottlenecks(traceroute_output, threshold=1.5):
    """
    Analyzes parsed traceroute data.
    Flags a hop as a potential bottleneck if its average RTT is greater
    than 'threshold' times the previous hop's average RTT.
    """
    hops = parse_traceroute_output(traceroute_output)
    print("Hop\tAvg RTT (ms)\tNote")
    previous_avg = None
    for hop_num, avg_rtt, line in hops:
        note = ""
        if previous_avg is not None and avg_rtt > previous_avg * threshold:
            note = "Potential bottleneck"
        print(f"{hop_num}\t{avg_rtt:.2f}\t\t{note}")
        previous_avg = avg_rtt

def run_and_analyze(domain):
    try:
        result = subprocess.run(["traceroute", domain], capture_output=True, text=True)
        output = result.stdout
        print("Traceroute Output:")
        print(output)
        print("\nBottleneck Analysis:")
        analyze_bottlenecks(output)
    except Exception as e:
        print(f"Error: {e}")

# Example: Run analysis for www.google.com
run_and_analyze("www.google.com")
