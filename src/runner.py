import requests

def take_list(clean_checks):
    """
    this takes the list from loader, vists each url,saves their status code and how much time it to response and stores it 'results' list 
    """
    results = []

    for check in clean_checks:
        url = check['url']
        expected_status_code = check["expected_status"]
        latency_threshold = check["latency_threshold_ms"]
        
        try:
            response_url = requests.get(url,timeout=10)
            response_status_code = response_url.status_code
            elapsed_ms = response_url.elapsed.total_seconds() * 1000

        except requests.exceptions.RequestException:
            response_status_code = None
            elapsed_ms = None

        result = {"url": url, "status_code": response_status_code,"elapsed_ms": elapsed_ms, "expected_status": expected_status_code, "latency_threshold_ms": latency_threshold}

        results.append(result)

    return results