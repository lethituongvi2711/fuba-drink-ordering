# fuba-drink-ordering

# 🥤 Fuba Online Drink Ordering System (Hệ thống đặt đồ uống trực tuyến Fuba)

> Đồ án môn học / Dự án nhóm quản lý theo mô hình Agile/Scrum (Sprint 0 - 4 tuần phát triển).

---

## 👥 Thành viên nhóm & Phân công vai trò
* **Lê Thị Tường Vi** *(Nhóm trưởng)*: Quản lý dự án Jira, Git Flow, phát triển khung giao diện Frontend (`FUBA-1`, `FUBA-6`).
* **Diệp Trương**: Quản lý hạ tầng GitHub, kiểm soát kho lưu trữ và phân quyền (`FUBA-2`).
* **Lê Phạm Thanh Huyền**: Thiết kế kiến trúc hệ thống 3-Tier và sơ đồ luồng dữ liệu (`FUBA-3`).
* **Nhi Phan Thị Yến**: Thiết kế mô hình cơ sở dữ liệu ERD và viết script SQL (`FUBA-4`).
* **Đoàn Lý Tường Vy**: Xây dựng khung mã nguồn Backend và cấu hình API (`FUBA-5`).

---

## 🏗️ Cấu trúc thư mục dự án (3-Tier Architecture)
Dự án được tổ chức rõ ràng theo chuẩn phân tầng kỹ thuật:
```text
fuba-drink-ordering/
├── docs/          # Tài liệu thiết kế, sơ đồ kiến trúc, tài liệu phân tích hệ thống
├── database/      # Mô hình ERD, script khởi tạo cơ sở dữ liệu (init.sql)
├── backend/       # Mã nguồn phía máy chủ (Server, API, kết nối CSDL)
└── frontend/      # Giao diện người dùng (HTML/CSS/JS, khung Wireframe)

# 🧋 FUBA DRINK ORDERING SYSTEM
Hệ thống quản lý và đặt nước online cho quán Fuba (Bài tập thực hành quy trình Agile/Scrum - 4 tuần).

## 👥 Thành viên nhóm thực hiện
| STT | Họ và Tên | Mã Jira (Sprint 0) | Vai trò dự kiến |
| :--- | :--- | :---: | :--- |
| 1 | Lê Thị Tường Vi | FUBA-1 | Nhóm trưởng / Scrum Master |
| 2 | **Trương Diệp** | **FUBA-2** | Cấu hình Repo, quy trình Git & README |
| 3 | Thành viên 3 | FUBA-3 | Nghiên cứu kiến trúc hệ thống |
| 4 | Thành viên 4 | FUBA-4 | Thiết kế Database & ERD |
| 5 | Thành viên 5 | FUBA-5 / FUBA-6 | Khởi tạo khung Backend & Frontend |

## 📁 Cấu trúc thư mục dự án
```text
fuba-drink-ordering/
├── docs/        # Tài liệu nghiên cứu kiến trúc hệ thống, sơ đồ luồng
├── frontend/    # Mã nguồn giao diện người dùng (Web App)
├── backend/     # Mã nguồn xử lý nghiệp vụ & RESTful API
├── database/    # Sơ đồ ERD và script khởi tạo cơ sở dữ liệu (.sql)
└── README.md    # Tài liệu tổng quan và hướng dẫn làm việc nhóm
 dev
