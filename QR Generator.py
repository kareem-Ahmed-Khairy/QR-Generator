# Import required library
import qrcode
import os

def generate_qr(text: str, filename: str = "qr_code", 
                fill_color: str = "black", back_color: str = "white",
                save_dir: str = ".") -> str:
    """
    Generate a QR code from the given text and save it as a PNG image.

    Args:
        text (str): The data to encode into the QR code.
        filename (str): The output image name (without extension).
        fill_color (str): Color of the QR code.
        back_color (str): Background color of the QR code.
        save_dir (str): Directory to save the QR code.

    Returns:
        str: Path to the saved QR code image.
    """

    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR Code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Pixel size of each box
        border=4      # Thickness of the border
    )

    qr.add_data(text)
    qr.make(fit=True)

    image = qr.make_image(fill_color=fill_color, back_color=back_color)

    # Ensure filename is safe and has .png extension
    safe_filename = f"{filename.strip() or 'qr_code'}.png"

    # Ensure save directory exists
    os.makedirs(save_dir, exist_ok=True)

    # Full path
    save_path = os.path.join(save_dir, safe_filename)

    image.save(save_path)

    return os.path.abspath(save_path)


if __name__ == "__main__":
    data = input("Enter the URL or any data: ").strip()
    if not data:
        print("⚠️ No data entered. Exiting.")
    else:
        name = input("Enter the image name (default: qr_code): ").strip() or "qr_code"
        save_dir = input("Enter save directory (default: current folder): ").strip() or "."
        
        saved_path = generate_qr(data, name, save_dir=save_dir)
        print(f"✅ QR code saved at: {saved_path}")
