html = b"""
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <title>Bash.im random quote</title>
  </head>
  <body>
    <script type="text/javascript" src="https://bash.im/forweb/?u"></script>
    <button id="btn" type="button" class="btn btn-outline-dark" onclick="myfunction()">Random</button>
    <script>function myfunction() {setTimeout(function(){ location.reload(); }, 5000)}</script>
  </body>
</html>
"""

def app(environ, start_response):
    """Simplest possible application object"""
    status = '200 OK'
    response_headers = [
        ('Content-type', 'text/html'),
    ]
    start_response(status, response_headers)
    return iter([html])
