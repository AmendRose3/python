"""Test2 Question
You're developing a chat application where users can send messages to each other. As
part of message processing, you're tasked with implementing a feature to validate URLs
within the chat messages. Your goal is to create a Python function that ensures URLs
follow specific criteria using regular expressions.
1. Input Format:
o The function should take a single string argument representing the URL to
be validated.
o Ensure that the input follows standard URL format, including protocol
(http:// or https://), domain name, and optional path or query parameters.
o URLs may include subdomains, port numbers, and query parameters.
o The domain name should consist of alphanumeric characters and hyphens,
with at least one dot separating the domain parts.
o Ensure that the URL does not contain any special characters or invalid
symbols.
2. Output Format:
o Print True if the URL is valid according to the specified criteria.
o Print False if the URL is invalid.
Conditions for Valid URL:
• The URL should begin with either "http://" or "https://".
• The domain name should consist of alphanumeric characters, hyphens, and dots.
• At least one dot should separate the domain parts.
• Optional: URLs may include subdomains, port numbers, and query parameters.
• Ensure that the URL does not contain any special characters or invalid symbols
"""
import re

def validate_url(url):
    pattern = r'^https?://(?:[a-zA-Z0-9\-]+\.)+[a-zA-Z]{2,}(?:/[^/]+)*\??(?:\w+=\w+&?)*$'
    if re.match(
        pattern, url):
        return True
    else:
        return False


url1 = input()
print(validate_url(url1)) 

