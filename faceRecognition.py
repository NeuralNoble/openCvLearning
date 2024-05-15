import cv2
import face_recognition as fr
font = cv2.FONT_HERSHEY_SIMPLEX

donald = fr.load_image_file("demoImages-master/known/Donald Trump.jpg")
faceLoc = fr.face_locations(donald)[0]
donaldFaceEncode = fr.face_encodings(donald)[0]

nancy = fr.load_image_file("demoImages-master/known/Nancy Pelosi.jpg")
faceLoc = fr.face_locations(nancy)[0]
nancyFaceEncode = fr.face_encodings(nancy)[0]

knownEncodes = [donaldFaceEncode, nancyFaceEncode]
names = ["Donald Trump", "Nancy Pelosi"]

unknownface = fr.load_image_file("demoImages-master/unknown/u2.jpg")
unknownfaceBGR = cv2.cvtColor(unknownface, cv2.COLOR_BGR2RGB)

faceLocations = fr.face_locations(unknownface)
unkownEncodes = fr.face_encodings(unknownface,faceLocations)

for faceLocation, unkownEncode in zip(faceLocations, unkownEncodes):
    top,right,bottom,left = faceLocation
    cv2.rectangle(unknownfaceBGR,(left,top),(right,bottom),(255,0,0),3)
    name = "unknown face"
    matches = fr.compare_faces(knownEncodes,unkownEncode)
    print(matches)

    if True in matches:
        matchIndex = matches.index(True)
        name = names[matchIndex]
    cv2.putText(unknownfaceBGR,name,(left,top),font,.75,(0,0,255),2)


# donald2 = cv2.cvtColor(donald, cv2.COLOR_BGR2RGB)
# print(faceLoc)
# top,right,bottom,left = faceLoc
# cv2.rectangle(donald2,(left,top),(right,bottom),(255,0,0),2)



cv2.imshow('face',unknownfaceBGR)
cv2.waitKey(0)