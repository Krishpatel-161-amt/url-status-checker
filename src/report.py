def display_results(judged_results):
    """
    takes the verdict and displays the result - how many checks passes vs failed
    """
    failed_count = 0
    total = len(judged_results) 
    for result in judged_results:
        if result['verdict'] != "UP":
            failed_count = failed_count + 1
        
    passed = failed_count == 0

    if passed:
        print(f"Verdict: PASSED - all {total} checks passed")
    else:
        print(f"Verdict: FAILED - {failed_count} out of {total} checks failed")
    
    print()

    print(f"{'STATE':<13} {'URL':<35} {'CODE':>6} {'TIME':>10}")
    print("-" * 67)
    
    for result in judged_results:
        code = '-' if result['status_code'] is None else f"{result['status_code']}"

        time = '-' if result['elapsed_ms'] is None else f"{result['elapsed_ms']:.0f} ms"

        print(f"{result['verdict']:<13} {result['url']:<35} {code:>6} {time:>10}")
    
    return passed
        

      
