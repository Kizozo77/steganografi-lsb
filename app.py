import io
import streamlit as st
from PIL import Image

# ==============================================================================
# FAVICON KUSTOM SVG (MATRIKS PIKSEL & STEGANOGRAFI)
# ==============================================================================
FAVICON_SVG = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">
  <rect x="4" y="4" width="56" height="56" rx="8" fill="#FFDE59" stroke="#000000" stroke-width="5"/>
  <rect x="14" y="14" width="14" height="14" fill="#5CE1E6" stroke="#000000" stroke-width="3"/>
  <rect x="36" y="14" width="14" height="14" fill="#FFFFFF" stroke="#000000" stroke-width="3"/>
  <rect x="14" y="36" width="14" height="14" fill="#FFFFFF" stroke="#000000" stroke-width="3"/>
  <rect x="36" y="36" width="14" height="14" fill="#FF914D" stroke="#000000" stroke-width="3"/>
  <circle cx="43" cy="43" r="3" fill="#000000"/>
</svg>
"""

st.set_page_config(
    page_title="Steganografi LSB",
    page_icon=FAVICON_SVG,
    layout="centered"
)

# ==============================================================================
# GAYA NEOBRUTALISME RAPI & BERSIH TOTAL
# ==============================================================================
def terapkan_tema_neobrutalisme():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&display=swap');

    /* Sembunyikan Toolbar Atas, Dekorasi & Lencana/Profil Bawah */
        [data-testid="stToolbar"],
        [data-testid="stHeader"],
        [data-testid="stDecoration"],
        [data-testid="manage-app-button"],
        [class*="viewerBadge"],
        [class*="profileContainer"],
        [class*="StatusWidget"],
        #MainMenu,
    footer {
        display: none !important;
        visibility: hidden !important;
        opacity: 0 !important;
        pointer-events: none !important;
    }

    /* Font & Warna Dasar */
    .stApp, .nb-header, .nb-box, .nb-result, p, label, h1, h2, h3, textarea, input {
        font-family: 'Space Grotesk', sans-serif !important;
        color: #111111 !important;
    }

    .stApp, [data-testid="stAppViewContainer"] {
        background-color: #FDFBF7 !important;
        color: #111111 !important;
    }

    .block-container {
        max-width: 740px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* Header Neobrutalisme */
    .nb-header {
        background-color: #FFDE59;
        border: 3px solid #000000;
        box-shadow: 6px 6px 0px #000000;
        padding: 1.5rem;
        margin-bottom: 2rem;
        text-align: center;
    }
    .nb-header h1 {
        margin: 0;
        font-size: 2rem;
        font-weight: 700;
        color: #000000 !important;
        letter-spacing: -0.5px;
    }
    .nb-header p {
        margin: 0.4rem 0 0 0;
        font-size: 0.95rem;
        color: #111111 !important;
        font-weight: 500;
    }

    /* Tab Navigasi Neobrutalisme */
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px;
        border-bottom: none !important;
        margin-bottom: 1.4rem;
        background-color: transparent !important;
    }
    .stTabs button[data-baseweb="tab"] {
        background-color: #FFFFFF !important;
        border: 2px solid #000000 !important;
        box-shadow: 4px 4px 0px #000000 !important;
        border-radius: 0px !important;
        padding: 10px 22px !important;
        margin: 0 !important;
        opacity: 1 !important;
        transition: all 0.1s ease-in-out;
    }
    .stTabs button[data-baseweb="tab"] p {
        color: #000000 !important;
        font-weight: 700 !important;
        font-size: 0.95rem !important;
        margin: 0 !important;
    }
    .stTabs button[data-baseweb="tab"]:hover {
        background-color: #FFF3B0 !important;
        transform: translate(-1px, -1px);
        box-shadow: 5px 5px 0px #000000 !important;
    }
    .stTabs button[aria-selected="true"] {
        background-color: #5CE1E6 !important;
        transform: translate(2px, 2px) !important;
        box-shadow: 2px 2px 0px #000000 !important;
    }
    .stTabs [data-baseweb="tab-highlight"],
    .stTabs [data-baseweb="tab-border"] {
        display: none !important;
    }

    /* Kotak Area File Uploader */
    [data-testid="stFileUploaderDropzone"] {
        background-color: #FFFFFF !important;
        border: 2px dashed #000000 !important;
        border-radius: 0px !important;
        box-shadow: 4px 4px 0px #000000 !important;
        padding: 1.2rem 1.4rem !important;
    }
    [data-testid="stFileUploaderDropzoneInstructions"] div,
    [data-testid="stFileUploaderDropzoneInstructions"] span,
    [data-testid="stFileUploaderDropzoneInstructions"] small {
        color: #111111 !important;
        font-weight: 500 !important;
    }

    /* HANYA Tombol Utama Browse Files di Dropzone (Tidak mengenai tombol hapus X) */
    [data-testid="stFileUploaderDropzone"] > button {
        background-color: #FFDE59 !important;
        color: #000000 !important;
        border: 2px solid #000000 !important;
        border-radius: 0px !important;
        box-shadow: 3px 3px 0px #000000 !important;
        padding: 0.45rem 1.2rem !important;
        font-family: 'Space Grotesk', sans-serif !important;
        font-weight: 700 !important;
        font-size: 0.9rem !important;
        white-space: nowrap !important;
        min-width: 140px !important;
        cursor: pointer !important;
    }
    [data-testid="stFileUploaderDropzone"] > button span,
    [data-testid="stFileUploaderDropzone"] > button svg {
        display: none !important;
    }
    [data-testid="stFileUploaderDropzone"] > button::after {
        content: "Pilih Gambar";
        color: #000000 !important;
        font-weight: 700 !important;
    }
    [data-testid="stFileUploaderDropzone"] > button:hover {
        background-color: #5CE1E6 !important;
        transform: translate(-1px, -1px);
        box-shadow: 4px 4px 0px #000000 !important;
    }

    /* Kartu File yang Sudah Diunggah (Terang & Kontras) */
    [data-testid="stFileUploaderFile"] {
        background-color: #FFFDF5 !important;
        border: 2px solid #000000 !important;
        box-shadow: 3px 3px 0px #000000 !important;
        border-radius: 0px !important;
        padding: 8px 12px !important;
        margin-top: 12px !important;
    }
    [data-testid="stFileUploaderFile"] div,
    [data-testid="stFileUploaderFile"] span,
    [data-testid="stFileUploaderFile"] small {
        color: #000000 !important;
        font-weight: 600 !important;
    }
    /* Tombol Hapus File (X) agar tetap rapi & kecil */
    [data-testid="stFileUploaderDeleteBtn"] button {
        background-color: #FF6B6B !important;
        color: #000000 !important;
        border: 2px solid #000000 !important;
        border-radius: 0px !important;
        padding: 2px 6px !important;
        min-width: auto !important;
        box-shadow: 2px 2px 0px #000000 !important;
    }
    [data-testid="stFileUploaderDeleteBtn"] button::after {
        content: none !important;
    }

    /* Kotak Input Teks & Text Area */
    .stTextArea textarea, .stTextInput input {
        background-color: #FFFFFF !important;
        border: 2px solid #000000 !important;
        border-radius: 0px !important;
        box-shadow: 4px 4px 0px #000000 !important;
        color: #000000 !important;
        font-size: 0.95rem !important;
    }
    .stTextArea textarea::placeholder {
        color: #666666 !important;
        opacity: 1 !important;
    }

    /* Tombol Aksi Utama & Tombol Download */
    .stButton > button, .stDownloadButton > button {
        background-color: #FF914D !important;
        border: 2px solid #000000 !important;
        border-radius: 0px !important;
        box-shadow: 4px 4px 0px #000000 !important;
        padding: 0.65rem 1.2rem !important;
        transition: all 0.1s ease-in-out;
        width: 100%;
    }
    .stButton > button p, .stDownloadButton > button p {
        color: #000000 !important;
        font-weight: 700 !important;
    }
    .stButton > button:hover, .stDownloadButton > button:hover {
        background-color: #FFDE59 !important;
        transform: translate(-1px, -1px);
        box-shadow: 5px 5px 0px #000000 !important;
    }
    .stButton > button:active, .stDownloadButton > button:active {
        transform: translate(3px, 3px);
        box-shadow: 1px 1px 0px #000000 !important;
    }
    .stDownloadButton > button {
        background-color: #7ED957 !important;
    }

    /* Kotak Info Kapasitas & Hasil */
    .nb-box {
        background-color: #FFFFFF;
        border: 2px solid #000000;
        box-shadow: 4px 4px 0px #000000;
        padding: 1rem 1.2rem;
        margin: 0.5rem 0 1rem 0;
        color: #111111 !important;
    }
    .nb-box code {
        background-color: #FFDE59 !important;
        color: #000000 !important;
        border: 1px solid #000000;
        padding: 2px 6px;
        font-weight: 700;
    }
    .nb-result {
        background-color: #E8F8F5;
        border: 2px solid #000000;
        box-shadow: 4px 4px 0px #000000;
        padding: 1.2rem;
        margin-top: 0.8rem;
        font-family: monospace !important;
        font-size: 1rem;
        color: #000000 !important;
        white-space: pre-wrap;
        word-break: break-word;
    }
    </style>
    """, unsafe_allow_html=True)

