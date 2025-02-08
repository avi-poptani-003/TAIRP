import cv2
import numpy as np

# Step 2: Capture an image using a webcam or load an existing image
image_path = input("Enter the path of the image: ")
image = cv2.imread(image_path)  # Load an existing image

# Step 3: Apply image processing to enhance document visibility
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(blurred, 30, 150)

# Step 4: Detect document edges using techniques like Canny edge detection
contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:1]

for contour in contours:
    peri = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.02 * peri, True)
    cv2.drawContours(image, [approx], -1, (0, 255, 0), 2)

# Step 5: Save the scanned document as an image or PDF file
cv2.imwrite('scanned_document.jpg', image)  # Save the scanned document as an image

cv2.imshow('Scanned Document', image)
cv2.waitKey(2000)  # Display for 2 seconds
cv2.destroyAllWindows()