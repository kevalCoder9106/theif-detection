import detect
import cv2

def give_alert():
    print("Alert human's detected")

def get_frame():
    cap = cv2.VideoCapture(1)
    ret,frame= cap.read()
    cv2.imwrite("frame_bin/frame.png",frame)

    return "frame_bin/frame.png"

def record_chunk():
    cap = cv2.VideoCapture(0)
    width= int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height= int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    writer= cv2.VideoWriter('basicvideo.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 20, (width,height))
    while True:
        ret,frame= cap.read()
        writer.write(frame)
        cv2.imshow('frame', frame)

        print(frame)

        if frame > 1200:
            break

    cap.release()
    writer.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    total_human_detected = detect.get_human_presense(get_frame())

    if len(total_human_detected) > 0:
        give_alert()
    else:
        print("No humans in the scene right now")
