{
    "python.pythonPath": "env\\Scripts\\python.exe"
}from flask import Flask,request
from datetime import datetime
import re
from flask import render_template
import pandas as pd
import numpy as np
from flask import url_for
from flask import jsonify
import os
import json
from flask_jsonpify import jsonpify
from sklearn.metrics.pairwise import cosine_similarity
from flask import Response


app = Flask(__name__)


@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "details copy.html",
        item=[],
        date=datetime.now()
    )

@app.route('/index_get_data')
def stuff():
  # Assume data comes from somewhere else
  SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
  json_url = os.path.join(SITE_ROOT, "static", "data.json")
  data = json.load(open(json_url,encoding="utf-8"))
  return jsonify(data=data)

@app.route('/get_candidat/<id>')
def get_candidat(id):
  # Assume data comes from somewhere else
  SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
  json_url = os.path.join(SITE_ROOT, "static", "data.json")
  data = json.load(open(json_url,encoding="utf-8"))
  d=jsonify(data=data).get_json()
  id=id.replace('SLASH','/')
  print(id)
  item=""
  for var in d.get("data"):
      if var.get("url")==id:
          item=var
  print(item)
  return render_template("details copy.html",item=item)
    
@app.route('/data')
def index():
  return render_template('data.html')   

@app.route('/getsimilarity/<id>')
def getsimilarity(id):
  
  SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
  json_url = os.path.join(SITE_ROOT, "static", "data.json")
  data=pd.read_json(json_url)
  v = cosine_similarity(data.drop(columns=["url","profil"]))
  #get selected profile
  id=id.replace('SLASH','/')
  #id of selected profile
  idx=data[data["url"]==id].index[0]
  sim_scores = list(enumerate(v[idx]))
  sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
  sim_scores = sim_scores[1:11]
  data["sim"]=0.0
  result=data[0:0]
  print(result)
  for i in range(0,len(sim_scores)):
    result=result.append(data.iloc[sim_scores[i][0],:], ignore_index = False)
    result.iloc[i,18]=sim_scores[i][1]

  result=result.append(data.iloc[idx,:], ignore_index = False)
  result.iloc[-1,18]=1
  
  df_list = result.values.tolist()
  JSONP_data = jsonpify(data=df_list)
  print((df_list))
  JSONP_data

  return JSONP_data


########### charts
@app.route('/home')
def home():
    data = pd.read_csv("DATA_FINAL_NOSKILLS_URL.csv")
    #groupby gender
    s=data.Gender.value_counts().rename({1: "Femme", 0: "Homme"})
    indexes=list(s.index)
    values=list(data.Gender.value_counts())

    #groupby profile
    s1=data.groupby("profil").count()["Unnamed: 0"].sort_values(ascending=False)[:9]
    indexes_profil=list(s1.index)
    values_profil=(s1.values)
    values_profil=values_profil.tolist()
    #groupby graduation
    s2=data.groupby("YoungGraduate").count()["Unnamed: 0"].sort_values(ascending=False)
    s2=s2.rename({1: "Jeune diplome", 0: "Ancien diplome"})
    indexes_grad=list(s2.index)
    values_grad=(s2.values)
    values_grad=values_grad.tolist()
    #groupby localisation
    s3=data.location.value_counts().rename({1: "En Tunisie", 0: "A l'etranger"})
    indexes_local=list(s3.index)
    values_local=(s3.values)
    values_local=values_local.tolist()
    # groupby Turnover
    s4=data.Turnover.value_counts().rename({1: "A tendance a changer le poste", 0: "n'a pas tendance a changerle poste"})
    indexes_turnover=list(s4.index)
    values_turnover=(s4.values)
    values_turnover=values_turnover.tolist()
    #groupby diploma
    s5=data.groupby(["Ingénieur","Licence","Master","Docteur","BTS","BTP"])["Unnamed: 0"].count().sort_values(ascending=True)  
    values_diploma=[]
    for i in range(0,s5.index.size-1):
        values_diploma.append(int(s5.values[list(s5.index.get_level_values(i)).index(1)]))
    indexes_diploma=list(s5.index.names)
 
    return render_template('chartjs.html',values=[values,json.dumps(values_profil),values_grad,values_local,values_turnover,values_diploma],indexes=[indexes,indexes_profil,indexes_grad,indexes_local,indexes_turnover,indexes_diploma])

 
@app.route('/addcandidat')
def addcandidat():
  skills=["JavaScript","SQL","NoSQL","Node.js","Express.js","Koa.js","Hapi.js","AngularJS","React.js","JQuery","Bash","Nginx","C","C++","HTML5","CSS","REST"
                   ,"SASS","PostCss","Webpack","Webpack","Gitlab","Linux","Embedded C","Embedded C++","Java","JEE","Microservices","Intégration continue","Docker","AWS","NodeJS",
                   "Ext.js","HTML","MongoDB","MySQL","Spring","SOA","SOAP","Git","SVN","Jira","Confluence","Spring Boot","Spring Security","Java 8","PHP","Symfony","Architecture RESTful"
                   ,"GIT","CMS","Drupal","Scrum","Analyse fonctionnelle","Testing","Rédaction"]
          
  return render_template('ajout_candidat.html',skills=skills)   


