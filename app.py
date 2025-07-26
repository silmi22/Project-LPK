import streamlit as st
from PIL import Image

st.set_page_config(page_title="Spektrum IR", page_icon="🔬", layout="centered")

st.markdown("<h1 style='text-align: center; color: teal;'>🔬 Interpretasi Spektrum IR</h1>", unsafe_allow_html=True)
st.markdown("""
Masukkan satu atau dua nilai bilangan gelombang IR (cm⁻¹) untuk mengidentifikasi kemungkinan gugus fungsi.  
Gunakan dua input jika ingin mendeteksi gugus kompleks seperti asam karboksilat.
""")

# Sidebar info tambahan
st.sidebar.title("📚 Informasi Tambahan")
opsi = st.sidebar.radio("Pilih salah satu:", ["—", "📖 Teori IR", "🎯 Tujuan Aplikasi", "👨‍💻 Pembuat Aplikasi", "refenresi data spektrum IR"])

if opsi == "📖 Teori IR":
    st.markdown("## 🧪 Teori Dasar Spektroskopi Inframerah (IR)")
    st.markdown("""
Spektroskopi Inframerah (IR) adalah teknik untuk *mengidentifikasi gugus fungsi dalam senyawa kimia* berdasarkan interaksi antara cahaya inframerah dan molekul.
Jenis analisis ini dapat digunakan untuk mengarakterisasi sampel dalam bentuk cairan, larutan, pasta, bubuk, film, serat, dan gas. Analisis ini juga memungkinkan untuk menganalisis material di permukaan substrat
### 🔬 Prinsip Dasar
Ketika molekul menyerap sinar inframerah, energi tersebut menyebabkan ikatan antar atom bergetar. Jenis getaran ini dapat berupa:
- *Regangan (stretching):* perubahan panjang ikatan
- *Tekukan (bending):* perubahan sudut ikatan
-sampel akan dikenai radiasi inframerah (IR). Radiasi IR ini kemudian memengaruhi getaran atom dari molekul dalam sampel, menghasilkan penyerapan dan/atau transmisi energi yang spesifik.

### 📏 Bilangan Gelombang
- IR diukur dalam satuan *bilangan gelombang (cm⁻¹)*.
- Setiap gugus fungsi menyerap pada rentang tertentu, menghasilkan *pita serapan* unik.

### 📌 Contoh Pita Serapan Umum
| Bilangan Gelombang (cm⁻¹) | Gugus Fungsi              | Keterangan                        |
|---------------------------|---------------------------|-----------------------------------|
| ~1700                     | *C=O*                   | Karbonil (keton, aldehid, ester) |
| >3200                     | *O–H* (lebar)           | Alkohol, Asam karboksilat        |
| ~2250                     | *C≡N* atau *C≡C*       | Nitril atau Alkuna               |
| 1600–1500                 | *C=C* aromatik          | Senyawa aromatik                 |
| ~3300                     | *N–H*, ≡C–H             | Amina, Asetilenik                |

### 🎯 Kegunaan Spektroskopi IR
- Mengidentifikasi *struktur senyawa* organik/anorganik
- Menentukan *gugus fungsi* spesifik
- Berguna dalam analisis *kualitatif* kimia, lingkungan, farmasi
""", unsafe_allow_html=True)

elif opsi == "🎯 Tujuan Aplikasi":
    st.success("""
Aplikasi ini bertujuan:
- Membantu pengguna menginterpretasikan data IR.
- Mempercepat identifikasi gugus fungsi.
- Menghubungkan spektrum IR dengan struktur senyawa organik.
    """)

elif opsi == "👨‍💻 Pembuat Aplikasi":
    st.warning("""
- *Nama*: [Annisa Balqis, Fachria, Marsya Putri, Nasywa Artha, Silmi]
- *Institusi*: [Contoh: Universitas X]
- Aplikasi dibuat dengan Python & Streamlit sebagai bagian dari tugas atau penelitian.
    """)

# Input bilangan gelombang
nilai1 = st.number_input("🧪 Masukkan bilangan gelombang Infra Red pertama (cm⁻¹)", min_value=1000, max_value=3800, step=1)
nilai2 = st.number_input("🧪 Masukkan bilangan gelombang Infra Red kedua (opsional)", min_value=0, max_value=3800, step=1)

# Data gugus fungsi 
gugus_fungsi = [
    {"rentang": (2970-2950, 2880-2860), "gugus": "C-H Stretch (Metil)",
    {"rentang": (1470-1430, 1380-1370), "gugus": "C-H Bending (Asam Karboksilat)", 
    {"rentang": (1385– 1380, 1370– 1365), "gugus": "C–H (Dimetil)", 
    {"rentang": (1395– 1385, 1365), "gugus": "C–H (Tersier Butil)", 
    {"rentang": (2850, 2750), "gugus": "C–H (Aldehid)", 
    {"rentang": (1300, 1000), "gugus": "C–O (Ester/Alkohol)",
    {"rentang": (1650, 1450), "gugus": "C=C (Aromatik)", 
    {"rentang": (2250, 2250), "gugus": "C≡N (Nitril)", 
    {"rentang": (2150, 2150), "gugus": "C≡C (Alkuna)",
]

# Tombol identifikasi
if st.button("🔍 Identifikasi"):

    hasil = []

    # Deteksi khusus asam karboksilat
    if (
        (1820 >= nilai1 >= 1660 and 3400 >= nilai2 >= 2400) or
        (1820 >= nilai2 >= 1660 and 3400 >= nilai1 >= 2400)
    ):
        st.success("🔴 Kemungkinan besar: Asam Karboksilat (–COOH)")
        st.image("https://i.imgur.com/purxZOP.png", caption="Struktur Asam Karboksilat", use_column_width=True)

    # Pengecekan nilai terhadap daftar gugus fungsi
    for nilai in [nilai1, nilai2]:
        if nilai == 0:
            continue
        cocok = False
        for item in gugus_fungsi:
            low, high = item["rentang"]
            if low >= nilai >= high or low <= nilai <= high:
                with st.container():
                    col1, col2 = st.columns([2, 1])
                    with col1:
                        st.success(f"✓ {nilai} cm⁻¹ → {item['gugus']}")
                    with col2:
                        st.image(item["img"], width=100)
                cocok = True
        if not cocok:
            st.error(f"✖ {nilai} cm⁻¹ → Tidak cocok dengan database.")
