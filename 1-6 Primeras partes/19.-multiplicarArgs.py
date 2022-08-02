def suma(*args):
    total=1
    for numero in args:
        total*=numero
    return total

print("numero")
print(f"total {suma(5,3,6)}")