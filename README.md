# Language Translation
Get instantaneous translation letter by letter .Every letter matters! Choose over 10+ sugesstions for each word.
# How to use?
* Select the language to which you want to convert
* Type the Word
* Select from the suggestion list and get the word replaced to translated word.
# Improvements
* One of the cases that doesn't work until now is , Adding a new word inbetween the previously typed words of a sentence.
* Another case is appending a letter in between word typed. 
``` However, You can use backspace and add back the letter.```
# How it works?
* For each letter typed, A key listner routine runs which gets the input from the user. A GET call is made with that particular letter and we get the translated word returned from the api. 
* After the api call, the typed word is replaced with the translated word
* Everytime, the user clicks the choice, an Xhr request is made which posts to the server with a json containing the word-translation pair.
* The backend python stores the pair as a dictionary(key-value store).
* When user clicks the download button,a GET request is made and all the dictionary values are inserted into the csv file stored in heroku by default(created by hardcoding it on heroku file structure).

* Word is formed by appending each of the letter and that's how the suggestions are made at letter level.

# Download
 * You can download the word you typed with the respective transliteration now as a CSV format.
 ``` \download ``` will produce a output.csv file with all the typed inputs in the current session. Also, You can download by  cclicking on the download button.
 
 # Deployment 
 * Heroku Procfile handles the deployment in heroku. Gunicorn is a WSGI HTTP server for handling multiple requests at the same time.
