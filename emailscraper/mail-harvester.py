import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import re


def extract_emails_from_text(text):
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(email_regex, text)

def scrape_emails_from_website():
    website_url = url_entry.get()
    response = requests.get(website_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.get_text()
        emails = extract_emails_from_text(text)
        unique_emails = set(emails)  # Remove duplicates if needed
        if unique_emails:
            with open('extracted_emails.txt', 'w') as file:
                for email in unique_emails:
                    file.write(email + '\n')
            messagebox.showinfo("Success", "Emails extracted successfully and saved in 'extracted_emails.txt'")
        else:
            messagebox.showinfo("No Emails", "No emails found on the provided website.")
    else:
        messagebox.showerror("Error", f"Failed to fetch content from {website_url}")


# Create main window
root = tk.Tk()
width=750
height=400
root.geometry(f"{width}x{height}")
root.title("")

#title label
title_label = tk.Label(root, text="Email Harvester", font=("Arial", 40, "bold"), bg="#f0f0f0")
title_label.pack(pady=5)

# URL input field
url_label = tk.Label(root, text="Enter website URL:", font=("Arial", 20), bg="#f0f0f0")
url_label.pack(pady=15, ipadx=5, ipady=10)
url_entry = tk.Entry(root, width=50, font=("Arial", 15))
url_entry.pack(pady=10, ipadx=10, ipady=5)

# Scrape button
scrape_button = tk.Button(root, text="Scrape Emails", command=scrape_emails_from_website, font=("Arial", 15), bg="green", fg="black", cursor="hand2")
scrape_button.pack(pady=10)

root.mainloop()
