import streamlit as st

# Sidebar info tambahan
opsi = st.sidebar.radio("📚 Pilihan Informasi Tambahan:", ["—", "Teori IR(infra red)", "Tujuan Aplikasi", "Pembuat Aplikasi"])

if opsi == "Teori Infra Red":
    st.subheader("📖 Teori Dasar Spektrum IR")
    st.markdown("""
Spektroskopi Inframerah (IR) digunakan untuk mengidentifikasi gugus fungsi berdasarkan getaran ikatan dalam molekul.  
Setiap gugus memiliki rentang frekuensi tertentu yang menyerap sinar IR(infra red), menghasilkan *pita serapan* pada spektrum.

- Getaran ikatan seperti *regangan (stretching)* dan *tekukan (bending)* menghasilkan pita serapan.
- Misalnya, ikatan C=O biasanya muncul pada sekitar *1700 cm⁻¹, sementara O–H yang lebar muncul di atas **3200 cm⁻¹*.
    """)

elif opsi == "Tujuan Aplikasi":
    st.subheader("🎯 Tujuan Aplikasi")
    st.markdown("""
Aplikasi ini bertujuan untuk membantu pengguna, terutama pelajar dan mahasiswa, dalam:
- Menginterpretasikan panjang gelombang IR menjadi *kemungkinan gugus fungsi*,
- Meningkatkan pemahaman *korelasi antara spektrum dan struktur senyawa*,
- Mempercepat proses analisis kualitatif senyawa organik berdasarkan data IR.
    """)

elif opsi == "Pembuat Aplikasi":
    st.subheader("👨‍💻 Pembuat Aplikasi")
    st.markdown("""
- *Nama*: [Annisa Balqis, Fachria Ilmi, Marsya Putri, Nasywa Artha, Silmi Kaffah]
- *Institusi*: [Politeknik AKA Bogor]
- *Keterangan: Aplikasi ini dikembangkan menggunakan **Python* dan *Streamlit* sebagai bagian dari tugas/penelitian untuk interpretasi spektrum IR.
    """)

# Judul dan penjelasan utama
st.title("Interpretasi Spektrum Infra Red")
st.markdown("""
Masukkan satu atau dua nilai bilangan gelombang IR (cm⁻¹) untuk mengidentifikasi kemungkinan gugus fungsi. 🖥 
Gunakan dua input jika ingin mendeteksi gugus kompleks seperti asam karboksilat.🔎
""")

# Input gelombang
nilai1 = st.number_input("Bilangan gelombang Infra Red pertama (cm⁻¹)", min_value=1000, max_value=3600, step=1)
nilai2 = st.number_input("Bilangan gelombang Infa Red kedua (opsional)", min_value=0, max_value=3600, step=1)

# Daftar rentang dan gugus (sesuai slide)
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
        hasil.append("🔴 Kemungkinan besar: Asam Karboksilat (–COOH)")

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
