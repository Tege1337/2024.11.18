nyelvek = ["Python", "C", "C++", "Java"]
nyelvek.append("Python")
print(nyelvek)
print()

nyelvek_masolat = nyelvek.copy()

nyelvek_website = ["HTML", "CSS", "JavaScript"]
nyelvek.extend(nyelvek_website)
print(nyelvek)
print()

nyelvek.insert(1, "Go")