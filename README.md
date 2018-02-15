##Sysbot
#### Slack Client to notify team member of the activity we do on servers

 
  Notify Developers of server activities. 
  Write you message in single quotes and press enter. It wil push it to a slack channel. 

The client make use of [Sack Incoming Webhooks](https://api.slack.com/incoming-webhooks).
 ####Install and Setup
 
 
 
 you will need python2.7 and virtualenv already to follow these intrunctions. 
 ```bash
 $ git clone https://github.com/nitigyas/sysbot.git
 $ cd sysbot

```

create a virtualenv for sysbot
```bash
mkvirtualenv sysbot
```
 
you should be in virtualenv now. execute the following commands
```bash
(sysbot) $ python setup.py install
(sysbot) $ export SLACK_WEBHOOK_URL='https://SecretSite.Shh/SecretURL'
(sysbot) $ sysbot.py "Hello World!!"
```


 
 **Example: 1**
 ```bash
$ sysbot 'Removed Empty log file from /sys/log/'
```

 Output on Slack:
 
 **nsharma** at **web0** : Removed Empty log file from /sys/log/
 
**Example: 2**
  ```bash
$ sysbot nitigyas mysql14 'Starting MySQL'
```
 
 Output on Slack:
 
 **nitigyas** at **mysql14** : Starting MySQL
 
 