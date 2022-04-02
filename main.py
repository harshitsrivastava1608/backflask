from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from wtforms.validators import InputRequired
import shutil
import moviepy.editor as mp
import subprocess
import speech_recognition as sr 
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence
import time
app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

@app.route('/', methods=['GET',"POST"])
@app.route('/home', methods=['GET',"POST"])
async def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data # First grab the file
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename))) # Then save the file
        await modelCall(file)

        return "File has been uploaded."
    return render_template('index.html', form=form)
async def modelCall(file):
    # Python program to demonstrate
# opening a file


# Open function to open the file "myfile.txt"
# (same directory) in read mode and store
# it's reference in the variable file1

    

    ftxt="static/files/"+file.filename
    with open(f'{"static/files/"+file.filename}','rb') as buffer:
        shutil.copyfileobj(file.file,buffer)
        
    #time.sleep(10)
    clip = mp.VideoFileClip(ftxt)
    clip.audio.write_audiofile("static/files/"+"AIaudio.mp3")
    '''with open(r"static/files/AIaudio.mp3",'rb') as buffer:
        shutil.copyfileobj(r'static/files/AIaudio.mp3',buffer)'''
    sound = AudioSegment.from_mp3('static/files/AIaudio.mp3')
    sound.export("static/files/result.wav", format="wav")
    #full_text=await get_large_audio_transcription("result.wav")
    return ftxt
if __name__ == '__main__':
    app.run(debug=True)