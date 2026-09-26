from loader import load_and_parse
from runner import take_list
from auditor import audit
final_list = load_and_parse()

audit_results = take_list(final_list)

print(audit(audit_results))