def suma(*args):
    total=0
    for numero in args:
        total+=numero
    return total

print("numero")
print(f"total {suma(5,3,6,4,7)}")