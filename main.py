from weather import mcp

if __name__ == "__main__":
    print("Server started1\n")
    # Initialize and run the server
    mcp.run(transport="stdio")
    print("Server started")
