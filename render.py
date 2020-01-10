from flask import Flask,render_template,request,send_file
import os

import csv
TranslationLibrary=dict()
app=Flask(__name__)
@app.route('/',methods=['GET'])
def renderIndex():
    return render_template('index.html')
@app.route('/download',methods=['POST','GET'])
def handledownload():
    
    
    if request.method=='POST':
        data=request.get_json()
        for key,val in data.items():
            
            if key in TranslationLibrary.keys():
                TranslationLibrary[key].append(val.encode('UTF-8'))
            else:
                TranslationLibrary[key]=[val.encode('UTF-8')]
         
        return "{message:success}"

    else:
        with open('output.csv','w',newline="",encoding="utf-8") as f:
            write=csv.writer(f)
            if len(TranslationLibrary)>1:
                col1,col2=TranslationLibrary.keys()
                write.writerow([col1,col2])
                for i in range(len(TranslationLibrary['Word_in_English'])):
                    write.writerow([TranslationLibrary['Word_in_English'][i].decode('utf-8'),TranslationLibrary['translation'][i].decode('utf-8')])

            f.close()
        return send_file(os.getcwd()+'\output.csv',as_attachment=True,cache_timeout=1)
    
#
if __name__ == "__main__":
    app.run(debug=True)
