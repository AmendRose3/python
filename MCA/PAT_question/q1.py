"""Test1 Question
You are provided with a string data that contains information about various products
sold in an online store. Each product's information is formatted as "name,category,price"
and separated from the next product's information by a semicolon (;). Your task is to
write a Python function named calculate_revenue_for_category that analyzes this string
to calculate and return the total revenue for a specified product category.
Your function should accept two parameters:
1. data (string): Contains product information in the format "name,category,price".
2. target_category (string): The category for which you need to calculate the total
revenue.
The function should return the total revenue (as a floating-point number) for all products
within the specified category. The category comparison is case-sensitive.
Function Signature:
def calculate_revenue_for_category(data, target_category)
Constraints:
• Use only string methods for processing the data string. Avoid using lists,
dictionaries, tuples, or sets.
• Assume that prices are valid numbers that can be converted to floating-point
values.
• The input string is well-formed and does not contain errors or inconsistencies.
"""


def calculate_revenue_for_category(data, target_category):
   
    # Initialize total revenue
    total_revenue = 0.0
    # Split the data string into a list of product information
    products = data.split(';')
    # Traverse through the list of product information
    for product_info in products:
        # Split product information into name, category, and price
        name, category, price = product_info.split(',')
        # Check if the product belongs to the target category
        if category == target_category:
            # Add the price to total revenue
            total_revenue += float(price)
    return total_revenue


data =input()
target_category =input()
revenue = calculate_revenue_for_category(data, target_category)
print(calculate_revenue_for_category(data, target_category))
