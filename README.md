

google-image-scraper
==================
<br/>

Purpose
-------------------------
Using three script files you can download original image files in bulk from a Google Image search. I am personally using it to create an image data set of textures.

**Python 2.7 is needed to run the Python scripts.**

Execution Instructions
-------------------------

 1. Search Google Images (I recommend using Google search tool filters for better results)
 2. Open Chrome Developer Tools and paste the JavaScript code from "googleImageLinksToFile.js". After running the script, a file will be saved in your downloads folder. Rename this file to "step1_Imagelinks.txt" and move to the directory of the repository on your file system (Of course you can modify the code yourself if you prefer).
 3. Run "saveHtmlLinks2.py" using `$ python saveHtmlLinks2.py`
 4. Run "downloadImages3.py" using `$ python downloadImages3.py`. Images will be saved in a folder called "images" in the directory of the repository.


License
-------------------------

google-image-scraper is available under the MIT license, see the LICENSE file for more details.

> Written with [StackEdit](https://stackedit.io/).
