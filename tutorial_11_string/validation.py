
"""
should contain only 1 @
should not start with @
should not start with ...
a@gmail.com_kumar
"""

import re

email = "arunkumar@gmail.com"
pattern = "^[\w\-\.]+@([\w-]+\.)+[\w-]{2,}$"

is_valid = re.match(pattern, email)

print(is_valid)