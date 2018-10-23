import re

#http://www.rexegg.com/regex-quickstart.html

## Phone Number

"""
1. 415-591-1923

    \d{3}-\d{3}-\d{4}

2. 914 3641718

    \d{3} \d{3}-?\d{4}  ### The ? means the dash is optional

3. abbbbccccc

    ab*c*d

4. a. 09
   b. 4
   c. 9

   0?\d
"""
