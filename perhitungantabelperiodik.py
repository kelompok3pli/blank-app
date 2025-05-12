# Data sederhana untuk contoh
tabel_periodik = {
    "H": {"nama": "Hidrogen", "nomor_atom": 1, "massa_atom": 1.008},
    "He": {"nama": "Helium", "nomor_atom": 2, "massa_atom": 4.0026},
    "O": {"nama": "Oksigen", "nomor_atom": 8, "massa_atom": 15.999},
    "C": {"nama": "Karbon", "nomor_atom": 6, "massa_atom": 12.011},
    # Tambahkan data lainnya sesuai kebutuhan
}

# Sidebar
st.sidebar.title("KalkulatorMr")
menu = st.sidebar.radio("Pilih Menu", [
    "Lihat Tabel Periodik",
    "Cari Unsur Berdasarkan Simbol",
    "Hitung Massa Molekul"
])

# Halaman 1: Lihat Tabel Periodik
if menu == "Lihat Tabel Periodik":
    st.title("Tabel Periodik Sederhana")
    st.write("Berikut adalah beberapa unsur dari tabel periodik:")
    for simbol, info in tabel_periodik.items():
        st.write(f"**{simbol}** - {info['nama']} | Nomor Atom: {info['nomor_atom']} | Massa Atom: {info['massa_atom']}")

# Halaman 2: Cari Unsur
elif menu == "Cari Unsur Berdasarkan Simbol":
    st.title("Cari Unsur")
    simbol = st.text_input("Masukkan simbol unsur (contoh: H, He, O)")
    if simbol:
        unsur = tabel_periodik.get(simbol)
        if unsur:
            st.success(f"Nama: {unsur['nama']}")
            st.write(f"Nomor Atom: {unsur['nomor_atom']}")
            st.write(f"Massa Atom: {unsur['massa_atom']}")
        else:
            st.error("Simbol tidak ditemukan dalam data.")

# Halaman 3: Hitung Massa Molekul
elif menu == "Hitung Massa Molekul":
    st.title("Kalkulator Massa Molekul")
    rumus = st.text_input("Masukkan rumus kimia (misalnya: H2O, CO2)")

    import re
    def hitung_massa_molekul(rumus):
        pola = r"([A-Z][a-z]*)(\d*)"
        total = 0.0
        for simbol, jumlah in re.findall(pola, rumus):
            jumlah = int(jumlah) if jumlah else 1
            if simbol in tabel_periodik:
                massa = tabel_periodik[simbol]["massa_atom"]
                total += massa * jumlah
            else:
                return None
        return total

    if rumus:
        hasil = hitung_massa_molekul(rumus)
        if hasil is not None:
            st.success(f"Massa molekul dari {rumus} adalah {hasil:.3f} uma")
        else:
            st.error("Rumus mengandung simbol yang tidak dikenal.")
