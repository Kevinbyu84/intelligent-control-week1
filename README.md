***Assignment Deteksi Warna***

**Ringkasan Alur Kode Assignment Deteksi Warna**

    *   Mengimpor library dan menginisialisasi kamera.
    *   Membaca frame dari kamera.
    *   Mengubah format warna dari BGR ke HSV.
    *   Membuat mask untuk setiap warna yang ingin dideteksi.
    *   Mencari kontur dalam setiap mask warna.
    *   Menggambar bounding box dan menambahkan teks pada objek yang terdeteksi.
    *   Menampilkan gambar hasil.
    *   Menunggu penekanan tombol 'q' untuk keluar dari loop.
    *   Melepaskan sumber daya kamera dan menutup semua jendela.

**Penjelasan Kode Assignment Deteksi Warna**

```python
import cv2
import numpy as np
```

*   `import cv2`: Mengimpor library OpenCV (cv2) yang digunakan untuk pengolahan citra dan video.
*   `import numpy as np`: Mengimpor library NumPy (np) yang digunakan untuk operasi matematika, terutama untuk array.

```python
# Inisialisasi kamera
cap = cv2.VideoCapture(0)
```

*   `cap = cv2.VideoCapture(0)`: Membuat objek `VideoCapture` dari OpenCV untuk mengakses kamera. Angka 0 menunjukkan kamera default (biasanya kamera internal). Jika Anda memiliki lebih dari satu kamera, Anda mungkin perlu mengubah angka ini (misalnya, 1 untuk kamera eksternal).

```python
while True:
    ret, frame = cap.read()  # Unpack the return value
    if not ret:
        print("Error: Could not read frame.")
        break
```

*   `while True:`: Memulai loop tak terbatas yang akan terus berjalan sampai dihentikan secara manual.
*   `ret, frame = cap.read()`: Membaca frame (bingkai) dari kamera.
    *   `ret` adalah nilai boolean yang menunjukkan apakah frame berhasil dibaca (True) atau tidak (False).
    *   `frame` adalah array NumPy yang berisi data gambar dari frame yang diambil.
*   `if not ret:`: Memeriksa apakah frame berhasil dibaca. Jika tidak, cetak pesan kesalahan dan keluar dari loop.
*   `break`: Menghentikan loop `while`.

```python
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
```

*   `hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)`: Mengubah format warna dari BGR (Blue, Green, Red) menjadi HSV (Hue, Saturation, Value). HSV lebih mudah digunakan untuk deteksi warna karena memisahkan informasi warna (Hue) dari kecerahan (Value) dan intensitas warna (Saturation).

```python
    # Rentang warna merah dalam HSV
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])

    # Rentang warna biru dalam HSV
    lower_blue = np.array([94, 80, 2])
    upper_blue = np.array([126, 255, 255])

    # Rentang warna hijau dalam HSV
    lower_green = np.array([25, 52, 72])
    upper_green = np.array([102, 255, 255])

    # Rentang warna kuning dalam HSV
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])
```

*   Bagian ini mendefinisikan rentang warna dalam format HSV yang akan dideteksi. Setiap warna (merah, biru, hijau, kuning) memiliki batas bawah (`lower_`) dan batas atas (`upper_`). Nilai-nilai ini ditentukan sebagai array NumPy.
    *   **Hue (H)**: Nilai warna (0-179 dalam OpenCV, mewakili 0-360 derajat).
    *   **Saturation (S)**: Intensitas warna (0-255).
    *   **Value (V)**: Kecerahan warna (0-255).
*   Rentang nilai ini perlu disesuaikan berdasarkan kondisi pencahayaan dan warna objek yang ingin dideteksi.

```python
    # Masking untuk mendeteksi warna merah, biru, hijau, dan kuning
    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
```

*   `cv2.inRange(hsv, lower_color, upper_color)`: Membuat "mask" (topeng) untuk setiap warna. Mask adalah gambar biner (hitam dan putih) di mana piksel putih menunjukkan area yang berada dalam rentang warna yang ditentukan, dan piksel hitam menunjukkan area di luar rentang.
    *   `hsv`: Gambar input dalam format HSV.
    *   `lower_color`: Batas bawah rentang warna.
    *   `upper_color`: Batas atas rentang warna.

