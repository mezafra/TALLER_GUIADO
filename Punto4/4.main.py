alcancia = [1000, 200, 500]
meta=3000

total=sum(alcancia)

if total >=meta:
    print("felicidades, lograste tu meta")
else:
    falta=meta-total
    print(f"te faltan {falta} para alcanzar tu meta")

