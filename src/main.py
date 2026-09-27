import sys
import argparse

from loader import load_and_parse
from runner import take_list
from auditor import audit
from report import display_results

def main():
    """
    Runs the pipeline: load → run → audit → report → exit.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="checks.yaml")
    args = parser.parse_args()

    
    checks = load_and_parse(args.config)

    raw_results = take_list(checks)

    judged_results = audit(raw_results)

    passed = display_results(judged_results)

    sys.exit(0 if passed else 1)

if __name__ == "__main__":
    main()