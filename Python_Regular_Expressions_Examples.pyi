# regex_examples.py

import re

# What are regular expressions?
print("Example 1: Regular Expressions")
pattern = r"apple"
text = "I love eating apple pie."
if re.search(pattern, text):
    print("Found 'apple' in the text.")
else:
    print("Did not find 'apple' in the text.")
print()


# The match Function
print("Example 2: The match Function")
pattern = r"apple"
text = "apple pie is delicious."
match = re.match(pattern, text)
if match:
    print("Matched 'apple' in the beginning of the text.")
else:
    print("No match found at the beginning of the text.")
print()


# The search Function
print("Example 3: The search Function")
pattern = r"apple"
text = "I love eating apple pie."
match = re.search(pattern, text)
if match:
    print("Found 'apple' in the text.")
else:
    print("Did not find 'apple' in the text.")
print()


# Matching vs Searching
print("Example 4: Matching vs Searching")
pattern = r"apple"
text = "I love eating apple pie."
match = re.match(pattern, text)
if match:
    print("Matched 'apple' at the beginning of the text.")
else:
    print("No match found at the beginning of the text.")

match = re.search(pattern, text)
if match:
    print("Found 'apple' in the text.")
else:
    print("Did not find 'apple' in the text.")
print()


# Search and Replace
print("Example 5: Search and Replace")
pattern = r"apple"
text = "I love eating apple pie. Apple is delicious."
replaced_text = re.sub(pattern, "banana", text)
print("Original Text:", text)
print("Replaced Text:", replaced_text)
print()


# Extended Regular Expressions
print("Example 6: Extended Regular Expressions")
pattern = r"p..ple"  # Match words with 'p', followed by any two characters, and ending with 'ple'.
text = "apple, purple, people"
matches = re.findall(pattern, text)
print("Matches:", matches)
print()


# Wildcard
print("Example 7: Wildcard")
pattern = r"p.*e"  # Match words starting with 'p', followed by any number of characters, and ending with 'e'.
text = "pie, apple, purple, people"
matches = re.findall(pattern, text)
print("Matches:", matches)
print()


# more_complex_regex.py

import re

# Complex Example 1: Extracting Phone Numbers
print("Complex Example 1: Extracting Phone Numbers")
text = "Contact us at +1 (555) 123-4567 or +91 9876543210."
# Regular expression to match phone numbers in the format: +X (XXX) XXX-XXXX or +XX XXXXXXXXXX
pattern = r"\+\d{1,2}\s?\(\d{3}\)\s?\d{3}-\d{4}|\+\d{2}\s?\d{10}"
phone_numbers = re.findall(pattern, text)
print("Phone Numbers:", phone_numbers)
print()

# Explanation of the Regular Expression (pattern) for Phone Numbers:
# \+                    -> Matches the '+' symbol.
# \d{1,2}               -> Matches one or two digits for the country code (e.g., +1 or +91).
# \s?                   -> Matches zero or one whitespace character.
# \(                    -> Matches the '(' symbol.
# \d{3}                 -> Matches three digits for the area code (e.g., (555)).
# \)                    -> Matches the ')' symbol.
# \s?                   -> Matches zero or one whitespace character.
# \d{3}-\d{4}           -> Matches three digits followed by a hyphen and four digits (e.g., 123-4567).
# |                     -> Alternation (OR) operator to match either of the two patterns.
# \+\d{2}\s?\d{10}       -> Matches country code and 10 digits without parentheses (e.g., +91 9876543210).
# Note: The regular expression combines two patterns with the '|' operator to cover both formats.

# Complex Example 2: Extracting URLs
print("Complex Example 2: Extracting URLs")
text = "Visit our website at https://www.example.com or http://sub.example.org."
# Regular expression to match URLs starting with 'http://' or 'https://' and domain name with optional subdomain.
pattern = r"https?://(?:\w+\.)?\w+\.\w+"
urls = re.findall(pattern, text)
print("URLs:", urls)
print()

# Explanation of the Regular Expression (pattern) for URLs:
# https?://              -> Matches 'http://' or 'https://'.
# (?:                    -> Non-capturing group.
#   \w+\.)?              -> Matches subdomain (e.g., 'www.') with a dot (.) or none.
# \w+                    -> Matches domain name (e.g., 'example').
# \.\w+                  -> Matches top-level domain (e.g., '.com').
# Note: The regular expression captures URLs starting with 'http://' or 'https://' and the domain name with optional subdomain.
# Non-capturing group (?:...) is used to avoid capturing the subdomain separately.

