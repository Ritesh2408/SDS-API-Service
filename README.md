# SDS-API-Service
An API which can take input from users and can perform CRUD operations with the user data.

## Guide
1) First make sure you have Flask installed ,SQLALCHEMY and neccesary imports installed.
 
Then you will need to set up flask app by using this command at your command prompt.

FOR WINDOWS 
```bash
set FLASK_APP= app/name_of_your_python_script.py
```
FOR MACOS use export instead of set.

2) Then run this command at your Command Prompt.
```bash
flask db init
```
3) Then set up migrations by running this command.
```bash
flask db migrate -m "any message here"
````
4) Run your python file by running this command.
```bash
python app.py
```
## This is how it looks: 
  ## Homepage
  ![](/images/Homepage.png)
  
  ## Adding Student
  ![](/images/Add.png)
  
  ## Editing Student's Info
  ![](/images/Update.png)
  
## Contributing
As a newbie , any suggestions regarding the code or regarding writing readme are welcome.
