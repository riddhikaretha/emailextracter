# Task 3: Email Address Extractor with Error Handling
# Author: Riddhi Karetha

import re
import sys

# Default file names
input_file = "input.txt"
output_file = "extracted_emails.txt"

try:
    # Read input file
    with open(input_file, "r", encoding="utf-8") as file:
        content = file.read()

    # Check if file is empty
    if not content.strip():
        print("⚠️ Input file is empty. No emails to extract.")
        sys.exit(0)

    # Email regex pattern
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    # Find all emails
    emails = re.findall(email_pattern, content)

    if not emails:
        print("⚠️ No email addresses found.")
        sys.exit(0)

    # Remove duplicates
    unique_emails = set(emails)

    # Write extracted emails
    with open(output_file, "w", encoding="utf-8") as file:
        for email in unique_emails:
            file.write(email + "\n")

    print("✅ Email extraction completed successfully!")
    print(f"📧 Total unique emails found: {len(unique_emails)}")
    print(f"📁 Saved to {output_file}")

except FileNotFoundError:
    print("❌ Error: input.txt file not found.")
    print("👉 Please make sure input.txt exists in the project folder.")

except PermissionError:
    print("❌ Error: Permission denied while accessing the file.")

except Exception as e:
    print("❌ An unexpected error occurred:")
    print(e)
