
import cv2
from pyzbar.pyzbar import decode
import tkinter as tk
from tkinter import messagebox
import webbrowser

# Function to open the URL in a web browser
def open_link(content):
    if content.startswith("http://") or content.startswith("https://"):
        webbrowser.open(content)
    else:
        messagebox.showinfo("Scanned Data", content)

# Function to start the QR code scanning
def scan_qr_code():
    cap = cv2.VideoCapture(0)  # Open the device's camera
    while True:
        _, frame = cap.read()
        for barcode in decode(frame):
            content = barcode.data.decode("utf-8")
            cv2.putText(frame, content, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cap.release()
            cv2.destroyAllWindows()
            open_link(content)
            return
        
        cv2.imshow("QR Code Scanner", frame)
        
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    
    cap.release()
    cv2.destroyAllWindows()

# Initialize the main window
root = tk.Tk()
root.title("QR Code Scanner")

# Create a button to start scanning
scan_button = tk.Button(root, text="Scan QR Code", font=("Arial", 20), command=scan_qr_code)
scan_button.pack(pady=20)

# Run the application
root.mainloop()


