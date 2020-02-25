from google.cloud import vision

### COPYPASTE CREDENTIAL SECTION
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ".googleapi_creds"
### end google creds


BERNIE = ["https://static.politico.com/dims4/default/4e708e3/2147483647/resize/1160x/quality/90/?url=https%3A%2F%2Fstatic.politico.com%2F7a%2Fa5%2Fbdbf91ed4d438afad37ae39f360a%2F200221-sanders-gty-773.jpg",
          "https://nyppagesix.files.wordpress.com/2020/02/bernie-sanders.jpg"]

HILLARY = ["https://static.politico.com/dims4/default/4e708e3/2147483647/resize/1160x/quality/90/?url=https%3A%2F%2Fstatic.politico.com%2F7a%2Fa5%2Fbdbf91ed4d438afad37ae39f360a%2F200221-sanders-gty-773.jpg"]


client = vision.ImageAnnotatorClient()
response = client.annotate_image({
  'image': {'source': {'image_uri': BERNIE[1]}}, 
  'features': [{'type': vision.enums.Feature.Type.FACE_DETECTION}],
})

