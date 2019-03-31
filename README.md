# awesomeEnvironment
a simple constructor of instances in amazon 

**Clean architecture implemented** :bomb:

It was tested with us-west-1, if you if you are going to use another area of aws please change the ami within models

```python
class Ami(Enum):
    UBUNTU = "ami-06397100adf427136" #ami for your custom zone
```

Requirements:

* python>=3.5
* aws cli
* aws credentials

If you use virtualenv
```console
pip install -r requirements.txt
```

please configure your aws credentials with
```console
aws configure
```
and follow the aws instructions.

Make sure that the user of iam that you have has full access of amazon ec2.

This script is made to receive the following structure
```json
{
  "name": "test-env-1",
  "region": "us-west-1",
  "servers": [
    {
      "name": "controller ",
      "deps": [
        "nginx"
      ]
    },
    {
      "hostname": "endpoint ",
      "deps": [
        "wget"
      ]
    }
  ]
}
```

for run the script please do
```console
(venv)foo@bar:~$ python environment.py -env env.json 
```
if if you want to pass the credentials as a parameter you can do it (although it can not always work for you, *I recommend configuring the credentials with amazon directly as mentioned above*)
```console
(venv)foo@bar:~$ python environment.py -env env.json -key <access_key:secret_key>
```

if you want to rest tests
```console
pytest -s -v
```