# import cv2
# import cvlib as cv
# from cvlib.object_detection import draw_bbox
# from gtts import gTTS
# from playsound import playsound

# def speech(text):
#     print(text)
#     language = "en"
#     output = gTTS(text=text, lang=language, slow=False)

#     output.save('./sounds/output.mp3')
#     playsound('./sounds.output.mp3')


# video = cv2.VideoCapture(1)
# labels= []

# while True:
#     ret, frame = video.read()
#     bbox, label, conf = cv.detect_common_objects(frame)
#     output_image = draw_bbox(frame, bbox,label, conf)

#     cv2.imshow("Object Detection", output_image)

#     for item in label:
#         if item in labels:
#             pass
#         else:
#             labels.append(item)

#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break

# i = 0
# new_sentence = []
# for label in labels:
#     if i == 0:
#         new_sentence.append(f"I found a {label}, and, ")
#     else:
#         new_sentence.append(f"a{label}")

#     i+=1

# print(" ".join(new_sentence))
import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
from gtts import gTTS
from playsound import playsound

def speech(text):
    print(text)
    language = "en"
    output = gTTS(text=text, lang=language, slow=False)
    output.save('./sounds/output.mp3')
    playsound('./sounds/output.mp3')

def main():
    video = cv2.VideoCapture(0)
    if not video.isOpened():
        print("Error: Camera not found or not accessible.")
        return

    labels = []
    while True:
        ret, frame = video.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break

        bbox, label, conf = cv.detect_common_objects(frame)
        output_image = draw_bbox(frame, bbox, label, conf)

        cv2.imshow("Object Detection", output_image)

        for item in label:
            if item not in labels:
                labels.append(item)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    video.release()
    cv2.destroyAllWindows()

    # Generate and play speech for detected objects
    if labels:
        new_sentence = [f"I found a {label}, and, " if i == 0 else f"a {label}" for i, label in enumerate(labels)]
        speech(" ".join(new_sentence))
    else:
        print("No objects detected.")

if __name__ == "__main__":
    main()


