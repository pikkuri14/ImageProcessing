
import cv2

original = cv2.imread("img/nana.png")

# converted_image = cv2.cvtColor(original, cv2.COLOR_BGR2HSV)
# rotate_image = cv2.rotate(original, rotateCode=cv2.ROTATE_90_COUNTERCLOCKWISE)
# blurred_image = cv2.GaussianBlur(original, (5,5), 0)
# garis_image = cv2.line(original, (0,0), (200,200), (255, 0 ,0), 1)
# circle_image = cv2.circle(original, (200,200), 100, (0,255,0), 10)
# rectangular_image = cv2.rectangle(original, (0,0), (200,200), (0,0,255), 10)
# texted_image = cv2.putText(original, "NANA WARNANA", (200,200), cv2.FONT_HERSHEY_SIMPLEX,1, (255,0,255), 5,)
# w = original.shape[0]
# h = original.shape[1]


# print(h)
# print(w)

# resized_image = cv2.resize(original, (0,0), fx =2, fy =2)

cv2.imshow("gambarnana", original)
# cv2.imshow("gambarnana", texted_image)

# vid = cv2.VideoCapture("video.mp4")
cv2.waitKey(0)


# while(True):
#     ret, frame = vid.read()

#     cv2.imshow("video", frame)

#     if cv2.waitKey(0) & 0xFF == ord('q'):
#         break



# cv2.destroyAllWindows()




