import cv2 
import face_recognition

# face encodings and name 
defined_face_encodings = []
defined_name = []

first_person = face_recognition.load_image_file("C:\\Users\\my pc\\Desktop\\python_series\\codsoft_AI\\Niharika.jpeg")
second_person = face_recognition.load_image_file("C:\\Users\\my pc\\Desktop\\python_series\\codsoft_AI\\siddharth.jfif")
third_person = face_recognition.load_image_file("C:\\Users\\my pc\\Desktop\\python_series\\codsoft_AI\\Anil.JPG")
fourth_person = face_recognition.load_image_file("C:\\Users\\my pc\\Desktop\\python_series\\codsoft_AI\\Shobha.JPG")
fifth_person = face_recognition.load_image_file("C:\\Users\\my pc\\Desktop\\python_series\\codsoft_AI\\Navitesh.JPG")

first_person_encoding = face_recognition.face_encodings(first_person)[0]
second_person_encoding = face_recognition.face_encodings(second_person)[0]
third_person_encoding = face_recognition.face_encodings(third_person)[0]
fourth_person_encoding = face_recognition.face_encodings(fourth_person)[0]
fifth_person_encoding = face_recognition.face_encodings(fifth_person)[0]

defined_face_encodings.append(first_person_encoding)
defined_face_encodings.append(second_person_encoding)
defined_face_encodings.append(third_person_encoding)
defined_face_encodings.append(fourth_person_encoding)
defined_face_encodings.append(fifth_person_encoding)

defined_name.append("Niharika")
defined_name.append("Siddharth")
defined_name.append("Anil")
defined_name.append("Shobha")
defined_name.append("Navitesh")

cap = cv2.VideoCapture(0)
while True:
    ret , frame = cap.read()
    face_location = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame , face_location)

    for (top , right , bottom , left) , face_encodings in zip(face_location , face_encodings):
        match = face_recognition.compare_faces(defined_face_encodings , face_encodings)
        name = "unknown"

        if True in match:
            match_index = match.index(True)
            name = defined_name[match_index]

        face_center_x = (left + right) // 2
        face_center_y = (top + bottom) // 2
        radius = (right - left) // 2
        cv2.circle(frame, (face_center_x, face_center_y), radius, (0, 0, 255), 2)
        cv2.putText(frame ,name, (left , top-10), cv2.FONT_HERSHEY_COMPLEX, 0.9, (0, 0, 255), 2 )
    
    cv2.imshow("video" , frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()