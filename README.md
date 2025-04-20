# Demo YOLOv11 - Fire Detection Model

## Mô tả

Dự án này được thực hiện để demo về việc sử dụng YOLOv11 (You Only Look Once version 11) trong việc nhận diện và phân loại đối tượng trong hình ảnh. Cụ thể, mục tiêu của dự án là huấn luyện một mô hình YOLOv11 để nhận diện liệu một bức hình có chứa "Lửa" (Fire) hay không, và trả về độ tin cậy (confidence) dựa trên kết quả nhận diện.

## Cấu hình dự án

- **Mô hình sử dụng**: YOLOv11
- **Dữ liệu huấn luyện**: Bộ dữ liệu hình ảnh có chứa các đối tượng "Fire" (Lửa) và không có "Fire"
- **Số epoch**: 100 epoch
- **Kết quả đầu ra**: Dự đoán là "Fire" hoặc "Không phải Fire" cùng với độ tin cậy (confidence) dưới dạng phần trăm.

## Các bước thực hiện

1. **Chuẩn bị dữ liệu**:
    - Dữ liệu huấn luyện bao gồm các bức ảnh có chứa và không chứa "Lửa". Mỗi hình ảnh được gán nhãn để mô hình có thể học cách phân biệt.

2. **Huấn luyện mô hình**:
    - Dự án sử dụng YOLOv11 để huấn luyện trên bộ dữ liệu đã chuẩn bị với 100 epoch. Quá trình huấn luyện này sẽ giúp mô hình cải thiện khả năng nhận diện "Fire" trong hình ảnh.

3. **Kiểm tra và đánh giá**:
    - Sau khi huấn luyện, mô hình sẽ được kiểm tra trên các bức ảnh test để xác định xem có phải là "Fire" hay không và mô hình sẽ đưa ra độ tin cậy (confidence) cho dự đoán đó.

## Cách chạy dự án

1. Cài đặt các thư viện yêu cầu:
   ```bash
   pip install -r requirements.txt
