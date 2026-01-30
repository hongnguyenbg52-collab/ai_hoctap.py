import streamlit as st
import google.generativeai as genai

# --- PHẦN CẤU HÌNH QUAN TRỌNG ---
# Bạn dán mã API vào giữa hai dấu ngoặc kép bên dưới.
# Tui đã thêm lệnh .strip() để tự sửa lỗi nếu bạn lỡ copy thừa dấu cách.
# Thay dòng chữ bên dưới bằng mã thật của bạn (bắt đầu bằng AIza...)
my_api_key = "AIzaSyBCmudyAOQeAFacBdkO0dL2eYtvFEylXiQ"

# Cấu hình API (Thêm .strip() để xóa dấu cách thừa - Chữa lỗi 400)
genai.configure(api_key=my_api_key.strip())

# Chọn model chuẩn (Không dùng models/ hay latest nữa cho đỡ lỗi)
model = genai.GenerativeModel('gemini-pro')

# --- GIAO DIỆN WEB ---
st.set_page_config(page_title="Trợ Lý Học Tập", page_icon="🤖")
st.title("🤖 Trợ Lý Phân Tích Bài Học")
st.write("Dán bài học vào đây, AI sẽ tóm tắt giúp bạn!")

# Ô nhập liệu
input_text = st.text_area("Nội dung cần tóm tắt:", height=200)

# Nút bấm xử lý
if st.button("🚀 Phân tích ngay"):
    if input_text:
        with st.spinner('Đang đọc bài... đợi xíu nha...'):
            try:
                # Gửi yêu cầu cho AI
                prompt = f"Hãy tóm tắt nội dung sau thành các gạch đầu dòng dễ nhớ: {input_text}"
                response = model.generate_content(prompt)
                
                # Hiển thị kết quả
                st.markdown("---")
                st.success("Xong rồi nè! 👇")
                st.markdown(response.text)
            except Exception as e:
                st.error("Vẫn lỗi hả? Chụp màn hình gửi tui xem nhé!")
                st.error(f"Chi tiết lỗi: {e}")
    else:
        st.warning("Ơ kìa, bạn chưa dán bài học vào!")
