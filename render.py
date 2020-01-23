from flask import Flask,render_template,request,send_file
import os
from pymongo import MongoClient
from flask_pymongo import PyMongo
import csv
client=MongoClient("mongodb+srv://HerokuUser:herokupassword@cluster0-cglnu.mongodb.net/test?retryWrites=true&w=majority")   
db=client.get_database("OflUsers")
rec=db.fileUploads
_id="English"

TranslationLibrary=dict()
app=Flask(__name__)



@app.route('/',methods=['GET'])
def renderIndex():
    return render_template('index.html')
@app.route('/download',methods=['POST','GET'])
def handledownload():
    global _id
    
    if request.method=='POST':
        data=request.get_json()
        console.log(data)
        # making the id to be non array
        _id=data['language']

        del data['language']
        for key,val in data.items():
            
            if key in TranslationLibrary.keys():
                
                TranslationLibrary[key].append(val)
            else:
                TranslationLibrary[key]=[val]
        TranslationLibrary['_id']=_id
        writeToDatabase(TranslationLibrary,_id)
        print(TranslationLibrary)
        TranslationLibrary.clear()
        return "{message:success}"

    else:
        
        

        output = rec.find_one({'_id': _id})
        if output:
            with open('output.csv','w',newline="",encoding="utf-8") as f:
                write=csv.writer(f)
                col1=output['Word_in_English']
                col2=output['translation']
                if len(col1)>1 and len(col1)==len(col2):
               
                    write.writerow(['Word_in_English','translation'])
                    for i in range(len(col1)):
                        write.writerow([col1[i],col2[i]])
        

                f.close()

            
        return send_file('output.csv',as_attachment=True,cache_timeout=1)

def writeToDatabase(TranslationDictionary,language):
    output = rec.find_one({'_id': language})
    if output:
        print(TranslationDictionary['Word_in_English'])
        rec.find_one_and_update(
            {'_id': language},
         
               { '$push': {
                            'Word_in_English': {
                                '$each': TranslationDictionary['Word_in_English']
            }
        }})
        
        
        rec.find_one_and_update(
            {'_id': language},
            {
                    '$push': {
                            'translation': {
                                '$each': TranslationDictionary['translation']
            }
        }

        })

    else:
        rec.insert_one(TranslationDictionary)
    


if __name__ == "__main__":
    app.run(debug=True)
