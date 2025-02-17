# intelligent-control-week1

Proyek ini adalah bagian dari mata kuliah Praktikum Kontrol Cerdas pada Program Studi Perkeretaapian Politeknik Negeri Madiun. Proyek ini bertujuan untuk mendeteksi objek dan warna tertentu (merah, biru, hijau, kuning) dalam video yang diambil dari kamera dan menampilkan bounding box di sekitar objek yang terdeteksi.

## Fitur

- Deteksi warna merah, biru, hijau, dan kuning dalam video.
- Menampilkan bounding box di sekitar objek yang terdeteksi.
- Menampilkan teks nama objek atau warna di dalam bounding box.

## Persyaratan

- Python 3.x
- OpenCV
- NumPy
- torch
- ultralytics

## Instalasi

1. Clone repositori ini:
    ```bash
    git clone https://github.com/Kevinbyup84/intelligent-control-week1.git
    ```
2. Masuk ke direktori proyek:
    ```bash
    cd intelligent-control-week1
    ```
3. Instal dependensi yang diperlukan:
    ```bash
    pip install opencv-python numpy torch ultralytics
    ```

## Penggunaan

1. Jalankan skrip `Assignment Deteksi Warna.py`:
    ```bash
    python Assignment Deteksi Warna.py
    ```
2. Skrip akan membuka jendela video yang menampilkan hasil deteksi warna dengan bounding box dan teks warna.

3. Contoh hasil deteksi warna dapat dilihat pada 'Result.JPG'

4. Jalankan skrip `Praktikum Deteksi Objek.py`:
    ```bash
    python Praktikum Deteksi Objek.py
    ```
5. Skrip akan membuka jendela video yang menampilkan hasil deteksi objek dengan bounding box dan Label yang berisi nama kelas objek dan confidence score.
