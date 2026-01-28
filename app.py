import streamlit as st
import google.generativeai as genai

# Cấu hình API xịn của bạn
GOOGLE_API_KEY = "AIzaSyBCmudyAOQeAFacBdkO0dL2eYtvFEylXiQ"
genai.configure(api_key=GOOGLE_API_KEY)

# ĐÂY LÀ DÒNG QUAN TRỌNG NHẤT: Sửa tên mô hình chuẩn xác
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="Học Tập Thông Minh AI", page_icon="📚")
st.title("📚 Trợ Lý Phân Tích Bài Học")

input_text = st.text_area("Nội dung cần tóm tắt:", height=250)

if st.button("🚀 Bắt đầu phân tích"):
    if input_text:
        with st.spinner('AI đang làm bài giúp bạn...'):
            try:
                prompt = f"Tóm tắt nội dung này thành các mục: Khái niệm, Đặc điểm, Ví dụ: {input_text}"
                response = model.generate_content(prompt)
                st.markdown("---")
                st.write(response.text)
                st.success("Xong rồi nè!")
            except Exception as e:
                st.error(f"Lỗi rồi: {e}")
    else:
        st.warning("Bạn chưa nhập nội dung!")
