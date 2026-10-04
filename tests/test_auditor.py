from url_status_checker.auditor import audit

def test_up_result():
    fake_results = [{"url": 'https://github.com', 'expected_status': 200, 'latency_threshold_ms': None, 'elapsed_ms': 1234,'status_code': 200}]

    judged = audit(fake_results)

    assert judged[0]['verdict'] == "UP"

def test_down_result():
    fake_results = [{'url': "https://httpbin.org/status/404", 'expected_status': 200, 'status_code': 404, 'latency_threshold_ms': None, "elapsed_ms": 12}]

    judged = audit(fake_results)

    assert judged[0]['verdict'] == "DOWN"

def test_slow_result():
    fake_results = [{'url': "https://httpbin.org/delay/5", 'expected_status': 200, 'status_code': 200, 'latency_threshold_ms': 1000, "elapsed_ms": 1050}]

    judged = audit(fake_results)

    assert judged[0]['verdict'] == "SLOW"

def test_unreachable_result():
    fake_results = [{'url': "https://localhost:9999", 'expected_status': 200, 'status_code': None, 'latency_threshold_ms': None, "elapsed_ms": None}]

    judged = audit(fake_results)
    
    assert judged[0]['verdict'] == "UNREACHABLE"

def test_server_error_is_down():
    fake_results = [{"url": 'https://github.com', 'expected_status': 200, 'latency_threshold_ms': None, 'elapsed_ms': 1234,'status_code': 500}]
    
    judged = audit(fake_results)

    assert judged[0]['verdict'] == "DOWN"

def test_wrong_code_and_slow():
    fake_results = [{"url": 'https://github.com', 'expected_status': 200, 'latency_threshold_ms': 500, 'elapsed_ms': 1000,'status_code': 404}]
        
    judged = audit(fake_results)

    assert judged[0]['verdict'] == 'DOWN'


