import streamlit as st
import numpy as np
import joblib
import os

# Atur konfigurasi halaman
st.set_page_config(page_title="🎓 Prediksi Dropout Mahasiswa", layout="wide")

# Navigasi Halaman
pages = ["🏠 Beranda", "🔍 Prediksi"]
page = st.sidebar.radio("Navigasi", pages)

# CSS Custom untuk warna coklat soft
theme_css = """
<style>
body {
    background-color: #f7f0e8;
}
h1, h2, h3, h4, h5, h6 {
    color: #5e4632;
}
.stApp {
    background-color: #f7f0e8;
}
.sidebar .sidebar-content {
    background-color: #f3e9dd;
}
.css-1d391kg {
    background-color: #fffaf3;
}
</style>
"""
st.markdown(theme_css, unsafe_allow_html=True)

# Halaman Beranda
if page == "🏠 Beranda":
    st.markdown("""
    <iframe width="100%" height="700" src="https://lookerstudio.google.com/embed/reporting/477e15a5-35db-410a-ba02-4b69716d8e1a/page/z1GNF" frameborder="0" style="border:1px solid #ccc; border-radius:10px;" allowfullscreen></iframe>
    """, unsafe_allow_html=True)
    st.markdown("Oleh: Nabila Febriyanti Valentin/@nfvalenn02")

# Halaman Prediksi
elif page == "🔍 Prediksi":
    st.title("🔍 Prediksi Risiko Dropout Mahasiswa")

    # Load model
    model_path = os.path.join(os.path.dirname(__file__), "model", "model.joblib")
    if not os.path.exists(model_path):
        st.error("❌ File model `model.joblib` tidak ditemukan.")
        st.stop()
    model = joblib.load(model_path)

    with st.form("form_prediksi"):
        col1, col2 = st.columns(2)
        with col1:
            course_options = {
                33: 'Computer Science',
                171: 'Nursing',
                8014: 'Business Management',
                9003: 'Law',
                9070: 'Psychology',
                9991: 'Veterinary Nursing',
                9085: 'Social Service',
                9119: 'Tourism',
                9130: 'Communication Design',
                9147: 'Marketing',
                9238: 'Journalism and Communication',
                9254: 'Basic Education',
                9500: 'Management',
                9556: 'Accounting',
                9670: 'Solicitor',
                9773: 'Management (Evening)',
                9853: 'Social Work (Evening)'
            }
            course_name = st.selectbox("🎓 Program Studi", list(course_options.values()))
            Course = [k for k, v in course_options.items() if v == course_name][0]

            Admission_grade = st.number_input("📝 Nilai Masuk (0–200)", min_value=0.0, max_value=200.0, value=100.0)
            Gender = st.selectbox("👤 Jenis Kelamin", [("Laki-laki", 0), ("Perempuan", 1)], format_func=lambda x: x[0])[1]
            Age_at_enrollment = st.number_input("🎂 Usia Saat Masuk Kuliah", min_value=16, max_value=60, value=18)
            Curricular_units_1st_sem_grade = st.number_input("📚 Nilai Rata-rata Semester 1 (0–20)", 0.0, 20.0, 10.0)

        with col2:
            Educational_special_needs = st.selectbox("🧩 Kebutuhan Khusus?", [("Tidak", 0), ("Ya", 1)], format_func=lambda x: x[0])[1]
            Debtor = st.selectbox("💸 Memiliki Tunggakan?", [("Tidak", 0), ("Ya", 1)], format_func=lambda x: x[0])[1]
            Tuition_fees_up_to_date = st.selectbox("💳 UKT Tepat Waktu?", [("Ya", 1), ("Tidak", 0)], format_func=lambda x: x[0])[1]
            Scholarship_holder = st.selectbox("🎁 Penerima Beasiswa?", [("Ya", 1), ("Tidak", 0)], format_func=lambda x: x[0])[1]
            Curricular_units_2nd_sem_grade = st.number_input("📚 Nilai Rata-rata Semester 2 (0–20)", 0.0, 20.0, 10.0)

        submitted = st.form_submit_button("🔍 Prediksi")

    if submitted:
        input_data = np.array([[Course, Admission_grade, Gender, Age_at_enrollment,
                                Educational_special_needs, Debtor, Tuition_fees_up_to_date,
                                Scholarship_holder, Curricular_units_1st_sem_grade,
                                Curricular_units_2nd_sem_grade]])
        try:
            prediction = model.predict(input_data)[0]
            probas = model.predict_proba(input_data)[0]
            st.subheader("📊 Hasil Prediksi")
            if prediction == 1:
                st.error(f"🚨 Mahasiswa diprediksi **Dropout** dengan probabilitas {probas[1]:.2%}.")
            elif prediction == 2:
                st.success(f"🎓 Mahasiswa diprediksi **Lulus** dengan probabilitas {probas[2]:.2%}.")
            else:
                st.info(f"✅ Mahasiswa **Tidak Dropout** dengan probabilitas {probas[0]:.2%}.")
        except Exception as e:
            st.error(f"❌ Terjadi kesalahan saat memprediksi: {e}")
