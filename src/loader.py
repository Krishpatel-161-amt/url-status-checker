import yaml

 
def load_and_parse():
    # Load the yaml file
    with open('checks.yaml','r') as file:
        data = yaml.safe_load(file)
        checks = data["checks"]

# loops through the list and fills defaults 
    returned_list = []
    for check in checks:
        url = check['url']
        expected_status_code = check.get("expected_status", 200)
        latency_threshold = check.get("latency_threshold_ms")
        
        packet = {"url": url, "expected_status": expected_status_code, "latency_threshold_ms": latency_threshold}
        returned_list.append(packet)
    return returned_list

print(load_and_parse())

    