```python
    result = frame.copy()
```

*   `result = frame.copy()`: Membuat salinan dari frame asli. Salinan ini akan digunakan untuk menggambar bounding box dan teks pada objek yang terdeteksi.

```python
    # Menemukan kontur untuk warna merah
    contours_red, _ = cv2.findContours(mask_red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours_red:
        x, y, w, h = cv2.boundingRect(contour)
        if w * h > 10000:  # Hanya tampilkan bounding box yang besar
            cv2.rectangle(result, (x, y), (x + w, y + h), (0, 0, 255), 2)  # Warna merah
            cv2.putText(result, "Merah", (x + 5, y + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Menemukan kontur untuk warna biru
    contours_blue, _ = cv2.findContours(mask_blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours_blue:
        x, y, w, h = cv2.boundingRect(contour)
        if w * h > 10000:  # Hanya tampilkan bounding box yang besar
            cv2.rectangle(result, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Warna biru
            cv2.putText(result, "Biru", (x + 5, y + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # Menemukan kontur untuk warna hijau
    contours_green, _ = cv2.findContours(mask_green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours_green:
        x, y, w, h = cv2.boundingRect(contour)
        if w * h > 10000:  # Hanya tampilkan bounding box yang besar
            cv2.rectangle(result, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Warna hijau
            cv2.putText(result, "Hijau", (x + 5, y + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Menemukan kontur untuk warna kuning
    contours_yellow, _ = cv2.findContours(mask_yellow, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours_yellow:
        x, y, w, h = cv2.boundingRect(contour)
        if w * h > 10000:  # Hanya tampilkan bounding box yang besar
            cv2.rectangle(result, (x, y), (x + w, y + h), (0, 255, 255), 2)  # Warna kuning
            cv2.putText(result, "Kuning", (x + 5, y + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
```

*   Bagian ini melakukan deteksi kontur dan menggambar bounding box di sekitar objek yang terdeteksi untuk setiap warna.
    *   `cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)`: Menemukan kontur dalam mask warna.
        *   `mask`: Mask warna yang telah dibuat sebelumnya.
        *   `cv2.RETR_TREE`: Mode pengambilan kontur yang menyusun kontur dalam hierarki pohon.
        *   `cv2.CHAIN_APPROX_SIMPLE`: Metode aproksimasi kontur yang menyimpan hanya titik-titik ujung kontur yang penting.
    *   `for contour in contours_color:`: Melakukan iterasi melalui setiap kontur yang ditemukan.
    *   `x, y, w, h = cv2.boundingRect(contour)`: Mendapatkan koordinat (x, y), lebar (w), dan tinggi (h) dari bounding box yang mengelilingi kontur.
    *   `if w * h > 10000:`: Memeriksa apakah area bounding box cukup besar (dalam hal ini, lebih dari 10000 piksel persegi). Ini digunakan untuk menghindari deteksi objek kecil yang mungkin merupakan noise.
    *   `cv2.rectangle(result, (x, y), (x + w, y + h), (B, G, R), 2)`: Menggambar persegi panjang (bounding box) di sekitar objek yang terdeteksi pada gambar `result`.
        *   `(x, y)`: Koordinat sudut kiri atas bounding box.
        *   `(x + w, y + h)`: Koordinat sudut kanan bawah bounding box.
        *   `(B, G, R)`: Warna bounding box dalam format BGR (Blue, Green, Red).
        *   `2`: Ketebalan garis bounding box.
    *   `cv2.putText(result, "Nama Warna", (x + 5, y + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (B, G, R), 2)`: Menambahkan teks yang menunjukkan nama warna di atas bounding box.
        *   `"Nama Warna"`: Teks yang akan ditampilkan.
        *   `(x + 5, y + 20)`: Koordinat posisi teks.
        *   `cv2.FONT_HERSHEY_SIMPLEX`: Jenis font yang digunakan.
        *   `0.5`: Skala font.
        *   `(B, G, R)`: Warna teks.
        *   `2`: Ketebalan garis teks.

```python
    # Menampilkan hasil
    cv2.imshow("Result", result)
```

