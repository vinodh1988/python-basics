def processPeople(sno,name,city="NA",country="India"):
    """Process a person's details and return a formatted string."""
    print( f"{sno} {name} {city} {country}")

processPeople(1, "Alice", "New York", "USA")  # Example call with all parameters
processPeople(2, "Bob", "Chennai")  # Example call with default country
processPeople(3, "Charlie")  # Example call with all defaults except name
processPeople(4, "David", country="Canada") 
processPeople(name="Roger",sno=5,country="India",city="Mumbai") # Example call with named parameter for country