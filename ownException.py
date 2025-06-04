class InvalidIdError(Exception):
    """Exception raised for errors in the input ID."""
    
    def __init__(self, message="Invalid ID provided."):
        self.message = message
        super().__init__(self.message)  

