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
    <style>
        .center {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 50%;
        }
        body {
        font-family: 'IBM Plex Sans', sans-serif;
        color: white !important;
        background-color: black !important;
        }

        h1 {
        font-family: 'IBM Plex Mono', monospace;
        font-weight: 600 !important;
        text-align: center;
        font-size:5vw !important;
        }

        h2 {
        font-family: 'IBM Plex Mono', monospace;
        font-weight: 600 !important;
        text-align: center;
        font-size:3vw;
        }

        a {
        color: #46b966;
        text-decoration: none !important;
        }

        a:hover {
        color: #17B2B5 !important;
        }

        .logoPic {
        width: 70%;
        margin: auto;
        display: block;
        }

        .header {
        background-color: #0e2f44;
        }

        ul {
        display: table;
        margin: 0 auto;
        }
    </style>
    <h1>Smogon API</h1>
    <p>
    <image src="https://www.dropbox.com/s/u4ognce7sevfkgx/smogonBanner.png?dl=1" style="width:600px;height:150px;" class="center"></image><br />
    Welcome to the Smogon API Project! This project is aimed at allowing developers 
    to access all of the data on <a href="https://smogon.com">Smogon</a> using API-style endpoints, in order
    to perform analysis or present different views. 
    </p>
    <p> You can find a list of the different endpoints that we have <a href="/docs">here</a>. 
    """
