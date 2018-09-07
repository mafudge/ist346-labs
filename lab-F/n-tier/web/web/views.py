from django.http import HttpResponse


def index(request):
    base_url = '{scheme}://{host}/'.format(
        scheme=request.scheme, host=request.get_host()
    )
    html_template = '''
    <!DOCTYPE html>
    <html>
        <head>
            <meta charset="UTF-8">
            <title>Your APP NAME</title>
            <link rel="stylesheet"
                href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
                integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
                crossorigin="anonymous">
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
                integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
                crossorigin="anonymous">
                </script>
        </head>
        <body>
            <header class="container">
                <section class="row">
                    <article class="col-6">
                        <h1>APP LOGO</h1>
                    </article>
                    <article class="col-6">
                        <nav class="nav">
                            <a href='{url_admin}' class="nav-link">{url_admin}</a>
                        </nav>
                    </article>
                </section>
            </header>
            <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
                integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
                crossorigin="anonymous">
                </script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js"
                integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q"
                crossorigin="anonymous">
                </script>
        </body>
    </html>
    '''
    html = html_template.format(
        url_admin=base_url + 'admin'
    )
    return HttpResponse(html)
