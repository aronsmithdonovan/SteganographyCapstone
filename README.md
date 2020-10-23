# A Picture's Worth a Thousand Bytes
#### Colin Kirby, Maddie AlQatami, Aron Smith-Donovan, Randy Beidelschies
<br>

***
<br>

### Documentation:
This repository contains an application for steganographic encoding of text within an image. Text input, which is either typed into a text box or uploaded as the contents of a .txt file, is encrypted with a symmetric (private-key) method, returning an encrypted token and a key, before being encoded into image data. The key must be provided to retrieve the original message from the image after it has been encoded. The application itself supports both encoding and decoding of images and two different methods of selecting the pixels that are encoded: the Least Significant Bit (LSB) method and the Scatter or Chaos method. The application also allows the user to upload locally stored image and .txt files and to download image and .txt files created by the software (i.e. encoded images, .txt files containing generated encryption keys, and .txt files containing decoded messages). All of the files contained in the `src` folder are equipped to run through the command line, but the user does not have the option to select their own image to be encoded through this channel, which is intended primarily to demonstrate the behavior of each file and not to provide full functionality.

This application was completed as the course project for COMP494: Computer Security/Privacy for the fall 2020 semester by Macalester College undergraduate students Colin Kirby, Maddie AlQatami, Aron Smith-Donovan, and Randy Beidelschies under the guidance of Prof. Abigail Marsh. All work on this project was completed independently by the students. The application in conjunction with the report and video demo provided meets the requirements for a capstone project for undergraduates pursuing a Bachelor's in Computer Science.

Special thanks to Prof. Abby, the Python documentation, and the Stack Overflow forums.
<br>

***
<br>

### File structure:

```
  SteganographyCapstone\
      .gitignore
      README.md
      Steganography.exe
      run.py
      src\
         process.py
         encodeLSB.py
         decodeLSB.py
         encodeChaos.py
         decodeChaos.py
         GUI.py
      img\
         cat.png
         icon.ico
```
<br>

***
<br>

<blockquote>

### Running the program:

   <blockquote>

   **Option 1: running the application with the executable file**<br>
   The `Steganography.exe` file is compiled with the full capabilities of the application, and can simply be run as a standalone file.

   </blockquote>
   <br>
   <blockquote>

   **Option 2: running the application with the Python files**<br>
   Download the repository to a local directory and follow the setup instructions below for installing the necessary packages. The `run.py` file can be run from a text editor or command line to launch the application.

   </blockquote>
   <br>
   <blockquote>

   **Option 3: running individual Python files**<br>
   Download the repository to a local directory and follow the setup instructions below for installing the necessary packages. The files contained in the `src` file can all be run from a text editor or command line to demonstrate the behavior of individual methods; this option does not allow for user-provided images to be encoded.

   </blockquote>
   <br>
</blockquote>
<br>

***
<br>

<blockquote>

### Setup instructions to run Python files:

  * check that Python is up-to-date
    * using version 3.8.6, released 09/24/2020
    * check version: `$ python --version`
    * download or update: <a href="https://www.python.org/downloads/release/python-390/">release page here to download the appropriate installer</a> 
 * check that pip is up-to-date
    * using version 20.2.3, released 09/08/2020
    * check version: `$ pip --version`
    * update: `$ pip install --upgrade pip`
 * download or update the `scipy` package (the `numpy` package is automatically installed with `scipy`)
    * using version 1.5.2 <a href="https://www.scipy.org/index.html">(docs)</a>
    * download: `$ pip install --user scipy`
    * update: `$ pip install --upgrade scipy`
 * download or update the `Pillow` package
    * using version 7.2.0 <a href="https://pillow.readthedocs.io/en/stable/index.html">(docs)</a>
    * download: `$ pip install Pillow`
    * update: `$ pip install --upgrade Pillow`
 * download or update the `cryptography` package
   * using version 3.1.1, released 09/22/2020
   * download: `$ pip install cryptography`
   * update: `$ pip install --upgrade cryptography`
 * download or update the `pyperclip` package
   * using version 1.8.1, released 10/10/2020
   * download: `$ pip install pyperclip`
   * update: `$ pip install --upgrade pyperclip`
 * download or update the `cv2` package
   * using version 4.4.0.44, released 09/22/2020
   * download: `$ pip install opencv-python`
   * update: `$ pip install --upgrade opencv-python`
</blockquote>
<!-- end of file -->