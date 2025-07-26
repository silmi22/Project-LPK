import streamlit as st

# Atur halaman
st.set_page_config(page_title="Aplikasi IR Spektrum", page_icon="🌈")

# Sidebar Navigasi
menu = st.sidebar.selectbox(
    "📂 Navigasi",
    ["🏠 Beranda", "📖 Teori IR", "🛠 Petunjuk Penggunaan", "🎯 Tujuan Aplikasi", "👨‍💻 Pembuat Aplikasi"]
)

# Tampilan Header Umum
st.title("🌈 Interpretasi Spektrum IR")
st.write("Aplikasi untuk membantu identifikasi gugus fungsi berdasarkan spektrum inframerah (IR).")

# Halaman Beranda
if menu == "🏠 Beranda":
    st.markdown("""
    <div style='text-align: center;'>
        <h2>👋 Selamat Datang di Aplikasi Spektrum IR!</h2>
        <p style='font-size:18px;'>Temukan gugus fungsi dari spektrum IR dengan mudah dan cepat.</p>
        <img src='https://i.imgur.com/mg8OaRG.png' width='300'/>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.info("🎓 Aplikasi ini cocok digunakan oleh:")
    st.markdown("""
    - Mahasiswa kimia atau farmasi  
    - Praktikan di laboratorium  
    - Pengajar yang ingin memberikan alat bantu ajar  
    - Peneliti atau analis spektrum senyawa organik
    """)

    st.success("📌 Silakan pilih menu di sidebar kiri untuk mulai menggunakan aplikasi.")

# Halaman Teori IR
elif menu == "📖 Teori IR":
    st.markdown("## 🧪 Teori Dasar Spektroskopi Inframerah (IR)")
    st.markdown("""
Spektroskopi Inframerah (IR) adalah teknik untuk mengidentifikasi gugus fungsi dalam senyawa kimia berdasarkan interaksi antara cahaya inframerah dan molekul.

### 🔬 Prinsip Dasar
Ketika molekul menyerap sinar inframerah, energi tersebut menyebabkan ikatan antar atom bergetar. Jenis getaran ini dapat berupa:
- *Regangan (stretching)*: perubahan panjang ikatan  
- *Tekukan (bending)*: perubahan sudut ikatan  

### 📏 Bilangan Gelombang (cm⁻¹)
Setiap gugus fungsi menyerap energi IR pada rentang bilangan gelombang tertentu.

### 📌 Contoh Pita Serapan Umum
| Bilangan Gelombang | Gugus Fungsi         | Keterangan                        |
|--------------------|----------------------|-----------------------------------|
| ~1700 cm⁻¹         | C=O                  | Karbonil (keton, aldehid, ester) |
| >3200 cm⁻¹         | O–H (lebar)          | Alkohol, Asam karboksilat        |
| ~2250 cm⁻¹         | C≡N atau C≡C         | Nitril atau Alkuna               |
| 1600–1500 cm⁻¹     | C=C aromatik         | Senyawa aromatik                 |
| ~3300 cm⁻¹         | N–H atau ≡C–H        | Amina, Asetilenik                |

### 🎯 Fungsi Spektroskopi IR
- Mengidentifikasi struktur senyawa organik/anorganik  
- Menentukan gugus fungsi spesifik  
- Mendukung analisis kualitatif dalam bidang kimia, farmasi, lingkungan  
""", unsafe_allow_html=True)

# Halaman Petunjuk Penggunaan
elif menu == "🛠 Petunjuk Penggunaan":
    st.markdown("## 🛠 Petunjuk Penggunaan")
    st.markdown("""
1. Siapkan data spektrum IR Anda (misalnya hasil FTIR).  
2. Perhatikan puncak-puncak utama dan nilai bilangan gelombangnya (dalam cm⁻¹).  
3. Bandingkan dengan tabel referensi atau gunakan fitur identifikasi otomatis jika tersedia.  
4. Cocokkan dengan kemungkinan gugus fungsi.  
""")

# Halaman Tujuan Aplikasi
elif menu == "🎯 Tujuan Aplikasi":
    st.markdown("## 🎯 Tujuan Aplikasi")
    st.markdown("""
- Membantu mahasiswa dalam menginterpretasi spektrum IR  
- Menjadi media pembelajaran interaktif dalam kimia organik  
- Mempermudah identifikasi gugus fungsi dari data eksperimen  
""")

# Halaman Pembuat Aplikasi
elif menu == "👨‍💻 Pembuat Aplikasi":
    st.markdown("## 👨‍💻 Tentang Pembuat Aplikasi")
    st.markdown("""
Aplikasi ini dibuat oleh:

- *Annisa Balqis*  
- *Fachria*  
- *Marsya Putri*  
- *Nasywa*  
- *Silmi*

📍 *Institusi*: Politeknik AKA Bogor  
🎯 *Tujuan: Mendukung kegiatan praktikum dan tugas akhir pada mata kuliah **Kimia Instrumental* dengan bantuan aplikasi berbasis Python dan Streamlit.
""")
