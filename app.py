from flask import Flask, render_template, request, send_file
   from PIL import Image, ImageFilter
   import os

   app = Flask(__name__)
   UPLOAD_FOLDER = 'static/'
   app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

   @app.route('/')
   def index():
       return render_template('index.html')

   @app.route('/upload', methods=['POST'])
   def upload_file():
       if 'file' not in request.files:
           return 'No file part'
       
       file = request.files['file']
       if file.filename == '':
           return 'No selected file'
       
       # Save the uploaded file
       filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
       file.save(filepath)

       # Open the image file
       with Image.open(filepath) as img:
           # Apply a filter
           img = img.filter(ImageFilter.CONTOUR)
           
           # Save edited image
           edited_path = os.path.join(app.config['UPLOAD_FOLDER'], 'edited_photo.jpg')
           img.save(edited_path)

       return send_file(edited_path, mimetype='image/jpeg')

   if __name__ == '__main__':
       app.run(debug=True, host='0.0.0.0')
