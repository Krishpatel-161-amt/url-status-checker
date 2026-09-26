import yaml

def load_and_parse():
    # Load the yaml file
    with open('checks.yaml','r') as file:
        data = yaml.safe_load(file)
        raw_checks = data["checks"]

# loops through the list and fills defaults 
    clean_checks = []
    for check in raw_checks:
        url = check['url']
        expected_status_code = check.get("expected_status", 200)
        latency_threshold = check.get("latency_threshold_ms")
        
        clean_check = {"url": url, "expected_status": expected_status_code, "latency_threshold_ms": latency_threshold}
        clean_checks.append(clean_check)
    return clean_checks



    