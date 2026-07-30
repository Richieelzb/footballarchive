import os

#Generating HTML Page

homepage_html = f"""
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet"
href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">

<title>Football Statistics Archive</title>

<style>

body{{
    margin:0;
    font-family: Arial, sans-serif;

    background:
        linear-gradient(
            rgba(0,0,0,0.85),
            rgba(0,0,0,0.85)
        ),
        url("badges/stadium.png");

    background-size: cover;
    background-position: center;
    background-attachment: fixed;

    color:white;
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
    background: black;
    border-bottom:2px solid #ff0000;
 /* Red */
    color: red;        /* Default text color in header */
}}

header h1 {{
    color: red;
}}

.the-word {{
    color: white;
}}


header p {{
    color: white;
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

.main-logo-left 
{{
    position: absolute;
    left: 20px;
    top: 50%;
    transform: translateY(-50%);
    width: 150px;
    height: auto;
}}
.main-logo-right
{{
    position: absolute;
    right: 20px;
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
    height: 250px;
    object-fit: contain;
}}

.epl-logo {{
    width: 400px;
    height: 350px;
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

.hero {{
    background:
        linear-gradient(rgba(0,0,0,.7),rgba(0,0,0,.7)),
        url('images/stadium.jpg');
    background-size:cover;
    background-position:center;
    text-align:center;
    padding-top: 40px;
    padding-bottom: 40px;
    margin-top: -30px;
}}

.hero h1 {{
    color:#ff0000;
    font-size:4rem;
}}

.league-panel {{
    display:flex;
    justify-content:space-between;
    align-items:center;
    margin:30px auto;
    width:90%;
    border-radius:20px;
    overflow:hidden;
}}

.psl {{
    background:linear-gradient(90deg,#02152c,#0b2b4d);
  
}}

.epl {{
    background: linear-gradient(90deg,#2a003d,#51187f);
    
}}

.features {{
    display:grid;
    grid-template-columns:repeat(4,1fr);
    gap:20px;
    width:90%;
    margin:auto;
}}
.feature{{
    background:#1e293b;
    padding:20px;
    border-radius:12px;
    text-align:center;
}}
.hero {{
    min-height: 500px;

    background:
        linear-gradient(
            rgba(0,0,0,0.65),
            rgba(0,0,0,0.65)
        ),
        url("badges/stadium.png");

    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;

    display: flex;
    align-items: center;
    justify-content: center;

    text-align: center;
    padding: 50px;
    margin-bottom: 0;
}}

.hero-content h2 {{
    color: white;
    font-size: 3rem;
    margin-bottom: 10px;
}}

.hero-content h1 {{
    color: #ff0000;
    font-size: 5rem;
    margin: 0;
}}

.hero-content p {{
    color: white;
    font-size: 1.5rem;
    max-width: 700px;
    margin: 20px auto;
}}
.browse-title {{
    display:flex;
    align-items:center;
    justify-content:center;
    gap:20px;
    margin-top:40px;
}}

.browse-title h3 {{
    color:white;
    font-size:2rem;
    letter-spacing:8px;
    margin:0;
    font-weight:300;
}}

.browse-title span {{
    width:80px;
    height:3px;
    background:#ff0000;
    border-radius:2px;
}}

@media (max-width:768px) {{

    .browse-title h3{{
        font-size:1.2rem;
        letter-spacing:4px;
    }}

    .browse-title span{{
        width:50px;
    }}
}}
.browse-title {{
    display:flex;
    align-items:center;
    justify-content:center;
    gap:15px;
    margin-top: 20px;
}}

.browse-title span {{
    width:60px;
    height:2px;
    background:#ff0000;
}}

.browse-title h3 {{
    font-size:1.7rem;
    color:white;
    letter-spacing:6px;
    text-transform:uppercase;
}}

.footer-link {{
    color: #ff0000;
    font-weight: bold;
}}

.social-icons {{
    display:flex;
    justify-content:center;
    gap:35px;
    margin-bottom:25px;
}}

.social-icons a {{
    color:white;
    font-size:2rem;
    transition:0.3s ease;
}}

.social-icons a:hover {{
    color:#ff0000;
    transform:translateY(-3px);
}}
.social-icons {{
    display:flex;
    justify-content:center;
    gap:35px;
    margin-bottom:25px;
    padding-bottom:25px;
    border-bottom:1px solid rgba(255,255,255,0.15);
}}
.container {{
    width:90%;
    max-width:1200px;
    margin:auto;
}}

.league-link {{
    text-decoration:none;
    color:white;
}}

.league-panel {{
    display:flex;
    justify-content:space-between;
    align-items:center;

    margin:30px 0;
    padding:40px;

    border-radius:20px;

    box-shadow:0 10px 30px rgba(0,0,0,.4);

    transition:0.3s ease;
}}

.league-panel:hover {{
    transform:translateY(-6px);
}}

.psl-panel {{
    background:#OA64BC;
}}

.epl-panel {{ 
    background: #OA64BC;
}}

.league-content {{
    width:50%;
}}

.league-content h2 {{
    font-size:3rem;
    margin-bottom:15px;
}}

.league-content p {{
    font-size:1.2rem;
    line-height:1.7;
    color:#ddd;
}}
@media (max-width:768px){{

    .league-panel{{
        flex-direction:column;
        text-align:center;
    }}

    .league-content{{
        width:100%;
    }}

    .psl-logo,
    .epl-logo{{
        width:200px;
        height:auto;
    }}

    .hero-content h1{{
        font-size:3rem;
    }}
}}

.league-image img {{
    width:250px;
    height: 150px;
}}

.archive-btn {{
    display:inline-block;

    margin-top:25px;
    padding:15px 30px;

    background:#ff0000;
    color:white;

    border-radius:8px;

    font-weight:bold;
    letter-spacing:1px;
}}

.epl-btn {{
    background:#8a2be2;
}}

.intro-banner{{
    width: 90%;
    max-width: 1200px;

    margin-left: auto;
    margin-right: auto;
    
    padding: 12px 20px;

    text-align: center;
    font-size: 2rem;

    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 12px;
}}

.stats-section{{
    width:90%;
    max-width:1200px;
    position: relative;
    margin-top:-40px auto 30px auto;
    padding:30px;
    z-index:10;
    margin-left: auto;
    margin-right: auto;

    display:flex;
    justify-content:space-around;
    flex-wrap:wrap;
    gap:20px;

    background:rgba(255,255,255,0.03);
    border:1px solid rgba(255,255,255,0.1);
    border-radius:20px;

    box-shadow:0 10px 30px rgba(0,0,0,0.4);
}}

.stat-card{{
    text-align:center;
    min-width:200px;
}}

.stat-card i{{
    font-size:2rem;
    color:#ff0000;
    margin-bottom:10px;
}}

.stat-card h2{{
    font-size:3rem;
    margin:10px 0;
    color:white;
}}

.stat-card p{{
    color:#cccccc;
    letter-spacing:2px;
    font-size:0.9rem;
}}
.league-image img{{
    width: 180px;    
    height: auto;
}}

</style>

</head>
<body>

<a href="https://footballarchive.co.za" style="text-decoration:none; color:inherit;">
<header>
 <img src="badges/footballarchive.png" alt ="Main Logo" class="main-logo-left">

    <h1>
        <span class="the-word">THE</span> FOOTBALL ARCHIVES
    </h1>

 <img src="badges/footballarchive.png" alt ="Main Logo" class="main-logo-right">   
     <p>Historical league tables, results, statistics and all seasons archives</p>
</header>
</a>

<div class="intro-banner">
   <p> The every football fan book...</p>
</div>

<section class="hero">
    <div class="hero-content">
        <h2>Explore The</h2>
        <h1>Football History</h1>

        <p>
            Relive the seasons, the teams, the players
            and the results that shaped the season.
        </p>
    </div>
</section>

<section class="stats-section">

    <div class="stat-card">
        <i class="fa-solid fa-trophy"></i>
        <h2>12</h2>
        <p>SEASONS ARCHIVED</p>
    </div>

    <div class="stat-card">
        <i class="fa-solid fa-shield-halved"></i>
        <h2>200+</h2>
        <p>CLUBS</p>
    </div>

    <div class="stat-card">
        <i class="fa-solid fa-futbol"></i>
        <h2>3,800+</h2>
        <p>MATCHES</p>
    </div>

    <div class="stat-card">
        <i class="fa-solid fa-calendar-days"></i>
        <h2>7+</h2>
        <p>YEARS OF HISTORY</p>
    </div>

</section>

<div class="browse-title">
    <span></span>
    <h3>BROWSE ARCHIVES</h3>
    <span></span>
</div>

<div class="container">

    <a href="https://psl.footballarchive.co.za" class="league-link">

        <div class="league-panel psl-panel">

            <div class="league-content">
                <h2>PSL SEASONS</h2>

                <p>
                    Premier Soccer League season archives,
                    results, tables, top scorers and
                    memorable moments.
                </p>

                <div class="archive-btn">
                    VIEW PSL ARCHIVES
                </div>
            </div>

            <div class="league-image">
                 <img src="badges/psl-logo.png" alt="PSL League" class="psl-logo">
            </div>

        </div>

    </a>

   <a href="https://epl.footballarchive.co.za" class="league-link">

        <div class="league-panel epl-panel">

            <div class="league-content">
                <h2>EPL SEASONS</h2>

                <p>
                    English Premier League season archives,
                    results, tables, top scorers and
                    memorable moments.
                </p>

                <div class="archive-btn epl-btn">
                    VIEW EPL ARCHIVES
                </div>
            </div>

            <div class="league-image">
                <img src="badges/epl-logo.png" alt="EPL Logo" class="epl-logo">
            </div>

        </div>

    </a>

</div>


</div>
<section class="features">

<div class="feature">
    
    <h3>Historical Seasons</h3>
</div>

<div class="feature">
    
    <h3>Statistics</h3>
</div>

<div class="feature">
    
    <h3>Upcoming Games</h3>
</div>

<div class="feature">
    
    <h3>Record Games</h3>
</div>

</section>



<footer>

   <div class="social-icons">

    <a href="https://www.facebook.com/share/19GZ5SwJUc/" target="_blank">
        <i class="fa-brands fa-facebook-f"></i>
    </a>

    <a href="https://x.com/yourpage" targer="_blank">
        <i class="fa-brands fa-x-twitter"></i>
    </a>

    <a href="Tiktok.com/@yourpage" target="_blank">
        <i class="fa-brands fa-tiktok"></i>
    </a>

    <a href="https://youtube.com/@yourpage"  class="fa-brands fa-youtube"></i>
    </a>

</div>

    <p>© 2026 Football Archive South Africa</p>

    <p class="footer-link">
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
