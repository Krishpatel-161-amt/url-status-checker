from loader import load_and_parse
from runner import take_list

final_list = load_and_parse()
take_list(final_list)
results = take_list(final_list)
print(results)