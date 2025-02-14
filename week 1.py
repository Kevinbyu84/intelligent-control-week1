import cv2
import numpy as np

# Membaca gambar dari file
image_path = 'rgb.png'
frame = cv2.imread(image_path)

if frame is None:
    print("Error: Could not read image.")
else:
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Rentang warna merah dalam HSV
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    
    # Rentang warna biru dalam HSV
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    
    # Rentang warna hijau dalam HSV
    lower_green = np.array([40, 40, 40])
    upper_green = np.array([70, 255, 255])
    mask_green = cv2.inRange(hsv, lower_green, upper_green)

    # Menggabungkan semua mask
    mask = mask_red | mask_blue | mask_green
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Menemukan kontur
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Menggambar bounding box di sekitar objek yang terdeteksi
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        
        # Menambahkan padding pada bounding box
        padding = 10
        x = max(x - padding, 0)
        y = max(y - padding, 0)
        w = min(w + 2 * padding, frame.shape[1] - x)
        h = min(h + 2 * padding, frame.shape[0] - y)
        
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Menentukan warna yang terdeteksi
        if cv2.inRange(hsv[y:y+h, x:x+w], lower_red, upper_red).any():
            color = "Red"
        elif cv2.inRange(hsv[y:y+h, x:x+w], lower_blue, upper_blue).any():
            color = "Blue"
        elif cv2.inRange(hsv[y:y+h, x:x+w], lower_green, upper_green).any():
            color = "Green"
        else:
            color = "Unknown"
        
        # Menambahkan teks pada bounding box
        cv2.putText(frame, color, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Menampilkan hasil
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
