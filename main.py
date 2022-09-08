
from typing import Union
from fastapi import FastAPI,  Header
from fastapi.responses import RedirectResponse, HTMLResponse

app = FastAPI()


@app.get("/")
async def redirect_typer(user_agent: Union[str, None] = Header(default=None)):
    print(123,user_agent)
    return RedirectResponse("http://play.google.com/store/apps/details?id=com.truecaller&hl=en")


@app.get("/manh")
async def main():
    content = """
        <head>
<meta property="og:title" content="The Rock" />
<meta property="og:type" content="video.movie" />
<meta property="og:url" content="https://www.imdb.com/title/tt0117500/" />
<meta property="og:image" content="https://ia.media-imdb.com/images/rock.jpg" />
    <script src="http://code.jquery.com/jquery-latest.min.js" type="text/javascript"></script>
    <title>Document</title>

</head>
<body>
    
    <script>
        $(document).ready(function (){
            if(navigator.userAgent.toLowerCase().indexOf("android") > -1){
                window.location.href = 'http://play.google.com/store/apps/details?id=com.truecaller&hl=en';
            }
            else if(navigator.userAgent.toLowerCase().indexOf("iphone") > -1){
                window.location.href = 'http://itunes.apple.com/lb/app/truecaller-caller-id-number/id448142450?mt=8';
            }
            else window.location.href = 'http://itunes.apple.com/lb/app/truecaller-caller-id-number/id448142450?mt=8';
        });
    </script>
</body>
    """
    return HTMLResponse(content=content)