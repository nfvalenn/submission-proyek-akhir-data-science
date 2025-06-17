## 🏢 Proyek Akhir: Jaya Jaya Institute

### 📌 Business Understanding

Institusi pendidikan tinggi menghadapi tantangan serius terkait tingkat **dropout** mahasiswa yang tinggi. Fenomena ini berdampak negatif terhadap **rasio kelulusan**, **efisiensi pembelajaran**, **citra institusi**, dan **pengelolaan sumber daya**. Ketidakmampuan dalam mengidentifikasi mahasiswa yang berisiko tinggi untuk keluar dapat menyebabkan kegagalan intervensi dini dan meningkatnya beban akademik serta administratif.

Faktor-faktor seperti **nilai akademik yang rendah**, **masalah finansial**, **kurangnya dukungan**, dan **faktor sosial-ekonomi** menjadi penyebab utama mahasiswa tidak menyelesaikan studinya. Oleh karena itu, diperlukan pendekatan berbasis data untuk memahami akar permasalahan dan mengembangkan sistem **deteksi dini** terhadap risiko dropout.

---

### ❗ Permasalahan Bisnis

Beberapa permasalahan utama yang dihadapi institusi adalah:

* Tingginya tingkat dropout pada program studi tertentu.
* Mahasiswa dengan nilai akademik rendah pada semester awal lebih berisiko tidak menyelesaikan studi.
* Mahasiswa yang tidak disiplin membayar UKT (Uang Kuliah Tunggal) cenderung mengalami kesulitan finansial dan akademik.
* Belum ada sistem prediksi otomatis yang mampu memberikan peringatan dini terhadap potensi dropout.
* Beberapa kelompok seperti **non-penerima beasiswa**, **mahasiswa dengan kebutuhan khusus**, atau **berusia lebih tua saat masuk kuliah** menunjukkan risiko lebih tinggi untuk dropout.

---

### 📦 Cakupan Proyek

Proyek ini mencakup:

* **Eksplorasi dan Pemahaman Data**: Analisis dataset dropout mahasiswa untuk mengenali karakteristik umum mereka.
* **Data Preparation**: Pra-pemrosesan dan pembersihan data agar siap untuk dimodelkan.
* **Analisis Faktor Penyebab Dropout**:

  * Korelasi antara nilai masuk, usia, status pembayaran, dan performa akademik awal terhadap dropout.
  * Visualisasi tren dropout berdasarkan gender, program studi, dan kategori spesifik lainnya.
* **Business Dashboard**: Visualisasi dalam Looker Studio untuk memantau pola dan risiko dropout.
* **Model Prediktif**: Menggunakan machine learning untuk memprediksi risiko dropout.
* **Rekomendasi Strategis**: Solusi konkret untuk mengurangi tingkat dropout.

---

### 🧪 Persiapan

* **Sumber Data**: Dataset yang digunakan dalam proyek ini adalah Dataset [Jaya Jaya Institute](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv) sesuai dengan instruksi dari submission proyek ini.
* **Tools**:

  * Python (pandas, matplotlib/seaborn, scikit-learn, xgboost)
  * Google Colab untuk analisis
  * Looker Studio untuk dashboard visualisasi
  * Streamlit untuk deploy aplikasi berbasis web
  * VsCode untuk membuat kode streamlitnya
* **Model Machine Learning** disimpan dalam format `.joblib` dan digunakan dalam aplikasi interaktif Streamlit.

---

### ⚙️ Setup Environment

Jika kamu belum membuat environment, berikut langkah opsional (namun direkomendasikan) untuk menjaga konsistensi dependensi:

#### 1. Buat Virtual Environment

```bash
python -m venv venv
```

#### 2. Aktifkan Virtual Environment

* **Windows**

```bash
venv\Scripts\activate
```


#### 3. Install Dependensi

Pastikan berada di root direktori proyek:

```bash
pip install -r requirements.txt
```

#### 4. Jalankan Aplikasi Streamlit Secara Lokal

```bash
streamlit run app.py
```

---

### 📊 Business Dashboard

Dashboard membantu pihak manajemen dan akademik untuk:

* Melihat sebaran mahasiswa berdasarkan usia, nilai, dan status beasiswa.
* Mengidentifikasi karakteristik umum mahasiswa yang dropout.
* Memantau hasil prediksi dropout dan performa akademik awal.
* Mengevaluasi efektivitas intervensi berdasarkan kelompok risiko.

📎 **Link Dashboard**: [Looker Studio - Jaya Jaya Institute](https://lookerstudio.google.com/reporting/477e15a5-35db-410a-ba02-4b69716d8e1a)

📎 **Link Aplikasi Prediksi Dropout (Streamlit)**: https://submission-proyek-akhir-data-science-nabila-febriyanti-valentin.streamlit.app/

---

### 🤖 Menjalankan Sistem Machine Learning
Prototipe sistem prediksi dropout telah dibuat berbasis web menggunakan Streamlit. Berikut cara menjalankannya:

```bash
streamlit run app.py
```

Atau akses langsung secara online melalui:

🔗 Link Aplikasi Streamlit:

https://submission-proyek-akhir-data-science-nabila-febriyanti-valentin.streamlit.app/

---

### ✅ Conclusion

Hasil proyek menunjukkan bahwa:

* **Nilai semester awal** (semester 1 dan 2) merupakan prediktor paling kuat untuk risiko dropout.
* **Kedisiplinan membayar UKT** dan **status debitur** sangat berkorelasi dengan peningkatan risiko dropout.
* **Mahasiswa yang tidak menerima beasiswa** dan **memiliki kebutuhan khusus** lebih rentan keluar dari sistem pendidikan.
* Model terbaik adalah **Random Forest** dengan **akurasi 92.6%** dan **F1-score > 92%**, yang siap digunakan sebagai alat bantu prediksi dropout mahasiswa secara real-time.
  
Karakteristik umum mahasiswa yang dropout adalah:
- Rata-rata nilai semester 1 & 2 di bawah 10.
- Tidak mendapatkan beasiswa.
- Status pembayaran tidak up to date.
- Tidak memiliki kredit semester sebelumnya.
- Berasal dari jalur pendaftaran dan program studi tertentu yang memiliki dropout rate tinggi.
  
---

### 🛠️ Rekomendasi Action Items

1. **Intervensi Akademik Dini**
   - Target: Mahasiswa dengan **nilai rata-rata semester 1 atau 2 < 10**.
   - Solusi: Program pembinaan akademik mingguan dan tutor sebaya.

2. **Perluasan Skema Beasiswa**
   - Target: Mahasiswa yang bukan penerima beasiswa dan memiliki nilai awal baik (≥10).
   - Solusi: Sistem seleksi otomatis berdasarkan data ekonomi & prestasi.

3. **Pendampingan Mahasiswa Baru & Berkebutuhan Khusus**
   - Solusi: Sistem onboarding, konseling awal, dan mentor inklusi sosial.

4. **Sistem Peringatan Dini Berbasis Machine Learning**
   - Implementasi: Dashboard Streamlit dengan integrasi model Random Forest.
   - Output: Risiko dropout & peringatan otomatis ke wali akademik.

5. **Layanan Konseling Terintegrasi**
   - Fokus: Masalah akademik, psikososial, dan finansial.
   - Target: Mahasiswa dengan skor risiko dropout > 0.7 (skala 0–1).
