import streamlit as st

Atur halaman dan ikon

st.set_page_config(page_title="Aplikasi Infra Red Spektrum", page_icon="🌈")

Header utama

st.title("🌈 Interpretasi Spektrum Infra Red") st.write("Aplikasi untuk membantu identifikasi gugus fungsi berdasarkan spektrum inframerah (IR)")

Sidebar navigasi

if "menu" not in st.session_state: st.session_state.menu = "🏠 Beranda"

menu = st.sidebar.selectbox("📂 Navigasi", ["🏠 Beranda", "📖 Teori IR", "🛠 Petunjuk Penggunaan", "🎯 Tujuan Aplikasi", "👨‍💻 Pembuat Aplikasi","Referensi Spektrum Infra Merah], index=["🏠 Beranda", "📖 Teori IR", "🛠 Petunjuk Penggunaan", "🎯 Tujuan Aplikasi", "👨‍💻 Pembuat Aplikasi"].index(st.session_state.menu))

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

elif menu == "📖 Teori IR": st.markdown("## 🧪 Teori Dasar Spektroskopi Inframerah (IR)") st.markdown(""" Fourier Transform Infra Red(FTIR) adalah salah satu teknik analisis penting bagi para peneliti. jenis analisis ini dapat digunakan untuk mengarakterisasi sampel dalam bentuk cairan, lauran, pasta, bubul, film, serat, dan gas. Analisis ini juga memmungkinkan untuk menganalisis permukaan substrat.

🔬 Prinsip Dasar

Sampel akan dikenai radiasi infra red (IR). Radiasi IR ini kemudian memengaruhi getaran atom dari molekul dalam sampel, menghasilkan penyerapan dan/atau transmisi energi yang spesifik.


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

Secara singkat, spektrum IR dibagi menjadi tiga wilayah spektrym:
Spektrum IR jauh (far-IR): < 400 cm⁻¹

Spektrum IR tengah (mid-IR): 400–4000 cm⁻¹

Spektrum IR dekat (near-IR): 4000–13000 cm⁻¹

Spektrum IR tengah adalah yang paling sering digunakan dalam analisis sampel, namun spektrum IR jauh dan dekat juga memberikan informasi penting tentang sampel yang dianalisis. Studi ini difokuskan pada analisis FTIR di wilayah spektrum IR tengah.

Spektrum IR tengah dibagi ke dalam empat wilayah:

Wilayah ikatan tunggal: 2500–4000 cm⁻¹

Wilayah ikatan rangkap tiga: 2000–2500 cm⁻¹

Wilayah ikatan rangkap dua: 1500–2000 cm⁻¹

Wilayah sidik jari (fingerprint): 600–1500 cm⁻¹


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

Memahami makna dari spektrum Infra Red

Menjadi media pembelajaran interaktif dalam kimia organik

Mempermudah identifikasi gugus fungsi dari data eksperimen """)


Tampilan Pembuat

elif menu == "👨‍💻 Pembuat Aplikasi": st.markdown("## 👨‍💻 Tentang Pembuat Aplikasi") st.markdown(""" Nama: Annisa Balqis, Fachria, Marsya Putri, Nasywa Artha, Silmi
Institusi: Politeknik AKA Bogor
Keterangan: Aplikasi ini dibuat untuk membantu praktikum dan tugas akhir mata kuliah Kimia Instrumental. """)



   
            
