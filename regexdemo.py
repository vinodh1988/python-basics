import regex
sample_strings = [
    "Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy",
    "Oscar", "Mallory", "Peggy", "Sybil", "Trent", "Victor", "Walter", "Yvonne", "Zara",
    "alice123", "Bob_Smith", "charlie.brown@example.com", "david99", "Eve-Adams", "frank_2024",
    "Grace.Hopper@domain.com", "HeidiKlum@fashion.net", "ivan_ivanov@mail.ru", "Judy-Blue",
    "Oscar.Wilde@literature.org", "Mallory@evil.com", "peggySue@music.com", "Sybil-2024",
    "Trent_Reznor@music.net", "victorAlpha", "Walter.White@bb.com", "Yvonne_Strahovski@tv.com",
    "Zara-Fashion", "ALICE@EXAMPLE.COM", "bob.smith@work.org", "CHARLIE@MAIL.COM",
    "david@domain", "eve@", "frank@", "grace@.com", "Heidi@domain.c", "Ivan@domain.co.uk",
    "Judy@sub.domain.com", "Oscar@domain.travel", "Mallory@domain.jobs", "Peggy@domain.info",
    "Sybil@domain.biz", "Trent@domain.name", "Victor@domain.email", "Walter@domain.io",
    "Yvonne@domain.dev", "Zara@domain.app", "alice@domain.tech", "Bob@domain.xyz",
    "Charlie@domain.site", "David@domain.online", "Eve@domain.store", "Frank@domain.blog",
    "Grace@domain.me", "Heidi@domain.tv", "Ivan@domain.cc", "Judy@domain.us",
    "Oscar@domain.ca", "Mallory@domain.au", "Peggy@domain.nz", "Sybil@domain.jp",
    "Trent@domain.cn", "Victor@domain.ru", "Walter@domain.de", "Yvonne@domain.fr",
    "Zara@domain.it", "Alice@domain.es", "Bob@domain.pt", "Charlie@domain.se",
    "David@domain.no", "Eve@domain.dk", "Frank@domain.fi", "Grace@domain.be",
    "Heidi@domain.nl", "Ivan@domain.ch", "Judy@domain.at", "Oscar@domain.pl",
    "Mallory@domain.gr", "Peggy@domain.tr", "Sybil@domain.il", "Trent@domain.sa",
    "Victor@domain.ua", "Walter@domain.ro", "Yvonne@domain.hu", "Zara@domain.cz",
    "Run", "Jump", "walk", "Swim", "Drive", "FLY", "Eat", "Sleep", "Code",
    "123 Main St.", "Apt 4B", "PO Box 123", "New York, NY", "Los Angeles, CA",
    "2024-06-01", "01/06/2024", "06/01/2024", "12:34 PM", "23:45", "error404",
    "success200", "fail500", "alice#domain.com", "bob@domain,com", "charlie@domain..com",
    "pig","hen","cow","dog","cat","fish","bird","snake","turtle","rabbit",
    "lion", "tiger", "bear", "elephant", "giraffe", "zebra", "monkey", "kangaroo",
    "John","Jhon","Jon","Jonson","Jhonson","10.0.0.17","192.168.1.1","49.113.12.34","10.43.55.35",
    "345.3636","434.34.abc","avv.ere.ere.rtd","is","an","he","a12x","x45p"
]
reg = r'^[a-zA-Z][a-zA-z0-9_\.]+@[a-zA-z][a-zA-z0-9_]+\.[a-zA-z]{2,7}$'  # Matches two letters separated by a space
for x in sample_strings:
   
    if regex.search(reg, x):
        print(f"Matched: {x}")

#   reg = r'^R'
#   reg = r'a$'
#   reg = r'^[0-9]'
#  reg = r'^[A-Z]'
# reg = r'^[A-Z][ai][rt]'
# reg = r'^J(oh|ho|o)n'
# reg = r'^[A-Za-z][a-z][A-Za-z]$'
# reg = r'^[A-Za-z][a-z]+[A-Za-z]$'
# reg = r'^[A-Za-z][a-z]*[A-Za-z]$'
# reg = r'^[A-Za-z][a-z]?[A-Za-z]$'
# reg = r'^[A-Za-z][a-z]{2}[A-Za-z]$' 
# reg = r'^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$'
# reg = r'^[a-zA-Z][a-zA-z0-9_\.]+@[a-zA-z][a-zA-z0-9_]+\.[a-zA-z]{2,7}$'


