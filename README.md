#  YOLOv11 -  Web for  Fire Detection Model

## Mô tả
![image](https://github.com/user-attachments/assets/963b60a4-1f46-4bbc-9c15-9a051fdac4e9)


Dự án này được thực hiện để demo về việc sử dụng YOLOv11 (You Only Look Once version 11) trong việc nhận diện và phân loại đối tượng trong hình ảnh. Cụ thể, mục tiêu của dự án là huấn luyện một mô hình YOLOv11 để nhận diện liệu một bức hình có chứa "Lửa" (Fire) hay không, và trả về độ tin cậy (confidence) dựa trên kết quả nhận diện.
## Hình ảnh sơ lược về web dùng Framework Streamlit
Web cho người dùng chọn ảnh xong sau đó detect Fire và cho biết các thông số nhận diện Confidence,Detection,Class,Coordinates
![image](https://github.com/user-attachments/assets/27d7e5d1-e6e0-429f-9c4b-d83c6064ddfe)

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
# Kết quả huấn luyện và đánh giá mô hình YOLO

## Epoch 87/100:
- **Epoch**: Số vòng huấn luyện hiện tại, ở đây là vòng thứ 87 trong tổng số 100 vòng.
- **GPU_mem**: Mức sử dụng bộ nhớ GPU trong quá trình huấn luyện, ở đây là 2.84 GB.

## Các giá trị mất mát (losses):
- **box_loss**: 1.168 - Mất mát liên quan đến việc dự đoán bounding boxes.
- **cls_loss**: 1.14 - Mất mát liên quan đến phân loại đối tượng.
- **dfl_loss**: 1.327 - Mất mát phân bố độ chính xác (distribution loss) trong YOLOv5.

## Batch và ảnh:
- **Instances**: 24 - Số lượng đối tượng trong mỗi batch.
- **Size**: 640 - Kích thước ảnh được huấn luyện (640x640).

---

## Đánh giá trên tập kiểm tra (validation):

### Đánh giá lớp "fire":
- **Images**: 460 - Số ảnh trong tập kiểm tra.
- **Instances**: 410 - Tổng số đối tượng trong tập kiểm tra.

### Các chỉ số đánh giá:
- **Precision (P)**: 0.815 (81.5%) - Độ chính xác của mô hình trong việc dự đoán bounding boxes.
- **Recall (R)**: 0.857 (85.7%) - Độ hồi lại của mô hình trong việc nhận diện đối tượng có mặt trong ảnh.
- **mAP50**: 0.91 (91%) - Mean Average Precision tại ngưỡng IoU 50%. Độ chính xác cao khi IoU ≥ 50%.
- **mAP50-95**: 0.655 (65.5%) - Mean Average Precision tại các ngưỡng IoU từ 50% đến 95%. Mô hình có độ chính xác trung bình khá ổn ở các ngưỡng IoU này.

---

## Tóm tắt:
- **Precision (P)**: 81.5% - Mô hình chính xác 81.5% khi dự đoán đối tượng.
- **Recall (R)**: 85.7% - Mô hình tìm được 85.7% các đối tượng có mặt trong ảnh.
- **mAP50**: 91% - Mô hình có độ chính xác trung bình rất cao (91%) khi IoU ≥ 50%.
- **mAP50-95**: 65.5% - Độ chính xác trung bình khi tính toán IoU từ 50% đến 95% (một chỉ số đánh giá chi tiết hơn về độ chính xác).

---

## Ý nghĩa các chỉ số:
- **Precision (P)** và **Recall (R)**: Chỉ ra mức độ chính xác và độ hồi lại của mô hình, càng cao càng tốt.
- **mAP50**: Là một chỉ số đánh giá độ chính xác của mô hình khi mức độ chồng lấn (IoU) giữa bounding box dự đoán và ground truth là 50% hoặc cao hơn.
- **mAP50-95**: Đánh giá độ chính xác của mô hình tại các ngưỡng chồng lấn từ 50% đến 95%. Mô hình  có một độ chính xác trung bình khá cao ở các ngưỡng này.
  ![image](https://github.com/user-attachments/assets/976bb30e-1419-4334-b65e-4bd772770cd0)

- **Một vài hình ảnh sau khi training**:
   ![image](https://github.com/user-attachments/assets/903d0f74-cbc2-4898-96ec-67944ae51580)
   ![image](https://github.com/user-attachments/assets/5bf092dd-2bc2-4a12-8149-ca1ebc3f7b5d)
   ![image](https://github.com/user-attachments/assets/4d1225fb-4461-48ec-bee7-02566688ac40)

## Giải thích log kết quả YOLOv11

### Dòng 1:
- **640x640**: Kích thước của ảnh đầu vào (640x640 pixel).
- **2 fires**: Mô hình phát hiện 2 đối tượng "Lửa".
- **54.9ms**: Thời gian nhận diện của mô hình (inference time).
- **Speed**:
  - **23.1ms preprocess**: Thời gian chuẩn bị ảnh (thay đổi kích thước, chuẩn hóa, ...).
  - **54.9ms inference**: Thời gian mô hình thực hiện nhận diện đối tượng trong ảnh.
  - **28.7ms postprocess**: Thời gian xử lý kết quả sau nhận diện (lọc kết quả, vẽ hộp giới hạn,...).
- **(1, 3, 640, 640)**: Kích thước của ảnh đầu vào mà mô hình nhận được (batch size: 1, channels: 3, kích thước ảnh: 640x640).
### Dòng log 2:

- **(no detections)**: Không phát hiện đối tượng nào trong ảnh.
- **79.6ms**: Thời gian nhận diện của mô hình (inference time).
- **Speed**:
  - **64.3ms preprocess**: Thời gian chuẩn bị ảnh.
  - **79.6ms inference**: Thời gian mô hình thực hiện nhận diện.
  - **2.4ms postprocess**: Thời gian xử lý sau nhận diện.

### Dòng log 3:
- **1 fire**: Mô hình phát hiện 1 đối tượng "Lửa".
- **113.3ms**: Thời gian nhận diện.
- **Speed**:
  - **22.8ms preprocess**: Thời gian chuẩn bị ảnh.
  - **113.3ms inference**: Thời gian mô hình thực hiện nhận diện.
  - **17.3ms postprocess**: Thời gian xử lý sau nhận diện.
## Cách chạy dự án

1. Cài đặt các thư viện yêu cầu:
   ```bash
   pip install -r requirements.txt

