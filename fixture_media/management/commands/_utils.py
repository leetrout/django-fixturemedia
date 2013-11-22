import re
file_patt = re.compile(r'"(?:media://)?([^"]+?[\/\\]+[^"]+?\.[^."]+?)"')
file_patt_prefixed = re.compile(r'"media://([^"]+?[\/\\]+[^"]+?\.[^."]+?)"')
