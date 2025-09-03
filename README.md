# QR Code Generator

## Description
A simple Python application that generates **QR codes** from any text or URL and saves them as PNG images.  
You can customize the QR code with different colors, file names, and save locations.

## Features
- Generate a QR code from any **text or URL**.  
- Save QR code as a **PNG image**.  
- Customize:
  - **Filename**  
  - **Save directory**  
  - **Colors** (fill color and background color)  
- Handles invalid or empty input gracefully.  

## Requirements
- Python 3.x  
- [qrcode](https://pypi.org/project/qrcode/) library  

Install dependencies:
```bash
pip install qrcode[pil]
