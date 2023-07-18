<div align="center">
<p>
</p>
<br>
<div>
   <a href="https://github.com/crisanglemass"><img src="https://img.shields.io/badge/Github-crisanglemass-plasticlogo=github&logoColor=white" ></a>
   <a href="https://redis.io"><img src="https://img.shields.io/badge/redis-passing-plastic?logo=redis&logoColor=red" ></a>
   <a href="https://www.mysql.com"><img src="https://img.shields.io/badge/mysql-passing-plastic?logo=mysql&logoColor=blue" ></a>
   <a href="https://vuejs.org/"><img src="https://img.shields.io/badge/vue-3.0-plastic?logo=Vue&logoColor=red" ></a>
   <br>
   <a href="https://flask.palletsprojects.com/"><img src="https://img.shields.io/badge/flask-2.3.2-plastic?logo=Vue&logoColor=red" ></a>
   <a href="https://www.electronjs.org/"><img src="https://img.shields.io/badge/electron-23.2.0-plastic?logo=Vue&logoColor=red" ></a>
   <a href="https://nodejs.org/"><img src="https://img.shields.io/badge/nodejs-18.16.1-plastic?logo=&logoColor=red" ></a> 
   <img src="https://img.shields.io/badge/License-MIT-plastic?logo=Vue&logoColor=red" >
</div>
<div align="center">Introduction</div>
This project aims to rapidly develop environment of flask_vue_electron and provide beginners with solvable 
development documents for potential issues.

See the [Crisangle Blog](https://www.crisangle.com) for development documents.

<details open>
<summary>Install</summary>

Clone repo and install [requirements.txt](https://github.com/crisanglemass/flask_vue_electron/blob/master/requirements.txt) in a
[**Python>=3.7.0**](https://www.python.org/),[**Nodejs**](https://nodejs.org/) environment.


## Rapid environmental development
Tips:You should ensure you have installed nodejs and python in your device either Windows or Linux,Mac OS.
### Win
```bat
./install.bat
./launch.bat 
```


### Linux
```shell
sudo chomd+x install.sh
bash install.sh 
sudo chomd+x launch.sh
bash launch.sh 
```
## Detailed deployment
### Win
1. Firstly,create virtual environment.
```python 
py -3.9 -m venv venv
venv\Scripts\python -m pip install -r requirements.txt
```
2. Then install the npm envs
```npm
npm install --save
cd web
npm install --save
```
3. Compiles and hot-reloads for development
``` npm
npm run serve
```
4. Compiles and minifies for production
``` npm
npm run build
```
5. start server app
```python
python app.py
```
6. if you want to start electron 
```npm
electron . 
electron-builder --win --x64
#the desktop sofware is produced to file. dist
```

### Linux
To be continued




