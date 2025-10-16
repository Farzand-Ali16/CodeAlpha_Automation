import os
import shutil
def move_jpg_files(source_folder, destination_folder):
    os.makedirs(destination_folder, exist_ok=True)
    count = 0
    for filename in os.listdir(source_folder):
        if filename.lower().endswith(".jpg"):
            source_path = os.path.join(source_folder, filename)
            dest_path = os.path.join(destination_folder, filename)
            shutil.move(source_path, dest_path)
            count += 1
    print(f"{count} .jpg files moved to '{destination_folder}' successfully")
if __name__ == "__main__":
    src = input("Enter source folder path: ").strip()
    dst = input("Enter destination folder path: ").strip()
    move_jpg_files(src, dst)
import re
def extract_emails(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()
    emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
    with open(output_file, "w", encoding="utf-8") as f:
        for email in sorted(set(emails)):
            f.write(email + "\n")
    print(f"✅ {len(set(emails))} email addresses extracted and saved to '{output_file}'.")
if __name__ == "__main__":
    in_file = input("Enter input .txt file path: ").strip()
    out_file = input("Enter output file name (e.g., emails.txt): ").strip()
    extract_emails(in_file, out_file)
import requests
from bs4 import BeautifulSoup
def scrape_title(url, output_file):
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.title.string.strip() if soup.title else "No title found"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(f"Page Title: {title}\n")
        print(f"✅ Title extracted and saved to '{output_file}'.")
if __name__ == "__main__":
    site_url = input("Enter webpage URL: ").strip()
    file_name = input("Enter output file name (e.g., title.txt): ").strip()
    scrape_title(site_url, file_name)

