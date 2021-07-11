
# QuoteGenerator - Every time its run, reads from a file and displays the quote

import random

f = open("quote.txt", "r", encoding='utf-8')
quote = f.readlines()
len = len(quote)
print("-"*25)
print(random.choice(quote))
print("-"*25)
f.close()

