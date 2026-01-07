# Task 3: Email Address Extractor with Error Handling and Summary Report
# Author: Riddhi Karetha

import re
import sys

input_file = "input.txt"
output_file = "extracted_emails.txt"
summary_file = "summary.txt"

try:
    # Read input file
    with open(input_file, "r", encoding="utf-8") as file:
        content = file.read()

    # Check empty file
    if not content.strip():
        print("⚠️ Input file is empty. No emails to extract.")
        sys.exit(0)

    # Email regex
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

    emails = re.findall(email_pattern, content)

    if not emails:
        print("⚠️ No email addresses found.")
        sys.exit(0)

    unique_emails = set(emails)

    # Save extracted emails
    with open(output_file, "w", encoding="utf-8") as file:
        for email in unique_emails:
            file.write(email + "\n")

    # Save summary report
    with open(summary_file, "w", encoding="utf-8") as file:
        file.write("Email Extraction Summary\n")
        file.write("-" * 30 + "\n")
        file.write(f"Input file: {input_file}\n")
        file.write(f"Output file: {output_file}\n")
        file.write(f"Total emails found: {len(emails)}\n")
        file.write(f"Unique emails extracted: {len(unique_emails)}\n")

    print("✅ Email extraction completed successfully!")
    print(f"📧 Unique emails found: {len(unique_emails)}")
    print(f"📁 Emails saved to {output_file}")
    print(f"📝 Summary saved to {summary_file}")

except FileNotFoundError:
    print("❌ Error: input.txt file not found.")
    print("👉 Please ensure the file exists in the project folder.")

except PermissionError:
    print("❌ Error: Permission denied while accessing a file.")

except Exception as e:
    print("❌ An unexpected error occurred:")
    print(e)
