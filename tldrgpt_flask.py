# importing Flask and other modules
from flask import Flask, request, render_template
from tldrgpt import main_runner

# Flask constructor
app = Flask(__name__)

# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def index():
   
    response="Response will be displayed here..."

    if request.method == "POST":
        # getting input with name = article_url in HTML form
        article_url = request.form.get("article_url")    
        response = main_runner(article_url).removeprefix("\n\n")
    
    return render_template("index.html", response_placeholder=response)



if __name__=='__main__':
    app.run(ssl_context='adhoc')
