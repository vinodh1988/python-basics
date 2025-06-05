data = []
with open('people.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    # Skip header and separator lines
    if line.strip() == "" or line.startswith('-') or line.lower().startswith('sno'):
        continue
    parts = line.strip().split()
    if len(parts) >= 3:
        sno = parts[0]
        name = parts[1]
        city = ' '.join(parts[2:])
        data.append({'SNo': sno, 'Name': name, 'City': city})

print(data)