### California_House_Pricing_End_To_End_Project

### Software and Tools Requirements 

1. [Github Account](https://github.com)
2. [VSCodeIDE](https://code.visualstudio.com)
3. [HerokuAccount](https://heroku.com)
4. [GitCLI](https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)

### Create Environment In VS Code 
deactivate all environment-->deactivate 

Create a new environment
'''
conda create -p venv python==3.7 -y
'''
py -m venv Saurabh_Environment
'''
### Activate Created Environment In VS Code 
'''
Saurabh_Env\Scripts\activate
'''
### Install Requirements.txt
'''
pip install -r requirements.txt
'''
### Configuration of GIT With Git hub account
'''
git config --global user.name "raisaurabh44"
git config --global user.email "saurabhrai.aiml.tech@gmail.com"
'''
### Git CLI Command 
git add --- to add 1 file to github account 

git add .  --- to add all file to github account 

git status --- to see file adition status 

git commit --- to commit all done in github account

git commit -m "Updated Files" -- to commit all done in github account with message

git push origin main -- Pushed all data to github server 

For Large file to upload in github

git init --- initialize git 

git remote add origin https://github.com/raisaurab44/California_House_Priceing_End_To_End_Projrct.git --- Initializing repo

git lfs install ---- Install LFS ( Large file system ) for file >100mb 

git lfs track "*.zip"  # replace *.zip with your large file types

git add .gitattributes ----afdding this for large file 

git push origin main --force ----for force upload

### Now Next Step is Deployment in Render Cloud 

We are using Procfile its giving command to Render Server - Related To Gunicorm 

We use Gunicorn as it pure Python HTTP server for WSGI application as it allows to run application concurrently 

FROM python:3.10-slim
Uses a lightweight Python 3.10 base image, which is stable and compatible with scikit-learn models.

WORKDIR /app
Sets /app as the working directory inside the container.

COPY requirements.txt .
Copies dependency list into the container.

RUN pip install --no-cache-dir -r requirements.txt
Installs Python dependencies without keeping cache, reducing image size and memory usage.

COPY . .
Copies the entire application code, models, and templates into the container.

EXPOSE 10000
Documents that the app listens on port 10000 (Render’s default internal port).

CMD ["gunicorn", "app:app", "--workers=1", "--threads=1", "--bind=0.0.0.0:10000"]
Starts the Flask app using Gunicorn with a single worker and thread to prevent memory issues on Render’s free tier.

### Now Next We are Docarizing the app To create Dockerfile image 
Explanation (Brief but Important)

type: web
→ This is a web service

env: docker
→ Tells Render to use your Dockerfile

plan: free
→ Uses free tier (512 MB RAM)

dockerfilePath: ./Dockerfile
→ Uses Dockerfile from root

autoDeploy: true
→ Auto redeploy on every Git push

envVars
→ Secrets (API keys) set in Render UI

### OutPUT LINK
https://california-house-pricing-end-to-end-5kwp.onrender.com/