terapkan_tema_neobrutalisme()

# ==============================================================================
# LOGIKA INTI STEGANOGRAFI LSB
# ==============================================================================
PENANDA_AKHIR = "#####"

def teks_ke_biner(teks):
    return ''.join(format(ord(karakter), '08b') for karakter in teks)

def sisipkan_pesan(gambar_pil, pesan_rahasia):
    gambar = gambar_pil.convert('RGB')
    lebar, tinggi = gambar.size
    
    pesan_lengkap = pesan_rahasia + PENANDA_AKHIR
    biner_pesan = teks_ke_biner(pesan_lengkap)
    panjang_biner = len(biner_pesan)
    
    kapasitas_maksimal = lebar * tinggi * 3
    if panjang_biner > kapasitas_maksimal:
        raise ValueError(f"Pesan terlalu panjang! Maksimal {kapasitas_maksimal // 8} karakter.")
    
    piksel = list(gambar.getdata())
    piksel_baru = []
    indeks_bit = 0
    
    for r, g, b in piksel:
        if indeks_bit < panjang_biner:
            r = (r & ~1) | int(biner_pesan[indeks_bit])
            indeks_bit += 1
        if indeks_bit < panjang_biner:
            g = (g & ~1) | int(biner_pesan[indeks_bit])
            indeks_bit += 1
        if indeks_bit < panjang_biner:
            b = (b & ~1) | int(biner_pesan[indeks_bit])
            indeks_bit += 1
        piksel_baru.append((r, g, b))
    
    gambar_stego = Image.new('RGB', (lebar, tinggi))
    gambar_stego.putdata(piksel_baru)
    
    buffer = io.BytesIO()
    gambar_stego.save(buffer, format="PNG")
    buffer.seek(0)
    return buffer

