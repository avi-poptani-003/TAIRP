# Python Projects

This repository contains two Python projects:

1. **Task 1: Credit Card Validator**
2. **Task 2: Location Finder**

Each task is implemented using Python and follows best practices.

---

## **Task 1: Credit Card Validator**
### **Description**
This Python script validates credit card numbers using the **Luhn Algorithm**. The user can enter a credit card number, and the script will determine if it's valid.

### **How It Works**
1. Accepts user input for a credit card number.
2. Removes any non-numeric characters.
3. Implements the **Luhn Algorithm**:
   - Doubles every second digit from the right.
   - If the result is greater than 9, subtracts 9.
   - Sums all digits and checks if divisible by 10.
4. Returns **True** if the card is valid, otherwise **False**.

### **Installation**
No additional libraries are required. Just run the script.

### **Usage**
Run the script and enter a credit card number:
```sh
python credit_card_validator.py
```
Example:
```
Enter your credit card number: 4539 1488 0343 6467
✅ The credit card number is VALID!
```

---

## **Task 2: Location Finder**
### **Description**
This Python script allows users to input a location and get its **latitude and longitude** using **Geopy** and **Tkinter**. It also displays the location on an interactive map.

### **How It Works**
1. User enters a location in the **Tkinter GUI**.
2. **Geopy API** converts the location to latitude & longitude.
3. **TkinterMapView** displays the location on a map.
4. Handles errors if the location is not found.

### **Installation**
Install the required dependencies:
```sh
pip install geopy tkintermapview
```

### **Usage**
Run the script:
```sh
python location_finder.py
```
Enter a location and click **Find Location**. Example:
```
Input: Eiffel Tower
Output: Latitude: 48.8588443, Longitude: 2.2943506
```
The map will display the location.

---
## **Task 3: Document Scanner**
### **Description**
This Python script scans a document by detecting its edges using **OpenCV** and saves the processed image.

### **How It Works**
1. The user provides an image file path.
2. The image is converted to grayscale for better processing.
3. **Gaussian Blur** is applied to remove noise.
4. **Canny Edge Detection** finds document edges.
5. The largest contour (document outline) is detected and highlighted.
6. The processed image is saved as `scanned_document.jpg`.

### **Installation**
Ensure you have OpenCV and NumPy installed:
```sh
pip install opencv-python numpy