import streamlit as st
from PIL import Image
from ultralytics import YOLO
import cv2  # Import OpenCV to handle color conversion
import pandas as pd
# Tải mô hình YOLOv11 đã huấn luyện của bạn
model_path = r'C:\Users\ADMIN\Desktop\DEEP LEARNING MATERIAL\ObjectDetection\runs\detect\train7\weights\last.pt'
model = YOLO(model_path)  # Tải mô hình đã huấn luyện từ tệp .pt

# Tiêu đề trang web
st.title("Ứng Dụng Nhận Diện Hỏa Hoạn Từ Ảnh Tải Lên 🔥")

# Hướng dẫn cho người dùng
st.markdown("""
Chào mừng bạn đến với ứng dụng nhận diện hỏa hoạn! 
Vui lòng tải lên một bức ảnh từ máy tính của bạn, và mô hình sẽ giúp bạn nhận diện xem trong ảnh có hỏa hoạn hay không.
""")

# Phần tải ảnh lên
uploaded_file = st.file_uploader("Tải lên ảnh để nhận diện", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Mở ảnh và hiển thị trên web
    image = Image.open(uploaded_file).convert('RGB')  # Chuyển đổi ảnh sang RGB để đảm bảo màu sắc chính xác
    # st.image(image, caption="Ảnh tải lên", use_container_width=True)

    # Tiến hành nhận diện đối tượng trên ảnh
    results = model(image)  # Sử dụng mô hình để nhận diện trên ảnh

    # Plot results image
    im_bgr = results[0].plot()  # BGR-order numpy array
    im_rgb = Image.fromarray(im_bgr[..., ::-1])  # Chuyển đổi từ BGR sang RGB và từ NumPy array sang PIL image

    # Hiển thị ảnh đã vẽ bounding box lên
    # st.image(im_rgb, caption="Kết quả nhận diện với bounding box", use_container_width=True)

    # Lấy các thông tin dự đoán
    boxes = results[0].boxes  # Lấy bounding boxes
    names = [results[0].names[int(cls)] for cls in boxes.cls.int()]  # Class name for each box
    confidences = boxes.conf.cpu().numpy()  # Confidence score of each box
    coordinates = boxes.xywh.cpu().numpy()  # Tọa độ của bounding box

    # Tạo một DataFrame để hiển thị thông tin dưới dạng bảng
    detection_data = {
        "Detection": [i + 1 for i in range(len(names))],
        "Class": names,
        "Confidence (%)": [confidence * 100 for confidence in confidences],
        "Coordinates (x_center, y_center, width, height)": [str(coord) for coord in coordinates]
    }
    
    detection_df = pd.DataFrame(detection_data)  # Tạo bảng từ dữ liệu
    # Hiển thị bảng với thông tin về các đối tượng đã nhận diện
    st.subheader("Thông Tin Nhận Diện")
    st.dataframe(detection_df.style.format({
        "Confidence (%)": "{:.2f}",
    }).set_properties(**{'text-align': 'center'}), width=1500)  # Điều chỉnh chiều rộng bảng và căn giữa văn bản

    # Hiển thị ảnh gốc và ảnh đã nhận diện ở 2 cột riêng biệt
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("Ảnh Gốc")
        st.image(image, caption="Ảnh gốc", use_container_width=True)

    with col2:
        st.subheader("Ảnh Đã Nhận Diện")
        st.image(im_rgb, caption="Kết quả nhận diện với bounding box", use_container_width=True)

    # Nếu phát hiện "fire", hiển thị thêm thông báo
    if 'fire' in names:
        st.success("Phát hiện hỏa hoạn trong ảnh!")
    else:
        st.warning("Không phát hiện hỏa hoạn trong ảnh.")