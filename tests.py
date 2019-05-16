import paddate

print("Test: Add Day to Month, CE")

padout = paddate.paddate('1500-05')
expect = '1500-05-01'
assert padout == expect

padout = paddate.paddate('1500-05', startend='end')
expect = '1500-05-31'
assert padout == expect

print("Test: Add Day to Month, CE, Leap years")

padout = paddate.paddate('1900-02', startend='end')
expect = '1900-02-28'
assert padout == expect

padout = paddate.paddate('2000-02', startend='end')
expect = '2000-02-29'
assert padout == expect

print("Test: Add Day to Month, BCE, Leap years")

padout = paddate.paddate('-1900-02', startend='end')
expect = '-1900-02-28'
assert padout == expect

padout = paddate.paddate('-2000-02', startend='end')
expect = '-2000-02-29'
assert padout == expect

print("Test: Add Day to Month, Extreme BCE")

padout = paddate.paddate('-1000000-02')
expect = '-1000000-02-01'
assert padout == expect

padout = paddate.paddate('-1000000-12')
expect = '-1000000-12-01'
assert padout == expect

print("Test: Add Day to Month, Extreme BCE, Leap Years")

padout = paddate.paddate('-1000000-02', startend='end')
expect = '-1000000-02-29'
assert padout == expect

padout = paddate.paddate('-999996-02', startend='end')
expect = '-999996-02-29'
assert padout == expect

padout = paddate.paddate('-999700-02', startend='end')
expect = '-999700-02-28'
assert padout == expect

print("Test: Year Start, CE and BCE")

padout = paddate.paddate('1500')
expect = '1500-01-01'
assert padout == expect

padout = paddate.paddate('-10191')
expect = '-10191-01-01'
assert padout == expect

padout = paddate.paddate('-1000000')
expect = '-1000000-01-01'
assert padout == expect

print("Test: Year End, CE and BCE")

padout = paddate.paddate('1500', startend='end')
expect = '1500-12-31'
assert padout == expect

padout = paddate.paddate('10191', startend='end')
expect = '10191-12-31'
assert padout == expect

padout = paddate.paddate('-1000000', startend='end')
expect = '-1000000-12-31'
assert padout == expect

print("All tests OK.")
