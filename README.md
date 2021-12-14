## Installation dependencies

```sh
$ sudo apt install libopencv-dev python3-opencv
$ sudo apt install python3-pip
$ pip3 install flask
```

## Use

```sh
$ git clone git@github.com:yan-wyb/rtsp-web-appliation.git
$ cd rtsp-web-appliation
$ python3 rtsp.py --device X
* Debug mode: on
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
```

**Note: X is the number for you camera**

Open the link , you can see a sample demo


If you use cctv camera or ip camera,

```
rtsp://username:password@ip_address:554/user=username_password='password'_channel=channel_number_stream=0.sdp
```
