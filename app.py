import streamlit as st
import google.generativeai as genai

# 1. Lấy mã API từ "Két sắt" Secrets mà bạn đã dán lúc nãy
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
except:
    st.error("Lỗi: Không tìm thấy mã API trong phần Secrets của Streamlit!")

# 2. Sử dụng tên model chuẩn nhất
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="AI Học Tập", page_icon="📚")
st.title("📚 Trợ Lý Phân Tích Bài Học")

# Ô nhập bài học
input_text = st.text_area("Dán nội dung bài học vào đây:", height=200)

if st.button("🚀 Phân tích ngay"):
    if input_text:
        with st.spinner('AI đang đọc bài...'):
            try:
                # Gửi yêu cầu cho AI xử lý
                response = model.generate_content(f"Tóm tắt nội dung này thật dễ hiểu: {input_text}")
                st.markdown("---")
                st.success("Kết quả đây nè!")
                st.write(response.text)
            except Exception as e:
                st.error(f"Lỗi rồi: {e}")
    else:
        st.warning("Bạn chưa nhập nội dung bài kìa!")