weights={'Web Back-End':{'JavaScript':1,'SQL':3,'NoSQL':2,'Node.js':3,'Express.js':3,'Koa.js':1,'Hapi.js':1,'AngularJS':1,
                         'React.js': 1 ,'JQuery':1,'Bash':1,'Nginx':1,'C':1,'C++':1},
         'Web Front-End':{'JavaScript':3,'HTML5':3,'CSS':3,'REST':3,'React.js':3,'SASS':1,'PostCss':1,'Webpack':1,'Gitlab':1},
         'Embarqué Middleware':{'C':2,'C++':2,'Linux':3,'Embedded C':3,'Embedded C++':3},
         'Technical Lead/ Architecte JEE':{'Java':3,'JEE':3,'Microservices':3,'Intégration continue':3,'Docker':3,'AWS':3},
         'FullStack JS':{'NodeJS':3,'JavaScript':3,'AngularJS':3,'Ext.js':3,'JQuery':2,'HTML':2,'CSS':2,'MongoDB':2,'MySQL':2},
         'JAVA/JEE':{ 'Java':3,'JEE':3,'Spring':3,'SOA':1,'SOAP':1,'REST':1,'Microservices':3,'Git':3,'SVN':2,'Jira':1,'Confluence':1,'Spring Boot':3, 'Spring Security':3,'Java 8': 3},
         'PHP/Symfony':{'PHP':3,'Symfony':3,'Architecture RESTful':2,'GIT':2},
         'DRUPAL':{'PHP':3,'CMS':1,'Drupal':3 ,'HTML':1 ,'CSS':1 ,'MySQL':1 ,'Symfony':2 ,'JavaScript':2, 'GIT':2},
         'Product Owner':{'Scrum':3,'Analyse fonctionnelle':3,'Testing':3 ,'Rédaction':3}}
@app.route('/candidat/addcandidat/',methods=['GET','POST'])

def addcandidat1():
 
  new_freq = request.get_data()
  skills=request.json['skills']
  skills_duree=request.json['skills_duree']
  gender=request.json['gender']
  jeuneDip=request.json['jeuneDip']
  nbcnx=request.json['nbcnx']
  nbprojets=int(request.json['nbprojets'])
  location=request.json['location']
  grade=request.json['grade']
  print(nbcnx)
  print(nbcnx=="+500")
  if gender=="Homme":
    gender=0
  else:
    gender=1
  if location=="Oui":
    location=1
  else:
    location=0
  if nbcnx=="+500":
    nbcnx=1
  else:
    nbcnx=0
  if jeuneDip=="Oui":
    jeuneDip=1
  else:
    jeuneDip=0
  
  SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
  json_url = os.path.join(SITE_ROOT, "static", "DATA_FINAL_withSKILLS_URL.json.") 
  data=pd.read_json(json_url)
  
  newcandid= pd.DataFrame(0, index=np.arange(1), columns=data.columns)
  print(newcandid.columns)
  newcandid.iloc[0,1]=location
  newcandid.iloc[0,2]=nbcnx
  newcandid.iloc[0,3]=nbprojets
  newcandid.iloc[0,5]=jeuneDip
  newcandid.iloc[0,6]=gender
  if grade=="Baccalauréat":
    newcandid.iloc[0,11]=1
  elif grade=="Docteur":
    newcandid.iloc[0,12]
  elif grade=="Ingénieur":
    newcandid.iloc[0,13]
  elif grade=="Licence":
    newcandid.iloc[0,14]
  elif grade=="Master":
    newcandid.iloc[0,15]
  else:
    newcandid.iloc[0:16]=1
 
 
  for  i in range(0,len(skills)):
    newcandid.loc[0,skills[i]]=int(skills_duree[i])

  d=newcandid.to_dict('index')
  dict={}
  for key in weights.keys():
    score=cal(d,key,i)
    print(score)
    dict[key]=score
  res=sorted(dict.items(), key=lambda x: x[1], reverse=True)
  if res[0][1]!=0:
    d.get(0)["profil"]=res[1][0]
    d.get(0)["score"]=res[0][1]
   
  else:
    d.get(0)["profil"]="Other"
 
  print('SCOOOOORE' + str(d.get(0)["score"]))
   
  print('PROFIIIL' + str(d.get(0)["profil"]))
  data=data.append(pd.DataFrame([d.get(0)]), ignore_index = False)#append
  print(pd.DataFrame([d.get(0)]))
  v = cosine_similarity(data.drop(columns=["url","profil"]))# matrix cosine similarity
  print(data.iloc[-1,8])

  sim_scores = list(enumerate(v[-1]))
  sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
  sim_scores = sim_scores[1:11]
  result=data[0:0]
  
  for i in range(0,len(sim_scores)):
    result=result.append(data.iloc[sim_scores[i][0],:], ignore_index = False)
  df_list = result.values.tolist()
  JSONP_data = jsonpify(data=df_list)
  print(JSONP_data)
  return JSONP_data




def cal(d,profil,index):
  score=0
  skills=weights.get(profil)
  for skill in skills: 
    score=score+skills[skill]*d.get(0)[skill]
  return score
def calculscore(d,i):
  dict={}
  for key in weights.keys():
    score=cal(d,key,i)
    print(score)
    dict[key]=score
  res=sorted(dict.items(), key=lambda x: x[1], reverse=True)
  if res[0][1]!=0:
    d.get(0)["profil"]=res[1][0]
    d.get(0)["score"]=res[0][1]
   
  else:
    d.get(0)["profil"]="Other"
  return d