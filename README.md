# Unknown Language Detector

Happy New Year 2023! As this is my first repository of the year and New Year's is a global celebration, I have decided to make this so that you can understand a lot of people around the world when they are texting you!

## Description

Don't know a language that someone is talking to you in? Then this set of programs is for you!

## Requirements

- `langcodes` module (for all programs in this repository):
  
  ```
  pip install langcodes
  ```

- `langdetect` module (for the `langdetect_detector.py` program in this repository):
  
  ```
  pip install langdetect
  ```
  
- `textblob` module (for the `textblob_detector.py` program in this repository):
  
  ```
  pip install textblob
  ```
  
- `langid` module (for the `langid_detector.py` program in this repository):
  
  ```
  pip install langid
  ```

## Which One Do I Use?

- The `langdetect` module in `langdetect_detector.py` is a port of Google’s language-detection library that supports 55 languages. It is best used for more common languages that are spoken.
- The `textblob` program is used for natural language processing(NLP) tasks such as noun phrase extraction, sentiment analysis, classification, translation, and more. It is best used for more complex and intricate sentences.
- The `langid` program is a standalone Language Identification tool. It is pre-trained over a large number of languages (as of January 14th 2020, 97). It is best used for languages which are not very commonly spoken.
