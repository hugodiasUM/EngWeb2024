import json

html = '''
<!DOCTYPE html>
<html>
<head>
    <title>EngWeb2024</title>
    <meta charset="UTF-8>
</head>
<body>
'''

file = open("mapa.json", "r", encoding=("utf-8")).read()

content = json.loads(file)

html += "<ul>"

for elem in content["cidades"]:
    html += f"<li>{elem["nome"]}</li>"

html += "</ul>"

html += "</body>"
html += "</html>"

file = open("mapa.html", "w", encoding="utf-8")
file.write(html)
file.close()