*   `cv2.imshow("Result", result)`: Menampilkan gambar `result` (dengan bounding box dan teks) dalam jendela dengan judul "Result".

```python
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
```

*   `cv2.waitKey(1)`: Menunggu penekanan tombol selama 1 milidetik.
*   `& 0xFF`: Digunakan untuk mengambil 8 bit terakhir dari nilai yang dikembalikan oleh `cv2.waitKey()`. Ini penting karena `cv2.waitKey()` mengembalikan kode ASCII tombol yang ditekan.
*   `ord('q')`: Mendapatkan kode ASCII dari tombol 'q'.
*   Jika tombol 'q' ditekan, maka kondisi ini akan bernilai `True`, dan `break` akan menghentikan loop `while`.

```python
cap.release()
cv2.destroyAllWindows()
```

*   `cap.release()`: Melepaskan sumber daya yang digunakan oleh objek `VideoCapture`. Ini penting untuk membebaskan kamera agar dapat digunakan oleh aplikasi lain.
*   `cv2.destroyAllWindows()`: Menutup semua jendela OpenCV yang terbuka.


***Praktikum Deteksi Objek***

**Ringkasan Alur Kode Praktikum Deteksi Objek**

    *   Mengimpor library, memuat model YOLO, dan membuka kamera.
    *   Membaca frame dari kamera.
    *   Melakukan deteksi objek pada frame.
    *   Menggambar bounding box dan label pada frame untuk setiap objek yang terdeteksi.
    *   Menampilkan frame hasil.
    *   Memeriksa apakah tombol 'q' ditekan untuk keluar dari loop.
    *   Melepaskan sumber daya kamera dan menutup semua jendela.

**Penjelasan Kode Praktikum Deteksi Objek**

```python
import torch
import cv2
import numpy as np
from ultralytics import YOLO
```

*   `import torch`: Mengimpor library PyTorch. PyTorch adalah framework machine learning yang digunakan oleh YOLO.
*   `import cv2`: Mengimpor library OpenCV untuk pengolahan citra dan video.
*   `import numpy as np`: Mengimpor library NumPy untuk operasi numerik, terutama untuk array.
*   `from ultralytics import YOLO`: Mengimpor kelas `YOLO` dari library `ultralytics`. `ultralytics` adalah library yang memudahkan penggunaan model YOLOv5 dan YOLOv8.

```python
# Load the YOLO model
model = YOLO("yolov5s.pt")  # Pastikan Anda memiliki model YOLO yang sesuai
```

