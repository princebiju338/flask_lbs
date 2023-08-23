from flask import Flask,render_template,request 
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def hello():
    if request.method=='POST':
         height = request.form('height')
         print(height)
         weight=weightpredict.predict([float(height)])
         return render_template("index.html",hei = height,wei=weight)
    return render_template("index.html")
if __name__=="__main__":
     app.run()