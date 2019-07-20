import pandas as pd
from flask import Flask,jsonify,request,make_response
import json
from flask_cors import CORS, cross_origin
import pickle

df = pd.read_csv("song_data.csv")
filep=open("KM.pkl","rb")
km=pickle.load(filep)
labels = list(km.labels_)
df['cluster'] = labels

def musicRec(sname):
    print("FGFFGFGG")
    cno=float(df[df.song_name==sname].cluster)
    gk=df[df.cluster==cno]
    print("bvnbnbs")
    mlist=list(gk.song_name)[2:12:1]
    print("vnvnvnvn")
    return(mlist)

app = Flask(__name__)
cors = CORS(app)
@app.route('/song', methods=['POST'])
def getReviewDetails():
    try:
        song_no = request.json['value']
        print(song_no)
    except:
        return make_response(jsonify({'error' :'bad request'}),400)
    try:
        mlist=musicRec(song_no)
        
    except:
        return make_response(jsonify({'error' :'internal server error'}),500)
    
    return make_response(jsonify({"mlist": mlist}),200)

if __name__ == "__main__":
    app.run(host= '0.0.0.0',port=5004,debug=True)
