"""
Utility functions for the Bifrost demo repository.
"""

def calculate_sum(a, b):
    """
    Calculate the sum of two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The sum of a and b
    """
    return a + b

def multiply(a, b):
    """
    Multiply two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The product of a and b
    """
    return a * b

if __name__ == "__main__":
    # Test the functions
    print(f"Sum: {calculate_sum(5, 3)}")
    print(f"Product: {multiply(5, 3)}")
