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
    gap: 40px;
    padding: 80px 40px 40px 40px;
}}


header {{
    position: relative;
    text-align: center;
    padding: 40px;
    background: #ff0000; /* Red */
    color: black;        /* Default text color in header */
}}

header h1 {{
    color: black;
}}

header p {{
    color: black;
}}

.league-button {{
    width: 450px;
    min-height: 180px;
    cursor: pointer;
    text-align: center;
    transition: all 0.3s ease;
}}

.league-button h2 {{
    font-size: 2rem;
    margin-top: 35px;
}}

.league-button p {{
    font-size: 1.1rem;
}}

.league-button:hover {{
    transform: translateY(-8px);
    background: #334155;
    box-shadow: 0 10px 25px rgba(0,0,0,0.4);
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

.main-logo 
{{
    position: absolute;
    left: 20px;
    top: 50%;
    transform: translateY(-50%);
    width: 150px;
    height: auto;
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
.league-title {{
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 15px;
    margin-top: 20px;
}}

.psl-logo {{
    width: 250px;
    height: 100px;
    object-fit: contain;
}}

.epl-logo {{
    width: 300px;
    height: 150px;
    object-fit: contain;
}}

.league-title h2 {{
    margin: 0;
    font-size: 2rem;
}}

.league-link {{
    text-decoration: none;
    color: inherit;
}}

.league-button {{
    width: 450px;
    min-height: 180px;
    cursor: pointer;
    text-align: center;
    transition: all 0.3s ease;
}}

.league-button:hover {{
    transform: translateY(-8px);
    background: #334155;
}}



</style>

</head>
<body>

<header>
 
 <img src="badges/footballarchive.png" alt ="Main Logo" class="main-logo">
    <h1>Football Seasons Archives </h1>

    <p>Historical league tables, results, statistics and season archives</p>

</header>

<div class="container">

    <a href="https://psl.footballarchive.co.za" class="league-link">
    <div class="card league-button">
        <div class="league-title">
            <h2>PSL Seasons </h2>
            <img src="badges/psl_logo.jpg" alt="PSL League" class="psl-logo">
        </div>
      
    </div>
</a>

<a href="https://epl.footballarchive.co.za" class="league-link">
    <div class="card league-button">
        <div class="league-title">
            <h2>EPL Seasons </h2>
            <img src="badges/epl-logo.png" alt="EPL Logo" class="epl-logo">
        
    </div>
</a>



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



output_dir = "website"

os.makedirs(output_dir, exist_ok=True)

with open(os.path.join(output_dir, "index.html"), "w", encoding="utf-8") as file:
    file.write(homepage_html)




# with open(f"website/{current_season}.html", "w", encoding="utf-8") as file:
#     file.write(html_content)

# with open("website/index.html", "w", encoding="utf-8") as file:
#     file.write(html_content)
