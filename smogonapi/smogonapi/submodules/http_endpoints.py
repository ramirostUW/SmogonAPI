"""
This function contains all of the endpoints that
return raw html.
"""

from fastapi import APIRouter
from fastapi.responses import HTMLResponse

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
def root ():
    """
    This functions returns the splash page for the API.
    """
    return """
    <html lang="en">

        <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>SmogonAPI</title>
        <style>

            html {
            box-sizing: border-box;
            }

            body {
            margin: 0;
            }

            /* CSS for main element */
            .intro {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            width: 100%;
            height: 520px;
            background: linear-gradient(to bottom, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.5) 100%), url("https://wallpaperaccess.com/full/216040.jpg");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            }

            .intro h1 {
            font-family: sans-serif;
            font-size: 60px;
            color: #fff;
            font-weight: bold;
            text-transform: uppercase;
            margin: 0;
            }

            .intro p {
            font-size: 20px;
            color: #d1d1d1;
            text-transform: uppercase;
            margin: 20px 0;
            }

            .intro button {
            background-color: #5edaf0;
            color: #000;
            padding: 10px 25px;
            border: none;
            border-radius: 5px;
            font-size: 20px;
            font-weight: bold;
            cursor: pointer;
            box-shadow: 0px 0px 20px rgba(255, 255, 255, 0.4)
            }

            *, *:before, *:after {
            box-sizing: inherit;
            }

            .column {
            font-family: Arial, Helvetica, sans-serif;
            float: left;
            width: 33.3%;
            margin-bottom: 16px;
            padding: 0 8px;
            }

            .card {
            box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
            margin: 8px;
            }

            .about-section {
            font-family: Arial, Helvetica, sans-serif;
            padding: 50px;
            text-align: center;
            background-color: #474e5d;
            color: white;
            }

            .container {
            padding: 0 16px;
            }

            .container::after, .row::after {
            content: "";
            clear: both;
            display: table;
            }

            .card_title {
            color: grey;
            }

            .card_button {
            border: none;
            outline: 0;
            display: inline-block;
            padding: 8px;
            color: white;
            background-color: #000;
            text-align: center;
            cursor: pointer;
            width: 100%;
            }

            .card_button:hover {
            background-color: #555;
            }

            @media screen and (max-width: 650px) {
            .column {
                width: 100%;
                display: block;
            }
            }
        </style>
        </head>

        <body>
        <main>
            <div class="intro">
            <h1>Smogon API</h1>
            <p>Access to Smogon data directly in your app or program</p>
            <a href="#what_is_this"><button>Learn More</button></a>
            </div>
            </div>
        </main>

        <div class="about-section">
            <h1 id="what_is_this">What is this?</h1>
            <p>This project is aimed at allowing developers to access all of the data on <a href="https://smogon.com">Smogon</a> 
            using API-style endpoints, in order to perform analysis or present different views.
            It is a REST API with easy-to-use endpoints that packages the data publicly 
            available data from Smogon, ready to be used by your own apps and tools.</p>
            <p>You can find a list of the different endpoints that we have <a href="docs">here</a>. </p>
        </div>
        
        <h2 style="text-align:center; font-family: Arial, Helvetica, sans-serif;">Example Uses</h2>
        <div class="row">
            <div class="column">
            <div class="card">
                <img src="https://s3.amazonaws.com/colorslive/png/2214673-xFZLT5eWE-4JvrhA.png" 
                alt="Jane" class="crop" style="width:100%; height: 290px">
                <div class="container">
                <h2>Analyze the data!</h2>
                <p class="card_title">For: Data Scientists</p>
                <p>Using our API, you can use analytical tools and languages like R to 
                    run stats and make charts on Smogon data.
                </p>
                <p><button class="card_button">More Info</button></p>
                </div>
            </div>
            </div>
        
            <div class="column">
            <div class="card">
                <img src="https://sixprizes.com/wp-content/uploads/2013/12/professor-oak-on-computer-1.jpg"
                object-fit: cover; alt="Mike" class="crop" style="width:100%;height: 290px;">
                <div class="container">
                <h2>Make alternate views!</h2>
                <p class="card_title">For: Developers</p>
                <p>Want to practice web development? Make a Smogon clone with data directly from the source!</p>
                <p><button class="card_button">More Info</button></p>
                </div>
            </div>
            </div>
            
            <div class="column">
            <div class="card">
                <img src="https://staticc.sportskeeda.com/editor/2022/06/0e580-16547201167528-1920.jpg" 
                alt="John" class="crop" style="width:100%; height: 290px">
                <div class="container">
                <h2>Build the perfect team!</h2>
                <p class="card_title">For: Trainers & Competitors</p>
                <p>Looking to win a VGC regional? Use our data to construct the perfect team for the meta!</p>
                <p><button class="card_button">More Info</button></p>
                </div>
            </div>
            </div>
        </div>
        </body>

    </html>
    """
