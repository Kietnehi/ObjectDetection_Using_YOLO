# from ultralytics import YOLO

# # Dự đoán trên video    
# model2 = YOLO("trained_model.pt")
# results = model2.track('car-detection.mp4',save=True,show=True)  # predict on a video
import cv2
from ultralytics import YOLO

# Tải mô hình YOLO đã huấn luyện sẵn
model3 = YOLO(r'C:\Users\ADMIN\Desktop\DEEP LEARNING MATERIAL\ObjectDetection\runs\detect\train7\weights\last.pt')

# Đọc ảnh vào
image_path = r'C:\Users\ADMIN\Desktop\DEEP LEARNING MATERIAL\ObjectDetection\images.jpg'
image = cv2.imread(image_path)

# Resize ảnh về kích thước mong muốn (ví dụ: 640x640)
resized_image = cv2.resize(image, (640, 640))

# Dự đoán trên ảnh đã thay đổi kích thước
results = model3.predict(resized_image, show=True)  # predict on resized image

# Chờ cho đến khi bạn nhấn một phím và sau đó đóng cửa sổ
cv2.waitKey(0)
cv2.destroyAllWindows()  # Đóng tất cả cửa sổ OpenCV