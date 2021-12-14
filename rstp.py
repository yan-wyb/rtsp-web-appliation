from flask import Flask, render_template, Response
import cv2 as cv
import argparse
import time

cap_num = 0
width = 1920
height = 1080

rstp = Flask(__name__)

def gen_frames():
    camera = cv.VideoCapture(cap_num)
    camera.set(3,width)
    camera.set(4,height)
    while True:
        start = time.time()
        success, frame = camera.read()
        if not success:
            break
        ret, buffer = cv.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        end = time.time()
        print('inference : ', end - start)


@rstp.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@rstp.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--device", help="the number for video device")
    parser.add_argument("--width", help="width for video capture")
    parser.add_argument("--height", help="height for video catpure")

    args = parser.parse_args()

    if args.device :
        cap_num = int(args.device)
    else :
        sys.exit("video device not found !!! Please use format :--device ")
    
    if args.width :
        width = args.width

    if args.height:
        height = args.height
    
    rstp.run(debug=True)
