import streamlit as st
import google.generativeai as genai

# CẤU HÌNH AI - Thay cái API Key của bạn vào đây
GOOGLE_API_KEY = "AIzaSyBCmudyAOQeAFacBdkO0dL2eYtvFEylXiQ"

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# GIAO DIỆN WEB
st.set_page_config(page_title="Học Tập Thông Minh AI", page_icon="📝")
st.title("📚 Trợ Lý Phân Tích Bài Học")
st.write("Dán nội dung bài học, AI sẽ chia ý giúp bạn dễ nhớ nhất!")

# Nhập liệu
input_text = st.text_area("Nội dung cần tóm tắt:", height=250, placeholder="Dán văn bản vào đây...")

if st.button("🚀 Bắt đầu phân tích"):
    if input_text:
        with st.spinner('AI đang đọc bài...'):
            prompt = f"""
            Hãy đóng vai một gia sư giỏi. Tóm tắt nội dung sau thành các mục:
            - 💡 Khái niệm chính: (Giải thích ngắn gọn)
            - 🔑 Tính chất/Đặc điểm: (Dạng gạch đầu dòng)
            - 📖 Ví dụ: (Dễ hiểu nhất)
            - 🧠 Mẹo ghi nhớ: (1 câu ngắn gọn)
            
            Nội dung: {input_text}
            """
            response = model.generate_content(prompt)
            st.markdown("---")
            st.markdown(response.text)
    else:
        st.warning("Bạn chưa nhập nội dung bài học kìa!")
