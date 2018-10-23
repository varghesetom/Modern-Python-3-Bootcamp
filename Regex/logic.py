'''

| = pipe character

1. a. 914 364 1718
   b. (914) 364 1718

   (\(\d{3}\)|\d{3}) \d{3} \d{4}

   -> "\(" is an escape char for the opening parantheses
   -> then use the \d{3} to get the 3 numbers
   -> "\)" is the escape char for the closing parantheses
   -> "|" is the logical or for the regular \d{3}
   -> close this entire expression with () so as to only apply
      the logic to the first set of 3 numbers and then continue searching
      for the second and third set of numbers in the phone number

2.
    a. Mr. Reginald Lordsworth
    b. Mrs. Deborah Pristiniz

    ->(Mr\.|Mrs\.) [A-Za-z]+ [A-Za-z]+

    -> (Mr\.|Mrs\.) ([A-Za-z]+) ([A-Za-z]+)
        -- can use parantheses to capture different groups

3. Match both "cat(s)" and "dog(s)"

    -> \w{3}\(s\)

'''
