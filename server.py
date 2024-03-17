from flask_app.controllers import Ryan
from flask_app.models import Ryans
from flask_app.controllers import accounts
from flask_app.models import Accounts
from flask_app.controllers import survey
from flask_app.models import Survey
from flask_app.controllers import posting
from flask_app.models import Postings
from flask_app import app

if __name__=="__main__":
    app.run(debug=True)

#This should remians simple as this is our root for our application