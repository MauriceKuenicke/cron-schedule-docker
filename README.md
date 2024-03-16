#

Docker commands
```sh
docker build -t cron-scheduled-python .
```
```sh
docker run cron-scheduled-python
```

## Cron Structure
```
*    *    *   *    *        command to be executed
-    -    -   -    -
|    |    |   |    |
|    |    |   |    +----- day of the week (0 - 6) (Sunday=0)
|    |    |   +------- month (1 - 12)
|    |    +--------- day of the month (1 - 31)
|    +----------- hour (0 - 23)
+------------- min (0 - 59)
```

Example:
```
* * * * * cd /app/ && python3 hello_world_1.py >> /var/log/hello_world_1.log 2>&1
```
"Every minute, change to the /app/ directory and, if successful, run the Python script
hello_world_1.py, writing both output and any errors into the file /var/log/hello_world_1.log"

2>&1 - This redirects standard error (stderr) to the same place where standard output (stdout) is going. 
Effectively, this means that both the output and any error messages from the script will be written to the 
file /var/log/hello_world_1.log.

## Cron Commands
`crontab -l` - shows current cron jobs