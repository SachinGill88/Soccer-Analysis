from ultralytics import YOLO

model = YOLO ('C:/Users/sachi/Desktop/SoccerAnalysis/models/best.pt')

results = model.predict('C:/Users/sachi/Desktop/SoccerAnalysis/input_videos/08fd33_4.mp4', save=True)

print (results[0]) #this will print results of first frame


for box in results[0].boxes:
    print(box)


#positioning system in use is xyxy, which is the 4 boundaries of the box (i.e.: xyxy: tensor([[1902.6053,  377.5464, 1919.2775,  443.0815]]))

# key improvements come in annotating players vs refs vs fans, improving ball recognition, etc 