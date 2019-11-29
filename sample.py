from clarifai.rest import ClarifaiApp
# Build model which pridicts image attributes
app = ClarifaiApp(api_key='9229dbaf8f044284b4837d397b50d372')
model = app.public_models.general_model
response = model.predict_by_filename("C:/Users/402096/Desktop/train_people_sitting.jpg")

# Display pridicted attributes on UI
concepts = response['outputs'][0]['data']['concepts']
indx = 1.0
for concept in concepts:
    print(concept['name'], concept['value'])