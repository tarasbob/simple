import additional_functions
from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def main_page():

  print request
  for key in request.__dict__:
    print key, request.__dict__[key]

  print 'request args'
  print request.args

  special_word = request.args.get('firstname', '')

  web_page = '''
  <!DOCTYPE html>
  <html>
  <body>

  <h1>My First Heading</h1>
  <h2>{0}</h2>

  <p>My first paragraph.</p>

  <form>
    First name:<br>
    <input type="text" name="firstname" value="{1}"><br>
    <input type="submit" value="Submit">
  </form>

  </body>
  </html>'''.format(special_word, additional_functions.capitalize(special_word))
  return web_page

if __name__ == '__main__':
  app.run(debug = True)
