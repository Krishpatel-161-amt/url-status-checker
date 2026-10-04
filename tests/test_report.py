from url_status_checker.report import display_results

def test_all_up_passes():
    fake_result = [{"url": 'https://github.com','status_code': 200, 'elapsed_ms': 100, 'verdict': 'UP'}, {"url": 'https://github.com/Krishpatel-161-amt','status_code': 200 , 'elapsed_ms': 100, 'verdict': 'UP'}]

    passed = display_results(fake_result)

    assert passed == True

def test_one_failure_fails_the_run():
    fake_result = [{"url": 'https://github.com','status_code': 200, 'elapsed_ms': 100, 'verdict': 'UP'}, {"url": 'https://github.com/Krishpatel-161-amt','status_code': 400 , 'elapsed_ms': 100, 'verdict': 'DOWN'}]

    passed = display_results(fake_result)

    assert passed == False