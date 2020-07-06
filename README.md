# Unsplash Search

## Description
The application implements a photo search engine using the Unsplash API.


<img src="https://media.giphy.com/media/egAFhEApCXJtIgN0rv/giphy.gif" width="600" height="450" />

## Dependencies

* Python
* Django framework
* python-unsplash 1.0.1

## Installation

`git clone https://github.com/lleviy/Unsplash_Search.git`

Transfer the contents of the Unsplash_Search folder to your Django project, confirming the merge of the folders. 

Install dependency: `pip install python-unsplash`. 


## Configuration
1) Add the "unsplash_search" application to the INSTALLED_APPS list in the settings.py file of your project.

```
INSTALLED_APPS = [
...
'unsplash_search',
]
```

2) Register on the Unsplash service as a developer: https://unsplash.com/developers, and then register
your application. Thus, you will get all the necessary settings for the api.

3) Create the unsplash_api.json file in the root directory of your project. This file will be used to access the api settings when
running the application locally.
Below is an example of api settings, replace the settings in it with your own and paste
to your unsplash_api.json file.
```
"client_id": "your_client_id",
"client_secret": "your_client_secret",
"redirect_uri": "some_redirect_uri"
```

In order to use the settings in the application deployed on the server, you need to additionally define them as environment variables.

## Template

The repository contains the example template: search_photos.html, where each photo is designed as a button. By clicking on the button, the field with id "id_photo_url" is assigned the url of the image for later saving the form.

You must configure the template yourself for your project.
