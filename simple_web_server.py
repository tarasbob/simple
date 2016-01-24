import additional_functions
from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def main_page():

  special_word = request.args.get('firstname', '')

  web_page = '''
  <!DOCTYPE html>
  <html>
  <body>

  <h1>My First Heading</h1>
  <h2>{0}</h2>

  <p>My first paragraph.</p>

  <div>
    First name:<br>
    <input type="text" id="inp1" name="firstname" value="nothing"><br>
    <input type="submit" id="btn_submit" value="Submit">
  </div>

  </body>

  <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.0/jquery.min.js"></script>

  <script>

    $(function(){

      $("#btn_submit").click(function() {

        var name_from_edit_box = $("#inp1").val();

        $.get("jesus", { firstname: name_from_edit_box }, function( data ) {
          if (data == 'go_ahead') {
            window.location.href = "/page2";
          }
        });
      });
    });

  </script>

  </html>'''

  return web_page


@app.route('/jesus')
def target():
  first_name = request.args.get('firstname', '')
  print 'received', first_name
  if request.args.get('firstname', '') == 'luba':
    return 'go_ahead'
  return 'stay_here'

@app.route('/page2')
def page2_page():

  web_page = '''
  <!DOCTYPE html>
  <html>
  <body>

  <h1>Page 2</h1>

  <p>My second paragraph.</p>

  </body>
  </html>'''
  return web_page

if __name__ == '__main__':
  app.run(debug = True)
