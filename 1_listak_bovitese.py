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
print(nyelvek)
print(len(nyelvek))
print()

del nyelvek[1]
print(nyelvek)
print()

nyelvek.remove("Python")
print(nyelvek)
print()

nyelvek.clear()
print(nyelvek)