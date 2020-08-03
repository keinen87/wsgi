HTML = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
    <title>Узнать IP адрес</title>
  </head>
  <body class="bg-info">
    <div class="container">
      <div class="d-flex align-items-center justify-content-center h-100">
        <div class="d-flex flex-column">
          <h1 class="text text-white align-self-center p-2">Ваш IP-адрес</h1>
        </div>
      </div>     
      <div class="row bg-faded">
        <div class="col">
          <div class="bg-light card w-100 h-100 card-block justify-content">
            <h1 class="display-1 text text-muted align-self-center p-2">{}</h1>
          </div>
        </div>
      </div>
    </div>  
  </body>
</html>
"""
print(HTML)