# Complex Example 3: Extracting Email Addresses
print("Complex Example 3: Extracting Email Addresses")
text = "Contact us at support@example.com or info@company.org."
# Regular expression to match email addresses in the format: username@domain.tld
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
email_addresses = re.findall(pattern, text)
print("Email Addresses:", email_addresses)
print()

# Explanation of the Regular Expression (pattern) for Email Addresses:
# [a-zA-Z0-9._%+-]+  -> Matches the username part before '@'.
#   [a-zA-Z0-9._%+-] -> Character set for valid characters in the username.
#   +               -> One or more occurrences of the previous character set.
# @                  -> Matches the '@' symbol.
# [a-zA-Z0-9.-]+     -> Matches the domain name part after '@'.
#   [a-zA-Z0-9.-]   -> Character set for valid characters in the domain name.
#   +               -> One or more occurrences of the previous character set.
# \.                 -> Escaped dot (.) to match the dot (.) symbol.
# [a-zA-Z]{2,}       -> Matches the top-level domain (e.g., .com, .org).
#   [a-zA-Z]{2,}     -> Character set for valid characters in the top-level domain.
#   {2,}             -> Two or more occurrences of the previous character set.

# The regular expression pattern matches email addresses that follow the typical
# structure of 'username@domain.tld'. It looks for a username with alphanumeric
# characters and special characters like '.', '_', '%', '+', or '-'. The '@' symbol
# is then expected, followed by a domain name with alphanumeric characters and special
# characters like '.', or '-'. Finally, the top-level domain (e.g., .com, .org) is
# matched, consisting of at least two letters.

# ... Additional examples ...


# Complex Example 4: Extracting Dates
print("Complex Example 4: Extracting Dates")
text = "Join us on 2023-07-17 for the event. RSVP by 2023/07/10."
# Regular expression to match dates in the format: YYYY-MM-DD or YYYY/MM/DD
pattern = r"\d{4}[-/]\d{2}[-/]\d{2}"
dates = re.findall(pattern, text)
print("Dates:", dates)
print()

# Explanation of the Regular Expression (pattern) for Dates:
# \d{4}        -> Matches four digits for the year (e.g., 2023).
# [-/]         -> Matches either '-' or '/' as the separator.
# \d{2}        -> Matches two digits for the month (e.g., 07).
# [-/]         -> Matches either '-' or '/' as the separator.
# \d{2}        -> Matches two digits for the day (e.g., 17).
# Note: The regular expression pattern matches dates in the format YYYY-MM-DD or YYYY/MM/DD.

# Complex Example 5: Extracting Hashtags
print("Complex Example 5: Extracting Hashtags")
text = "Using #Python for #DataAnalysis is amazing! #programming #AI"
# Regular expression to match hashtags starting with '#' and followed by alphanumeric characters or underscores.
pattern = r"#\w+"
hashtags = re.findall(pattern, text)
print("Hashtags:", hashtags)
print()

# Explanation of the Regular Expression (pattern) for Hashtags:
# #              -> Matches the '#' symbol.
# \w+            -> Matches one or more word characters (alphanumeric characters or underscores).
# Note: The regular expression pattern matches hashtags in the format #word, where 'word' can be any sequence of alphanumeric characters or underscores.

# Complex Example 6: Extracting HTML Tags
print("Complex Example 6: Extracting HTML Tags")
html_text = "<p>This is a paragraph.</p><a href='https://www.example.com'>Link</a>"
# Regular expression to match HTML tags (opening and closing) and their content.
pattern = r"<(\w+).*?>(.*?)<\/\1>"
html_tags = re.findall(pattern, html_text)
print("HTML Tags:", html_tags)
print()

# Explanation of the Regular Expression (pattern) for HTML Tags:
# <(\w+)        -> Matches the opening HTML tag (<tag_name>), capturing the tag name.
# .*?           -> Matches any characters (non-greedy) between the opening and closing tags.
# (.*?)         -> Captures the content within the tags.
# <\/\1>        -> Matches the closing HTML tag (</tag_name>), using a backreference to the captured tag name.
# Note: The regular expression pattern matches HTML tags and their content. It captures both the tag name and the content using parentheses for later retrieval.

# ... Additional examples ...



