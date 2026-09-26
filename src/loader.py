import yaml

def load_and_parse():
    """
    Opens and parses the yaml file, apply defaults 
    (if user didnt write expected_status and latency in the yaml) and
    hands off the list of checks to perform 
    """
    with open('checks.yaml','r') as file:
        data = yaml.safe_load(file)
        raw_checks = data["checks"]

    clean_checks = []

    for check in raw_checks:
        url = check['url']
        expected_status_code = check.get("expected_status", 200)
        latency_threshold = check.get("latency_threshold_ms")
        
        clean_check = {"url": url, "expected_status": expected_status_code, "latency_threshold_ms": latency_threshold}
        clean_checks.append(clean_check)

    return clean_checks



    