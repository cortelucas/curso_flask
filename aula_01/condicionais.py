inteiro: int = 5
online: bool = True

if inteiro == 5:
    print("inteiro: 5")
elif inteiro == 4 or online:
    print("Hi 4")
else:
    print("Fim")

print("Ola estou online" if online else "Ola estou offline")
