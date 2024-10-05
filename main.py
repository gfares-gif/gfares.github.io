html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Info Table</title>
    <style>
        table {
            width: 50%;
            border-collapse: collapse;
            margin-left: auto;
            margin-right: auto;
        }
        table, th, td {
            border: 1px solid black;
        }
        th, td {
            padding: 10px;
            text-align: left;
        }
        body {
            text-align: center;
        }
    </style>
</head>
<body>

<h2>Gabriel Fares</h2>

<table>
    <tr>
        <td><strong>Name</strong></td>
        <td>Gabriel Fares</td>
    </tr>
    <tr>
        <td><strong>Introduction</strong></td>
        <td>Hello, I am a junior majoring in BS IT. My favorite programming language is Java.</td>
    </tr>
    <tr>
        <td><strong>Hobbies</strong></td>
        <td>Hobbies are going to the gym and reading books.</td>
    </tr>
</table>

</body>
</html>
"""

with open("index.html", "w") as file:
    file.write(html_content)
