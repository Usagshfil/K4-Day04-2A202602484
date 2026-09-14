# Danh Sách Thành Viên Nhóm & Phân Công Vai Trò (Day 04 Lab)

| STT | Họ và Tên | MSSV | GitHub Username | Vai trò Phân công | Trách nhiệm chính |
|:---:|:---|:---:|:---|:---|:---|
| 1 | Phan Đức Duy | 2A202602397 | DuykoNgu | **A (Prompt Architect / Lead)/B (Tool & Schema Engineer)**  | Quản lý `system_prompt.md`, format JSON output, context carry-over & artifact version hash/Quản lý `tools.yaml`, chuẩn hóa tool enums/arguments, đồng bộ tool declarations, Tavily setup |
| 2 | Đinh Trường An | 2A202602393 | dinhtruongan | **C (Eval & Red-Team)** | Thiết kế 10 eval cases `eval_group.json` (G01–G10), chạy và rà soát 12 adversarial security attacks |
| 3 | Nguyễn Thọ Đạt | 2A202602484 | Usagshfil | **D (UI & Report Coordinator)** | Dựng Live Chat Streamlit (`app.py`), test kịch bản demo (rehearsal), tổng hợp báo cáo `REPORT.md` |

---

### Quy tắc cộng tác & Phối hợp (Team Rules):
- **Phân tách công việc:** Tránh conflict bằng cách mỗi vai trò chịu trách nhiệm chính trên artifact tương ứng (`system_prompt.md` cho A, `tools.yaml` cho B, `eval_group.json` cho C, `app.py` & `REPORT.md` cho D).
- **Git Contribution:** Mỗi thành viên làm việc trên branch riêng (`contrib/<username>`) và tạo ít nhất 1 commit có ý nghĩa trước khi merge vào repository chung của nhóm.
- **Nộp bài VLearn:** Toàn bộ thành viên nộp cùng một URL của repository chung đã hoàn thiện.

