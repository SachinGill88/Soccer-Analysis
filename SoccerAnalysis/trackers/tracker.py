from ultralytics import YOLO
import supervision as sv 

class Tracker: 
    def __init__(self, model_path):
        self.model= YOLO (model_path)
        self.tracker = sv.ByteTracks()


    def detect_frames(self, frames):
        batch_size = 20
        detections =[]
        for i in range  (0,len(frames), batch_size):
            detections_batch = self.model.predict (frames[i:i+batch_size], conf=0.1) #minimum confidence is 0.1 thus don't need overwhelming probability meter 
            detections += detections_batch
        return detections
    

    def get_object_tracks (self, frames):
        detections = self.detect_frames (frames)

        for frame_num, detection in enumerate (detections): #enumerate to add index 
            cls_names = detection.names 
            cls_names_inv = {v:k for k,v in cls_names.items()} ## all this does is switch key and value to be value and key

            # convert to supervision libraries detection format 
            detection_supervision = sv.Detections.from_ultralytics(detection)

            print (detection_supervision)
