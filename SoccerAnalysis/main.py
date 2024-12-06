from utils import read_video, save_video

def main():
    print("Soccer Computer Vision Application")
    # read video
    video_frames = read_video('C:/Users/sachi/Desktop/SoccerAnalysis/input_videos/bundesliga.mp4')

    #save video
    save_video = (video_frames, 'C:/Users/sachi/Desktop/SoccerAnalysis/output_videos/output_video.avi')

if __name__ == "main":
    main()