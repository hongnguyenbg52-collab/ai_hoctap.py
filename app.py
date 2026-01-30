import streamlit as st
import google.generativeai as genai

# Kết nối với "Két sắt" Secrets
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"Lỗi cấu hình: {e}")

st.title("📚 Trợ Lý Học Tập AI")

input_text = st.text_area("Dán bài học vào đây:", height=200)

if st.button("🚀 Phân tích ngay"):
    if input_text:
        with st.spinner('AI đang làm bài...'):
            try:
                # Cách gọi đơn giản nhất
                response = model.generate_content(input_text)
                st.markdown("---")
                st.write(response.text)
            except Exception as e:
                st.error(f"Lỗi kết nối AI: {e}")
    else:
        st.warning("Nhập nội dung đã bạn ơi!")
