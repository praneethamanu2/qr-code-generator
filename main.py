import qrcode
import argparse
import os

def generate_qr(url, output_dir="qr_codes"):
    os.makedirs(output_dir, exist_ok=True)
    img = qrcode.make(url)
    output_path = os.path.join(output_dir, "qrcode.png")
    img.save(output_path)
    print(f"✅ QR code generated and saved at: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="QR Code Generator")
    parser.add_argument("--url", type=str, default="https://github.com/kaw393939", help="URL to encode as QR code")
    args = parser.parse_args()
    generate_qr(args.url)

