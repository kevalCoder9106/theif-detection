import detect
import cv2
import send_mail

chunk_recorded = False

cap = cv2.VideoCapture(1)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'MPEG')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (width,height))
writer = cv2.VideoWriter('recording/rec1.avi', cv2.VideoWriter_fourcc(*'XVID'), 20, (width,height))

def give_alert():
    send_mail.send_mail("kevalcoder@gmail.com",
                        "Testing human detection project 2\nMessage: a human is detected sending a clip in few seconds")

def get_frame():
    """
    this function will return perticular frame from input device
    """
    
    ret,frame= cap.read()
    cv2.imwrite("frame_bin/frame.png",frame)

    return "frame_bin/frame.png"

def record_chunk():
    """
    this function will save few seconds video clip to recording folder
    """

    i = 0

    while True:
        ret,frame= cap.read()
        writer.write(frame)

        #cv2.imshow('frame', frame)

        if i > 100:
            break

        i = i + 1

    chunk_recorded = True

    cap.release()
    writer.release()
    #cv2.destroyAllWindows()

if __name__ == "__main__":
    # initiate send email object
    send_mail = send_mail.send_mail("actemp22@gmail.com","atempaccount99",)
    
    while True:
        # get if any human are detected
        total_human_detected = detect.get_human_presence(get_frame())

        if len(total_human_detected) > 0: # if any detected
            print(f"[+] Human is detected")
            print(f"[+] Sending mail")
            # give alert
            give_alert()
            
            if not chunk_recorded:
                # save video clip
                print(f"[+] Recording video clip")
                record_chunk()
                # sending mail
                print(f"[+] Sending video clip")
                send_mail.send_mail_with_attachment(
                                    "kevalcoder@gmail.com",
                                    "Testing human detection project 2",
                                    "sending a clip",
                                    "recording/rec1.avi")
                break

        else: # if not
            print(f"[=] No humans detected")