

1. Sqlite3 io error
* Question
currently I have some trouble with Disk I/O Errors in Code Developments.
I have noticed this problem with two separate programs.

First Neptune AI. This provider offers simple tracking of the training process. To connect to the web service there is a Python package that implements the data transfer to Neptune AI. By default this program uses a cache (a hidden folder .neptune/ in the corresponding project directory). If there is no internet connection at the moment, the data will be cached longer and uploaded afterwards. This works quite well so far. However, for the cache system files are created in the hidden folder and deleted again after successful upload. This asynchronous procedure is sometimes so fast that the file can not be deleted with os.remove(), because it does not exist yet, or is not visible, writable, whatever. 

The second application is Optuna. This is used for hyperparameter optimization. In order not to lose the results and set parameters in case of an error, they can be stored in a sqlite3 database at runtime. The database file is again located in the project directory. After a certain time the disk I/O error occurs when accessing the database (see screenshot). 

I suspect that these errors have a common reason, which lies in the Kubenetes technique to share a file system. I assume you are using pods to connect multiple containers to a shared storage and network resource. Unfortunately I am a amateur in this area but in the context of sqlite3 Connection, for example, there are also problems if the database file is on a cloud like Onedrive.  See: https://stackoverflow.com/questions/47540607/disk-i-o-error-with-sqlite3-in-python-3-when-writing-to-a-database

I think there is room for improvement in this regard. Maybe it's just a configuration thing. 
If you know a workaround, please let me know. Thank you!

* Anwser
