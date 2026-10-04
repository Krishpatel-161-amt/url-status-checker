def audit(audit_results):
    """
    Takes the raw results from runner.py and judges if the url's were unreachable,up,down or slow and returns the list
    """
    judged_results = []
    for result in audit_results:
        if result['status_code'] is None:
            result.update({"verdict": "UNREACHABLE"})
        elif result['status_code'] != result['expected_status']:
            result.update({"verdict": "DOWN"})
        elif result['latency_threshold_ms'] is not None and result['elapsed_ms'] > result['latency_threshold_ms']:
            result.update({"verdict": "SLOW"})
        else:
            result.update({"verdict": "UP"})
        
        judged_results.append(result)

    return judged_results