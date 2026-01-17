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