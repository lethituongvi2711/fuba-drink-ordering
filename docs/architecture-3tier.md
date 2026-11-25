# Kiến trúc hệ thống 3-Tier & Luồng dữ liệu - Quán nước Fuba (Sprint 0)

## 1. Tổng quan kiến trúc 3 tầng (3-Tier Architecture)
- **Presentation Tier (Frontend Web):** Giao diện đặt nước trực tuyến cho Khách hàng (xem menu, chọn size/đường/đá/topping, giỏ hàng) và màn hình quản lý cho Nhân viên/Quản lý quán Fuba.
- **Business Logic Tier (Backend API):** Xử lý nghiệp vụ đặt đơn, tính tổng tiền tự động, phân quyền người dùng và cập nhật trạng thái đơn hàng.
- **Data Tier (Database):** Lưu trữ tập trung dữ liệu người dùng, thực đơn, topping, đơn hàng và lịch sử giao dịch.

## 2. Sơ đồ kiến trúc 3-Tier & Luồng dữ liệu (Data Flow)
mermaid
flowchart LR
A[Presentation Tier


Web Khách hàng & Quầy Fuba] -->|HTTP Request / JSON| B[Business Logic Tier


API Xử lý đơn & Tính giá]
B -->|SQL / ORM Query| C[(Data Tier


Database Menu & Đơn hàng)]
C -->|Dữ liệu trả về| B
B -->|JSON Response| A


## 3. Luồng dữ liệu đặt nước cơ bản
1. **Khách hàng** chọn món trên giao diện và gửi yêu cầu đặt đơn -> **Presentation Tier** gửi request sang **Business Logic Tier**.
2. **Business Logic Tier** kiểm tra món, tính tiền ly nước + topping và ghi nhận đơn mới xuống **Data Tier**.
3. **Data Tier** lưu đơn hàng thành công và trả kết quả ngược lại để hiển thị mã đơn cho khách và báo đơn mới tại quầy pha chế.
