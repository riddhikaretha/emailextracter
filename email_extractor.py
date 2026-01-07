# Task 3: Email Address Extractor
# Author: Riddhi Karetha

import re

input_file = "input.txt"
output_file = "extracted_emails.txt"

# Read input file
with open(input_file, "r", encoding="utf-8") as file:
    content = file.read()

# Regular expression for email addresses
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# Find all emails
emails = re.findall(email_pattern, content)

# Remove duplicates
unique_emails = set(emails)

# Save extracted emails
with open(output_file, "w", encoding="utf-8") as file:
    for email in unique_emails:
        file.write(email + "\n")

print("✅ Email extraction completed successfully!")
print(f"📧 Total emails found: {len(unique_emails)}")
print(f"📁 Saved to {output_file}")
