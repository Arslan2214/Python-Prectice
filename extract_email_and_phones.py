import pyperclip
import re

def extract_data(text):
    phone_pattern = re.compile(r'\+?\d{1,4}[ -]?\(?\d{1,4}\)?[ -]?\d{1,4}[ -]?\d{1,9}')
    email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
    
    phones = phone_pattern.findall(text)
    emails = email_pattern.findall(text)
    
    # Clean up the phone numbers (strip unwanted characters and spaces)
    phones = [re.sub(r'[^\d\+\- ]', '', phone).strip() for phone in phones]
    
    formatted_result = ""
    
    # Add phone numbers section if any found
    if phones:
        formatted_result += "Phone Numbers Found:\n"
        formatted_result += '\n'.join(f"    {phone}" for phone in phones)
        formatted_result += "\n"
    
    # Add email addresses section if any found
    if emails:
        if formatted_result:  # Add a newline if phone numbers were also found
            formatted_result += "\n"
        formatted_result += "Email Addresses Found:\n"
        formatted_result += '\n'.join(f"    {email}" for email in emails)
    
    # Handle cases where no phone numbers or emails were found
    if not formatted_result:
        formatted_result = "No phone numbers or email addresses found."
    
    return formatted_result

# Get text from the clipboard
text = pyperclip.paste()

# Extract data and format it
formatted_data = extract_data(text)

# Copy the formatted data back to the clipboard
pyperclip.copy(formatted_data)

# Print a message based on what was found
if "Phone Numbers Found:" in formatted_data and "Email Addresses Found:" in formatted_data:
    print("Both phone numbers and email addresses have been copied to the clipboard.")
elif "Phone Numbers Found:" in formatted_data:
    print("Phone numbers have been copied to the clipboard. No email addresses found.")
elif "Email Addresses Found:" in formatted_data:
    print("Email addresses have been copied to the clipboard. No phone numbers found.")
else:
    print("No phone numbers or email addresses found. The clipboard has been updated with the result.")

# Uncomment the following line if you want to see the formatted data in the console
# print(formatted_data)
