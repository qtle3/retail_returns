# Retail Store Return Policy Checker

This Python program helps determine whether an item is eligible for return at a retail store. It checks various criteria such as possession of a receipt, the time since purchase, whether the item is a food product, the condition of the item, and whether the item was marked as a final sale. The program guides the user through a series of questions and provides a decision on the return eligibility based on predefined store policies.

## Key Concepts Covered

- **User Input Handling**: The program utilizes functions to capture and validate user inputs, ensuring correct data types and responses (e.g., yes/no questions).
  
- **Conditional Logic**: It uses conditional statements (`if-else`) to evaluate multiple factors in determining the eligibility of the item for return.
  
- **Logging**: The program implements logging to track the flow and decisions made during the execution, which is useful for debugging and auditing.
  
- **Modularity**: The program is broken down into smaller, reusable functions (`yes_no_input`, `numeric_input`, and `log_and_print`), promoting code reuse and readability.
