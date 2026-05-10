# rock-paper-SCISSORS

##  #HOW TO RUN
1. Make sure you have <a href="https://www.python.org/downloads/" installed.
2. Clone/download the repo and unzip.
3. Open terminal and run "pip install -r requirements.txt".
4. cd into project folder (should say something like user/rock-paper-SCISSORS" and run "python app.py"

Give webcame access, and the model will recognize rock paper scissors from your webcam; capture the image, and play against you randomly.

Model file: keras_model.h5
Labels file: labels.txt
Input image size: 224 x 224
Built using TensorFlow + Keras

Dependencies: flask, tensorflow, numpy, pillow, h5py

TROUBLESHOOTING: 
- if dependency download doesn't work, manually install 
pip install flask
pip install tensorflow
pip install pillow
pip install numpy
pip install h5py
- if you recieve "port already in use" error, change "app.run(port=5002)" in app.py to another number 

##  What this project is
Experimenting with Google's teachable machine, made a Flask site inspired by Jennifer's Body. Here's a screenshot <img width="911" height="854" alt="Screenshot 2026-05-08 at 2 35 17 PM" src="https://github.com/user-attachments/assets/74493f59-7380-45b2-9c05-6e4eed16b0fa" /> of the website, as well as <a href="https://vimeo.com/1190579612?fl=ip&fe=ec">a video demo</a> as well.


## Why I made this project
Jennifer's Body is so good. I forgot how GOOD Megan Fox looked in it. It's <a href="[https://open.spotify.com/album/1aqg30bNvLSWgShZgX4oop](https://www.netflix.com/title/70111322)">now on Netflix</a>, go watch it! :)

---

## How I made this project

Python, Teachable Mahcine, Flask, Figma

## Challenges I faced

Some of the biggest challenges were:

- trying to style the CSS (ended up vibe coding to get it in before deadline, sorry :(. Will reship and make it better.)
- struggling to deploy it onto Vercel up until I realized no free provider will deploy TensorFlow because it's too big
