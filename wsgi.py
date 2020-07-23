HTML = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href=./static/styles.css>
    <title>Узнать ip</title>
  </head>
  <body>
   <p id="content">Ваш ip адрес: {}</p>
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
    html_as_bytes = HTML.format(environ["HTTP_X_REAL_IP"]).encode('utf-8')
    return iter([html_as_bytes])
