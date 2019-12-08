# Question-analyzer
Built a NLP based Deep-Learning model for multi-classification of question categories (what, when, who, affirmaton, unknown) and also developed a web-application using flask.

The classifier is deployed in the Heroku application with the help of a WSGI HTTP Server for UNIX.

#### https://question-analyzer.herokuapp.com/index


## Setting up in Local Machine

#### Step-1 
Clone the Tap search repository and `cd` into the directory.
```bash
git clone https://github.com/sherwin7/Question-analyzer.git

cd Question-analyzer
```

#### Step-2
Check python-3 is inatalled then install pip manager for python-3 and install virtual environment.
```bash
#Checking python is installed
python3 --version 

#Installing pip manager
sudo apt install python3-pip

#Checking pip is installed for python3
pip3 --version

#Installing virtual environment
sudo pip3 install virtualenv
```

#### Step-3
Setting up virtual environment
```bash
#Creating virtual environment
virtualenv -p python3 venv

#Activating the virtual environment venv
source venv/bin/activate
```

#### Step-4
Now we have to install all the dependencies using pip in our virtual environment from requirement.txt.
```python
pip3 install -r requirements.txt
```
* hello
