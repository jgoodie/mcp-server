# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract two numbers"""
    return a - b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

@mcp.tool()
def divide(a: int, b: int) -> float:
    """Divide two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b    

@mcp.tool()
def power(a: int, b: int) -> float:
    """Raise a to the power of b"""
    return a ** b   

@mcp.tool()
def modulus(a: int, b: int) -> int:
    """Get the modulus of a by b"""
    return a % b    

@mcp.tool()
def floor_divide(a: int, b: int) -> int:
    """Perform floor division of a by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a // b   

@mcp.tool()
def max_value(a: int, b: int) -> int:
    """Get the maximum of two numbers"""
    return max(a, b)    

@mcp.tool()
def min_value(a: int, b: int) -> int:
    """Get the minimum of two numbers"""
    return min(a, b)

@mcp.tool()
def average(a: int, b: int) -> float:
    """Get the average of two numbers"""
    return (a + b) / 2
