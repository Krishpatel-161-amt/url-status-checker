import requests

def take_list(clean_checks):
    results = []

    for check in clean_checks:
        url = check['url']
        
        try:
            response_url = requests.get(url,timeout=10)
            response_status_code = response_url.status_code
            elapsed_ms = response_url.elapsed.total_seconds() * 1000
        
        except requests.exceptions.RequestException:
            response_status_code = None
            elapsed_ms = None

        result = {"url": url, "status_code": response_status_code,"elapsed_ms": elapsed_ms}
        results.append(result)
    return results