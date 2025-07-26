import streamlit as st

Atur halaman dan ikon

st.set_page_config(page_title="Aplikasi Infra Red Spektrum", page_icon="🌈")

Header utama

st.title("🌈 Interpretasi Spektrum IR") st.write("Aplikasi untuk membantu identifikasi gugus fungsi berdasarkan spektrum inframerah (IR)")

Sidebar navigasi

if "menu" not in st.session_state: st.session_state.menu = "🏠 Beranda"

menu = st.sidebar.selectbox("📂 Navigasi", ["🏠 Beranda", "📖 Teori IR", "🛠 Petunjuk Penggunaan", "🎯 Tujuan Aplikasi", "👨‍💻 Pembuat Aplikasi"," Referensi Spketrum IR], index=["🏠 Beranda", "📖 Teori IR", "🛠 Petunjuk Penggunaan", "🎯 Tujuan Aplikasi", "👨‍💻 Pembuat Aplikasi"].index(st.session_state.menu))

Tampilan Beranda

if menu == "🏠 Beranda": st.markdown(""" <div style='text-align: center;'> <h2>👋 Selamat Datang di Aplikasi Spektrum IR!</h2> <p style='font-size:18px;'>Temukan gugus fungsi dari spektrum IR dengan mudah dan cepat</p> <img src='https://i.imgur.com/mg8OaRG.png' width='300'/> </div> """, unsafe_allow_html=True)

st.markdown("---")

st.info("🎓 Aplikasi ini cocok digunakan oleh:")
st.markdown("""
- Mahasiswa kimia atau farmasi
- Praktikan di laboratorium
- Pengajar yang ingin memberikan alat bantu ajar
- Peneliti atau analis spektrum senyawa organik
""")

st.success("📌 Silakan pilih menu di sidebar kiri untuk mulai menggunakan aplikasi.")

Tampilan Teori IR

elif menu == "📖 Teori IR": st.markdown("## 🧪 Teori Dasar Spektroskopi Inframerah (IR)") st.markdown(""" Spektroskopi Inframerah (IR) adalah teknik untuk mengidentifikasi gugus fungsi dalam senyawa kimia berdasarkan interaksi antara cahaya inframerah dan molekul.

🔬 Prinsip Dasar

Ketika molekul menyerap sinar inframerah, energi tersebut menyebabkan ikatan antar atom bergetar. Jenis getaran ini dapat berupa:

Regangan (stretching): perubahan panjang ikatan

Tekukan (bending): perubahan sudut ikatan
Secara singkat, spektrum IR dibagi menjadi tiga wilayah spektrum:

Spektrum IR jauh (far-IR): < 400 cm⁻¹

Spektrum IR tengah (mid-IR): 400–4000 cm⁻¹

Spektrum IR dekat (near-IR): 4000–13000 cm⁻¹

Spektrum IR tengah adalah yang paling sering digunakan dalam analisis sampel, namun spektrum IR jauh dan dekat juga memberikan informasi penting tentang sampel yang dianalisis. Studi ini difokuskan pada analisis FTIR di wilayah spektrum IR tengah.

Spektrum IR tengah dibagi ke dalam empat wilayah:

Wilayah ikatan tunggal: 2500–4000 cm⁻¹

Wilayah ikatan rangkap tiga: 2000–2500 cm⁻¹

Wilayah ikatan rangkap dua: 1500–2000 cm⁻¹

Wilayah sidik jari (fingerprint): 600–1500 cm⁻¹


📏 Panjang Gelombang dan Bilangan Gelombang

Panjang gelombang IR biasanya dinyatakan dalam satuan bilangan gelombang (cm⁻¹).

Setiap gugus fungsi menyerap pada rentang bilangan gelombang tertentu.


📌 Contoh Pita Serapan Umum

Bilangan Gelombang (cm⁻¹)	Gugus Fungsi	Keterangan

~1700	C=O	Karbonil (keton, aldehid, ester)
>3200	O–H (lebar)	Alkohol, Asam karboksilat
~2250	C≡N atau C≡C	Nitril atau Alkuna
1600–1500	C=C aromatik	Senyawa aromatik
~3300	N–H atau ≡C–H	Amina, Asetilenik


🎯 Fungsi Spektroskopi IR

Mengidentifikasi struktur senyawa organik atau anorganik

Menentukan keberadaan gugus fungsi spesifik

Mendukung analisis kualitatif dalam kimia, farmasi, dan lingkungan """, unsafe_allow_html=True)


Tampilan Petunjuk

elif menu == "🛠 Petunjuk Penggunaan": st.markdown("## 🛠 Petunjuk Penggunaan") st.markdown("""

1. Siapkan data spektrum IR Anda (misalnya hasil FTIR).


2. Perhatikan puncak-puncak utama dan nilai bilangan gelombangnya (dalam cm⁻¹).


3. Bandingkan dengan tabel referensi atau gunakan fitur identifikasi otomatis jika tersedia.


4. Cocokkan dengan kemungkinan gugus fungsi. """)



Tampilan Tujuan Aplikasi

elif menu == "🎯 Tujuan Aplikasi": st.markdown("## 🎯 Tujuan Aplikasi") st.markdown("""

Membantu mahasiswa dalam menginterpretasi spektrum IR

Menjadi media pembelajaran interaktif dalam kimia organik

Mempermudah identifikasi gugus fungsi dari data eksperimen """)


Tampilan Pembuat

elif menu == "👨‍💻 Pembuat Aplikasi": st.markdown("## 👨‍💻 Tentang Pembuat Aplikasi") st.markdown(""" Nama: Nasywa Arta
Institusi: Politeknik AKA Bogor
Keterangan: Aplikasi ini dibuat untuk membantu praktikum dan tugas akhir mata kuliah Kimia Instrumental. """)
# Input gelombang
nilai1 = st.number_input("Bilangan gelombang IR pertama (cm⁻¹)", min_value=1000, max_value=3800, step=1)
nilai2 = st.number_input("Bilangan gelombang IR kedua (opsional)", min_value=0, max_value=3800, step=1)

# Daftar rentang dan gugus 
gugus_fungsi = [
    {"rentang": (1820, 1660), "gugus": "C=O (Karbonil umum: Aldehid, Keton, Ester, Asam Karboksilat, Amida, Anhidrida)"},
    {"rentang": (3400, 2400), "gugus": "O–H (Asam Karboksilat) – sangat lebar, overlap dengan C–H"},
    {"rentang": (3600, 3300), "gugus": "O–H (Alkohol / Fenol)"},
    {"rentang": (3500, 3500), "gugus": "N–H (Amina / Amida)"},
    {"rentang": (2850, 2750), "gugus": "C–H (Aldehid) – dua pita lemah"},
    {"rentang": (1810, 1710), "gugus": "C=O (Anhidrida) – dua pita"},
    {"rentang": (1300, 1000), "gugus": "C–O (Ester, Alkohol, Eter, Asam Karboksilat)"},
    {"rentang": (1650, 1650), "gugus": "C=C (Alkena)"},
    {"rentang": (1650, 1450), "gugus": "C=C (Aromatik)"},
    {"rentang": (3000, 3000), "gugus": "C–H aromatik/vinil (sebelah kiri 3000 cm⁻¹)"},
    {"rentang": (3000, 3000), "gugus": "C–H alifatik (sebelah kanan 3000 cm⁻¹)"},
    {"rentang": (2250, 2250), "gugus": "C≡N (Nitril)"},
    {"rentang": (2150, 2150), "gugus": "C≡C (Alkuna)"},
    {"rentang": (3300, 3300), "gugus": "≡C–H (asetilenik)"},
    {"rentang": (1600, 1500), "gugus": "NO₂ – pita kuat"},
    {"rentang": (1390, 1300), "gugus": "NO₂ – pita tambahan"},
    {"rentang": (1450, 1450), "gugus": "C–H bending (CH₃, CH₂)"},
    {"rentang": (1375, 1375), "gugus": "C–H bending (CH₃, CH₂)"},
]

# Tombol identifikasi
if st.button("Identifikasi"):

    hasil = []

    # Cek kombinasi asam karboksilat
    if (
        (1820 >= nilai1 >= 1660 and 3400 >= nilai2 >= 2400) or
        (1820 >= nilai2 >= 1660 and 3400 >= nilai1 >= 2400)
    ):
        hasil.append("🔴 *Kemungkinan besar: Asam Karboksilat (–COOH)*")

    # Cek masing-masing nilai terhadap daftar rentang
    for nilai in [nilai1, nilai2]:
        if nilai == 0:
            continue
        cocok = False
        for item in gugus_fungsi:
            if item["rentang"][0] >= nilai >= item["rentang"][1] or item["rentang"][0] <= nilai <= item["rentang"][1]:
                hasil.append(f"✓ {nilai} cm⁻¹ → {item['gugus']}")
                cocok = True
        if not cocok:
            hasil.append(f"✖ {nilai} cm⁻¹ → Tidak dikenali dalam daftar.")

    # Tampilkan hasil
    if hasil:
        st.markdown("### Hasil Identifikasi:")
        for h in hasil:
            st.markdown(h)
    else:
        st.warning("Tidak ada nilai yang dikenali.")
