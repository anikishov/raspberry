Raspberry service for temperature return.

`cd /opt/`
`git clone git@github.com:anikishov/me.git && cd me`
`python3 -m venv env`
`pip3 install -r requirerments.txt`
`cp /opt/me/deploy/me.service /etc/systemd/system/me.service`
`systemctl enable me.service`
`service me start`

Example:

`curl http://127.0.0.1:5000/temp`
```
Date: Thu, 27 Feb 2020 09:56:48 GMT
Content-Type: application/json
Content-Length: 58
Connection: keep-alive
Strict-Transport-Security: max-age=604800

{
  "hostname": "raspberrypi",
  "temperature": "32.0"
}
```
