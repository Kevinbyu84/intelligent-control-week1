# intelligent-control-week1

Proyek ini adalah bagian dari mata kuliah Praktikum Kontrol Cerdas pada Program Studi Perkeretaapian Politeknik Negeri Madiun. Proyek ini bertujuan untuk mendeteksi warna tertentu (merah, biru, hijau, kuning) dalam video yang diambil dari kamera dan menampilkan bounding box di sekitar objek yang terdeteksi.

## Fitur

- Deteksi warna merah, biru, hijau, dan kuning dalam video.
- Menampilkan bounding box di sekitar objek yang terdeteksi.
- Menampilkan teks warna di dalam bounding box.

## Persyaratan

- Python 3.x
- OpenCV
- NumPy

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
    pip install opencv-python numpy
    ```

## Penggunaan

1. Jalankan skrip `Deteksi Warna.py`:
    ```bash
    python Deteksi Warna.py
    ```
2. Skrip akan membuka jendela video yang menampilkan hasil deteksi warna dengan bounding box dan teks warna.

3. Contoh hasil deteksi warna dapat dilihat pada 'Result.JPG'

## Analisis dan Diskusi

Analisis Hasil:
- Apa yang terjadi saat objek berwarna merah muncul di kamera?
    Ketika terdapat objek berwarna merah muncul di kamera akan terdeteksi oleh sistem sehingga akan terbentuk bounding box yang mendeteksi objek berwarna merah
- Bagaimana sistem mendeteksi dan memfilter warna merah?
    Dalam sistem ini pendeteksian warna menggunakan teknik pemrosesan citra dengan OpenCV. Berikut adalah langkah-langkah yang dilakukan:
    1. Konversi Warna: Gambar dari kamera dikonversi dari ruang warna BGR (Blue, Green, Red) ke ruang warna HSV (Hue, Saturation, Value).
    ```python
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    ```
    2. Definisi Rentang Warna: Rentang ini mencakup nilai-nilai Hue, Saturation, dan Value yang sesuai dengan warna. Contoh HSV warna merah:
    ```python
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    ```
    3. Deteksi Kontur: Kontur (batas objek) dalam gambar biner ditemukan menggunakan fungsi cv2.findContours.
    ```python
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    ```
    4. Bounding Box: Bounding box digambar di sekitar kontur yang terdeteksi. Hanya kontur dengan area yang lebih besar dari nilai tertentu yang akan ditampilkan untuk menghindari deteksi noise atau objek kecil.
    ```python
    for contour in contours_red:
    x, y, w, h = cv2.boundingRect(contour)
    if w * h > 10000:  # Hanya tampilkan bounding box yang besar
        cv2.rectangle(result, (x, y), (x + w, y + h), (0, 0, 255), 2)  # Warna merah
        cv2.putText(result, "Merah", (x + 5, y + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    ```
- Bagaimana metode ini dapat diterapkan dalam intelligent control systems?
    Metode deteksi warna dan bounding box ini dapat diterapkan dalam sistem kontrol cerdas seperti pada sistem pengawasan, robotika, dan kendaraan otonom.

Diskusi:
- Bagaimana AI dapat meningkatkan sistem kontrol berbasis Computer Vision?
    Penggunaan AI dapat meningkatkan akurasi deteksi dengan dilatih dengan akurasi yang lebih baik. AI dapat terus belajar dan beradaotasi sehingga dapat memperbaiki kinerja dan mengurangi kesalahan.
- Apa kelebihan dan kekurangan metode deteksi objek berbasis warna?
    Kelebihan metode ini relatif sederhana dan cepat untuk diimplementasikan, tidak memerlukan komputasi yang berat. Aplikasi penggunaan yang luas seperti robotika dan pengawasan.
    Kekurangan metode ini sangat sensitif terhadap perubahan kondisi pencahayaan. Dapat mendeteksi noise atau objek kecil yang tidak relevan jika tidak ada filter tambahan untuk menghilangkan deteksi yang tidak diinginkan.
- Bagaimana cara meningkatkan akurasi sistem deteksi objek?
    Untuk meningkatkan akurasi sistem deteksi objek, dapat dilakukan dengan beberapa hal seperti kalibrasi kamera, peningkatan resolusi gambar, dan penyesuaian rentang warna.