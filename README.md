## Concepts  

### Instance folder  
A place that stores deployment specific files related to the flak app. Files can be
configuation, databases.  
App instance folder can be accessed with `app.instance_path`  
Doc Link: [Instance Folders](https://flask.palletsprojects.com/en/2.3.x/config/#instance-folders)  

### click   
Click gives an interface to add new command that can be run with `flask`  

### flash  
flash is a transient message storage that is usually used for conveying confiramtion, success, error
message to the user. It's kind of notification pipeline.  
For example, We have a user registered, so we store a congratulatory message in flash and redirect the user to the login page and there we show the congratulatory message stored in flash. To access the flash message 
we need to access `get_flashed_messages()` method in template.  
In same way we can use this to show error message and others knid of notifications. 
* Flash messages are one time accessible, they will be gone as soon as accessed once.
* Flas message are stored using `flash(message, category)`. Here second parameter is optional and contains the knid of message the flash is holding, for example, `success`, `error` etc.

### Methods  
1. **app.teardown_appcontext()** tells Flask to call that function when cleaning up after returning the response.  
