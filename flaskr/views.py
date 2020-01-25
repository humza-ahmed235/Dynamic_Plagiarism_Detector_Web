from flask import Flask, request, render_template, Blueprint
from flaskr import Plg_Detect_Methods
import os



bp = Blueprint('ind', __name__)


@bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        f1 = request.files['file1']
        f2 = request.files['file2']

        f1.save("file/fy1.txt")
        f2.save("file/fy2.txt")

        """f3 = open("original.txt","r")
        f4 = open("suspected.txt","r")"""
        f1 = open("file/fy1.txt", "r")
        f2 = open("file/fy2.txt", "r")
        print("after humza ********************")
        #print(Plg_Detect_Methods.get_plg_score(f1,f2))
        score = Plg_Detect_Methods.get_plg_score(f1,f2)
        return render_template("index.html",score=score)
        f1.close()
        f2.close()




    return render_template("index.html")




