import os

psl_seasons = [
    ("2026_2027.html", "2026/2027"),
    ("2025_2026.html", "2025/2026"),
    ("2024_2025.html", "2024/2025"),
    ("2023_2024.html", "2023/2024"),
]

epl_seasons = [
    ("2026_2027.html", "2026/2027"),
    ("2025_2026.html", "2025/2026"),
    ("2024_2025.html", "2024/2025"),
    ("2023_2024.html", "2023/2024"),
]

psl_seasons = []
epl_seasons = []

for file in os.listdir(psl_folder):

    if file.endswith(".html") and file != "index.html":

        season = file.replace(".html", "")
        label = season.replace("_", "/")

        psl_seasons.append((file, label))

for file in os.listdir(epl_folder):

    if file.endswith(".html") and file != "index.html":

        season = file.replace(".html", "")
        label = season.replace("_", "/")

        epl_seasons.append((file, label))

psl_seasons.sort(reverse=True)
epl_seasons.sort(reverse=True)


psl_options = ""

for file, season in psl_seasons:
    psl_options += (
        f'<option value="https://psl.footballarchive.co.za/{file}">{season}</option>'
    )


epl_options = ""

for file, season in epl_seasons:
    epl_options += (
        f'<option value="https://epl.footballarchive.co.za/{file}">{season}</option>'
    )




#Generating HTML Page

homepage_html = f"""
<!DOCTYPE html>
<html>
<head>

<title>Football Statistics Archive</title>

<style>

body {{
    margin: 0;
    font-family: Arial, sans-serif;
    background: #111111;
    color: white;
}}

header {{
    text-align: center;
    padding: 40px;
    background: #111827;
}}

.container {{
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 30px;
    padding: 40px;
}}

.card {{
    width: 350px;
    background: #1e293b;
    padding: 25px;
    border-radius: 12px;
    box-shadow: 0 5px 15px rgba(0,0,0,.3);
}}

.card h2 {{
    margin-top: 0;
}}

select {{
    width: 100%;
    padding: 10px;
    border-radius: 6px;
    border: none;
    background: #334155;
    color: white;
}}

footer{{
    text-align:center;
    padding:30px;
    margin-top:50px;
    background:#1c1c1c;
}}


</style>

</head>
<body>

<header>
   
    /logo.png" alt="Football Archive Logo" class="logo">

    <h1>Football Archive South Africa</h1>

    <p>Historical league tables, results, statistics and season archives</p>

</header>

<div class="container">

    <div class="card">
        <h2>🇿🇦 Betway Premiership</h2>

        <select onchange="openSeason(this.value)">
            <option value="">Select Season</option>
            {psl_options}
        </select>
    </div>

    <div class="card">
        <h2>🏴 English Premier League</h2>

        <select onchange="openSeason(this.value)">
            <option value="">Select Season</option>
            {epl_options}
        </select>
    </div>

</div>

<script>

function openSeason(page)
{{
    if(page)
    {{
        window.location.href = page;
    }}
}}

</script>

<footer>

    <p>
    © 2026 Football Archive South Africa
    </p>

    <p>
    www.footballarchive.co.za
    </p>

</footer>

</body>
</html>
"""


with open("website/index.html", "w", encoding="utf-8") as file:
    file.write(homepage_html)


# with open(f"website/{current_season}.html", "w", encoding="utf-8") as file:
#     file.write(html_content)

# with open("website/index.html", "w", encoding="utf-8") as file:
#     file.write(html_content)
