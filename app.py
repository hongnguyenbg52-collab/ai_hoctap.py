import streamlit as st
import google.generativeai as genai

# Lấy khóa từ hệ thống bảo mật của Streamlit
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
except:
    st.error("Thiếu mã API trong phần Secrets!")

# Dùng model chuẩn xác nhất
model = genai.GenerativeModel('gemini-1.5-flash')

st.set_page_config(page_title="AI Học Tập", page_icon="📚")
st.title("📚 Trợ Lý Phân Tích Bài Học")

input_text = st.text_area("Nội dung bài học:", height=200)

if st.button("🚀 Phân tích ngay"):
    if input_text:
        with st.spinner('AI đang làm việc...'):
            try:
                response = model.generate_content(input_text)
                st.markdown("---")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Lỗi: {e}")
    else:
        st.warning("Hãy nhập nội dung trước nhé!")
