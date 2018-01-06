dari  __future__  import with_statement
impor kembali
# #
# Setup.py Astroboyy ??
# JANGAN EDIT ??
# Terima kasih ??
# #
coba :
    dari setuptools import setup
kecuali  ImportError :
    dari ez_setup import use_setuptools
    use_setuptools ()
    dari setuptools import setup



mempersiapkan(
        nama = ' LINETCR ' ,
        paket = [ ' LINETCR ' ],
        versi = ' 0.9.9.9 ' ,
        deskripsi = ' Semoga Waifu bersamamu ... ' ,
        lisensi = ' BSD License ' ,
        author = ' Astroboyy ' ,
        author_email = ' asttroboy01@gmail.com ' ,
        url = ' canseethefuture.org ' ,
        kata kunci = [ ' LINETCR ' ],
        classifier = [
            ' Status Pengembangan :: 2 - Pre-Alpha ' ,
            ' Lingkungan :: Konsol ' ,
            ' Pemirsa yang Dituju :: Pengembang ' ,
            ' Lisensi :: OSI Disetujui :: Lisensi BSD ' ,
            ' Sistem Operasi :: OS Independen ' ,
            ' Bahasa Pemrograman :: Python ' ,
            ' Bahasa Pemrograman :: Python :: 2 ' ,
            ' Bahasa Pemrograman :: Python :: 2.6 ' ,
            ' Bahasa Pemrograman :: Python :: 2.7 ' ,
            ' Bahasa Pemrograman :: Python :: 3 ' ,
            ' Bahasa Pemrograman :: Python :: 3.1 ' ,
            ' Bahasa Pemrograman :: Python :: 3.2 ' ,
            ' Bahasa Pemrograman :: Python :: 3.3 ' ,
            ' Bahasa Pemrograman :: Python :: Implementasi :: CPython ' ,
            ' Bahasa Pemrograman :: Python :: Implementasi :: PyPy ' ,
            ' Topic :: Pengembangan Perangkat Lunak :: Perpustakaan :: Modul Python ' ,
            ' Topic :: Internet :: WWW / HTTP :: Konten Dinamis ' ,
            ' Topic :: Communications :: Chat ' ,
        ],
        install_requires = [
            ' permintaan ' ,
            ' kurva ' ,
            ' rsa ' ,
		' hemat == 0.9.3 '
        ],
    )