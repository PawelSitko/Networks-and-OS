import subprocess

def run_traceroute(domain):
    print(f"Tracing route to {domain}...\n")
    try:
        result = subprocess.run(["traceroute", domain], capture_output=True, text=True)
        print(result.stdout)
    except FileNotFoundError:
        print("The traceroute command is not available on this system.")
    except Exception as e:
        print(f"An error occurred while tracing route for {domain}: {e}")
    print("-" * 60 + "\n")

domain = "www.google.com"
run_traceroute(domain)