def ekstrak_pesan(gambar_pil):
    gambar = gambar_pil.convert('RGB')
    piksel = list(gambar.getdata())
    
    kumpulan_bit = ""
    pesan_hasil = ""
    
    for r, g, b in piksel:
        for warna in (r, g, b):
            kumpulan_bit += str(warna & 1)
            if len(kumpulan_bit) == 8:
                karakter = chr(int(kumpulan_bit, 2))
                pesan_hasil += karakter
                kumpulan_bit = ""
                if pesan_hasil.endswith(PENANDA_AKHIR):
                    return pesan_hasil[:-len(PENANDA_AKHIR)]
    return ""

# ==============================================================================
# ANTARMUKA PENGGUNA (UI WEB)
# ==============================================================================
st.markdown("""
<div class="nb-header">
    <h1>STEGANOGRAFI METODE LSB</h1>
    <p>Sisipkan dan Ekstrak Pesan Rahasia pada Citra Digital secara Lossless</p>
</div>
""", unsafe_allow_html=True)

tab_encode, tab_decode = st.tabs(["ENCODE (SISIPKAN PESAN)", "DECODE (BACA PESAN)"])

with tab_encode:
    st.markdown("### 1. Unggah Gambar Asli (Cover Image)")
    file_asli = st.file_uploader(
        "Pilih file gambar (PNG, JPG, JPEG, BMP)", 
        type=["png", "jpg", "jpeg", "bmp"], 
        key="upload_encode"
    )
    
    if file_asli is not None:
        img_asli = Image.open(file_asli)
        lebar, tinggi = img_asli.size
        maks_karakter = max(0, ((lebar * tinggi * 3) // 8) - len(PENANDA_AKHIR))
        
        col1, col2 = st.columns([1, 1.3])
        with col1:
            st.image(img_asli, caption="Pratinjau Gambar", use_container_width=True)
        with col2:
            st.markdown(f"""
            <div class="nb-box">
                <strong>Detail Citra Digital:</strong><br><br>
                • Nama File: <code>{file_asli.name}</code><br>
                • Resolusi: <b>{lebar} x {tinggi} px</b><br>
                • Kapasitas Maksimal: <b>{maks_karakter:,} karakter</b>
            </div>
            """, unsafe_allow_html=True)
            
        st.markdown("### 2. Tulis Pesan Rahasia")
        pesan_input = st.text_area(
            "Masukkan teks rahasia yang ingin disembunyikan:", 
            height=130, 
            placeholder="Ketik pesan rahasia Anda di sini..."
        )
        st.caption(f"Jumlah karakter saat ini: {len(pesan_input):,} / {maks_karakter:,} karakter")
        
        if st.button("PROSES & BUAT GAMBAR STEGO (.PNG)"):
            if not pesan_input.strip():
                st.warning("Pesan rahasia tidak boleh kosong!")
            elif len(pesan_input) > maks_karakter:
                st.error("Pesan melebihi kapasitas maksimal gambar ini!")
            else:
                try:
                    hasil_buffer = sisipkan_pesan(img_asli, pesan_input)
                    st.success("Pesan berhasil disisipkan! Silakan unduh gambar stego di bawah ini.")
                    st.download_button(
                        label="UNDUH GAMBAR STEGO (.PNG)",
                        data=hasil_buffer,
                        file_name="hasil_stego_lsb.png",
                        mime="image/png"
                    )
                except Exception as e:
                    st.error(f"Terjadi kesalahan: {e}")

with tab_decode:
    st.markdown("### 1. Unggah Gambar Stego (.PNG / .BMP)")
    file_stego = st.file_uploader(
        "Wajib menggunakan file lossless hasil encode (.PNG atau .BMP)", 
        type=["png", "bmp"], 
        key="upload_decode"
    )
    
    if file_stego is not None:
        img_stego = Image.open(file_stego)
        st.image(img_stego, caption="Gambar Stego yang Akan Diperiksa", width=280)
        
        if st.button("EKSTRAK PESAN RAHASIA"):
            with st.spinner("Memindai bit LSB setiap piksel..."):
                try:
                    pesan_terbaca = ekstrak_pesan(img_stego)
                    if pesan_terbaca:
                        st.success("Pesan rahasia ditemukan!")
                        st.markdown("**Hasil Pesan Rahasia:**")
                        st.markdown(f'<div class="nb-result">{pesan_terbaca}</div>', unsafe_allow_html=True)
                    else:
                        st.warning("Tidak ditemukan pesan rahasia pada gambar ini.")
                except Exception as e:
                    st.error(f"Gagal membaca gambar: {e}")