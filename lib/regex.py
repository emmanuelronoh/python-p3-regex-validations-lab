# lib/regex.py

import re

# Updated regular expression for names
# Matches names with initial capital letter, followed by letters, apostrophes, hyphens, and single spaces.
name_regex = re.compile(r"^[A-Z][a-zA-Z-']*( [A-Z][a-zA-Z-']*)*$")

# Regular expression for phone numbers
# Matches phone numbers in formats: 5555555555, 555-555-5555, (555) 555-5555
phone_regex = re.compile(r"^(\(\d{3}\)\s?|\d{3}[-\s]?)\d{3}[-\s]?\d{4}$")

# Regular expression for email addresses
# Matches email addresses starting with letters, optionally followed by dots, and ending with valid domain
email_regex = re.compile(r"^[a-zA-Z][a-zA-Z0-9]*[.]?[a-zA-Z0-9]*@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$")
