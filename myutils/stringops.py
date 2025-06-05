def bigStrings(strings):
  
    return [s for s in strings if len(s) >=8]

def smallStrings(strings):
    return [s for s in strings if len(s) < 8]