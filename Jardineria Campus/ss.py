import json

with open("storage/producto.json", "r", encoding="utf-8") as f:
    fichero = f.read()
    data = json.loads(fichero)
    for i, val in enumerate(data):
        if i in data:
            data[i]["id"] = (i+1)
    data = json.dumps(data, indent=4).encode("utf-8")
    with open("storage/producto.json", "wb+") as f1:
        f1.write(data)
        f1.close()