*   `model = YOLO("yolov5s.pt")`: Membuat instance dari kelas `YOLO` dan memuat model YOLO.
    *   `"yolov5s.pt"` adalah path ke file model YOLO yang telah dilatih. Dalam kasus ini, ini adalah model YOLOv5s yang telah dilatih sebelumnya. Pastikan Anda telah mengunduh file model ini dan menyimpannya di lokasi yang sesuai. Anda dapat mengunduh model YOLOv5 dari [repositori YOLOv5 resmi](https://github.com/ultralytics/yolov5).

```python
# Open the webcam
cap = cv2.VideoCapture(0)  # Ganti dengan URL kamera jika perlu
```

*   `cap = cv2.VideoCapture(0)`: Membuat objek `VideoCapture` dari OpenCV untuk mengakses kamera.
    *   `0` menunjukkan indeks kamera default (biasanya kamera internal). Jika Anda memiliki beberapa kamera, Anda bisa mengganti `0` dengan indeks kamera yang sesuai (misalnya, `1` untuk kamera eksternal).
    *   Jika Anda ingin menggunakan video dari file, Anda bisa mengganti `0` dengan path ke file video (misalnya, `"video.mp4"`).
    *   Jika Anda ingin menggunakan stream dari URL (misalnya, IP camera), Anda bisa mengganti `0` dengan URL stream tersebut.

```python
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
```

*   `while cap.isOpened():`: Memulai loop tak terbatas yang akan terus berjalan selama kamera terbuka (yaitu, selama `cap.isOpened()` mengembalikan `True`).
*   `ret, frame = cap.read()`: Membaca frame dari kamera.
    *   `ret` adalah nilai boolean yang menunjukkan apakah frame berhasil dibaca (True) atau tidak (False).
    *   `frame` adalah array NumPy yang berisi data gambar dari frame yang diambil.
*   `if not ret:`: Memeriksa apakah frame berhasil dibaca. Jika tidak, keluar dari loop.
*   `break`: Menghentikan loop `while`.

```python
    # Perform object detection
    results = model(frame)
```

*   `results = model(frame)`: Melakukan deteksi objek pada frame menggunakan model YOLO yang telah dimuat. Hasil deteksi (bounding box, confidence score, class) disimpan dalam variabel `results`.

```python
    # Draw bounding boxes and labels
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            cls = int(box.cls[0])
            label = f"{model.names[cls]} {conf:.2f}"
            
            # Draw rectangle and label
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
```

*   Bagian ini menggambar bounding box dan label pada frame untuk setiap objek yang terdeteksi.
    *   `for result in results:`: Loop melalui setiap hasil deteksi. Dalam beberapa versi `ultralytics`, `results` mungkin sudah berupa list deteksi, jadi loop ini mungkin tidak diperlukan.
    *   `for box in result.boxes:`: Loop melalui setiap bounding box dalam hasil deteksi. `result.boxes` berisi informasi tentang bounding box, confidence score, dan class dari objek yang terdeteksi.
    *   `x1, y1, x2, y2 = map(int, box.xyxy)`: Mendapatkan koordinat bounding box.
        *   `box.xyxy` adalah tensor yang berisi koordinat bounding box dalam format $$x1, y1, x2, y2], di mana (x1, y1) adalah koordinat sudut kiri atas dan (x2, y2) adalah koordinat sudut kanan bawah.
        *   `map(int, ...)` mengubah nilai koordinat menjadi integer.
    *   `conf = float(box.conf)`: Mendapatkan confidence score (tingkat keyakinan) dari deteksi.
        *   `box.conf` adalah tensor yang berisi confidence score.
        *   `float(...)` mengubah confidence score menjadi float.
    *   `cls = int(box.cls)`: Mendapatkan indeks class dari objek yang terdeteksi.
        *   `box.cls` adalah tensor yang berisi indeks class.
        *   `int(...)` mengubah indeks class menjadi integer.
    *   `label = f"{model.names[cls]} {conf:.2f}"`: Membuat label yang akan ditampilkan pada bounding box.
        *   `model.names[cls]` mendapatkan nama class dari list `model.names` menggunakan indeks class.
        *   `{conf:.2f}` memformat confidence score menjadi string dengan dua angka desimal.
    *   `cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)`: Menggambar persegi panjang (bounding box) pada frame.
        *   `(x1, y1)`: Koordinat sudut kiri atas bounding box.
        *   `(x2, y2)`: Koordinat sudut kanan bawah bounding box.
        *   `(0, 255, 0)`: Warna bounding box (hijau) dalam format BGR.
        *   `2`: Ketebalan garis bounding box.
    *   `cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)`: Menambahkan teks (label) di atas bounding box.
        *   `label`: Teks yang akan ditampilkan.
        *   `(x1, y1 - 10)`: Koordinat posisi teks.
        *   `cv2.FONT_HERSHEY_SIMPLEX`: Jenis font yang digunakan.
        *   `0.5`: Skala font.
        *   `(0, 255, 0)`: Warna teks (hijau) dalam format BGR.
        *   `2`: Ketebalan garis teks.

```python
    # Show the frame
    cv2.imshow("YOLO Real-time Object Detection", frame)
    
    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
```

*   `cv2.imshow("YOLO Real-time Object Detection", frame)`: Menampilkan frame dengan bounding box dan label dalam jendela dengan judul "YOLO Real-time Object Detection".
*   `if cv2.waitKey(1) & 0xFF == ord('q'):`: Memeriksa apakah tombol 'q' ditekan. Jika ya, keluar dari loop.
*   `break`: Menghentikan loop `while`.

```python
# Release resources
cap.release()
cv2.destroyAllWindows()
```

*   `cap.release()`: Melepaskan sumber daya yang digunakan oleh objek `VideoCapture`. Ini penting untuk membebaskan kamera agar dapat digunakan oleh aplikasi lain.
*   `cv2.destroyAllWindows()`: Menutup semua jendela OpenCV yang terbuka.