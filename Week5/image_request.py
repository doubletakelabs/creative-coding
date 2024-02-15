import py5
import requests

# create a query to send to the MET API to retrieve a list of objects with this query
query = "dolphin"
url = f"https://collectionapi.metmuseum.org/public/collection/v1/search?q={query}&hasImages=true"
response = requests.request("GET", url)
result = response.json()
# print(result) # uncomment this line to see what the response looks like at this point

# after we receive the result, let's grab the first objectID in the response
objectID = result["objectIDs"][0] # this is the first objectID and we'll store it in a variable

# let's do another request to the API to now get information about that particular objectID
url = f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{objectID}"
response = requests.request("GET", url)
result = response.json()
# print(result) # uncomment this line to see what the response looks like at this point


hasImage = False # create a boolean variable to keep track of whether or not this object has an image in its json response

# if there is a key within the result called "primaryImage"
if result["primaryImage"] != "":
    global img # make a new global variable called img
    img = py5.load_image(result["primaryImage"]) # load the image from the URL listed at the "primaryImage" key for the object
    hasImage = True # set the hasImage variable to True

# if it does not have an image, then hasImage is still False

def setup():    
    py5.size(500, 500) # set the canvas size

def draw():
    if(hasImage): # if the returned object has an image
      py5.image(img, 10, 10, 400, 400) # show the image at 10,10 and make it 400x400 in size

py5.run_sketch() # run the sketch