import tkinter as tk
from tkinter import filedialog, messagebox
import os
import base64
import re

# Constants
COUNT_FILE = ".hidden_usage_data"  # Hidden file with an ambiguous name
MAX_USES = 10  # Set the maximum number of uses allowed

# Read the current usage count
def read_count():
    if os.path.exists(COUNT_FILE):
        with open(COUNT_FILE, 'rb') as file:
            count_data = file.read()
            count = int(base64.b64decode(count_data).decode('utf-8'))
    else:
        count = 0
    return count

# Write the updated usage count
def write_count(count):
    with open(COUNT_FILE, 'wb') as file:
        count_data = base64.b64encode(str(count).encode('utf-8'))
        file.write(count_data)

def clean_phone_number(phone):
    digits = re.sub(r'\D', '', phone)  # Remove all non-digit characters
    return f"+1{digits}" if len(digits) == 10 else digits


def generate_html():
    count = read_count()
    print(f"Current count: {count}")  # Debug statement
    if count >= MAX_USES:
        messagebox.showwarning("Usage Limit Reached", "The maximum number of signatures has been generated. Contact the creator to receive more tokens.")
        return

    name = name_entry.get()
    title = title_entry.get()
    phone = phone_entry.get()
    cleaned_phone = clean_phone_number(phone)

    email = email_entry.get()
    photo_url = photo_url_entry.get()
    linkedin = linkedin_entry.get()

    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <style type="text/css">
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600&display=swap');
    a {{ text-decoration: none !important; color: inherit; }}
    table, tr, td, a, span {{ font-family: 'Montserrat', Arimo, Helvetica, Arial, sans-serif; }}
    img {{ display: block; }}
  </style>
</head>
<body>
  <table width="100%" border="0" cellspacing="0" cellpadding="0" style="max-width: 500px;">
    <tr>
      <td style="padding-bottom: 12px;">
        <table border="0" cellspacing="0" cellpadding="0" style="width: 100%;">
          <tr>
            <td valign="middle" style="padding-right: 8px; border-right: 2px solid #312d2d;">
              <img src="{photo_url}" alt="Photo" style="height: 120px; width: 120px; border-radius: 50%;">
            </td>
            <td valign="middle" style="padding: 0 5px; border-right: 2px solid #312d2d;">
              <table border="0" cellspacing="0" cellpadding="4">
                <tr>
                  <td>
                    <p style="margin: 0;">
                      <span style="font-size: 10.5pt; font-weight: bold; color: #006400;">{name} |</span>
                      <span style="font-size: 10.5pt; color: #000;">{title}</span>
                    </p>
                    <p style="margin: 0;">
                      <span style="font-size: 10.2pt; font-weight: bold; color: #000;">CONSOLIDATED MOSQUITO ABATEMENT DISTRICT</span>
                    </p>
                  </td>
                </tr>
                <tr>
                  <td style="padding-top: 6px;">
                    <table cellspacing="0" cellpadding="0" style="line-height: 1;">
                      <tr>
                        <td><img src="https://cdn-icons-png.flaticon.com/512/16076/16076069.png" width="13" height="13"></td>
                        <td style="width: 6px;"></td>
                        <td><a href="tel:{cleaned_phone}"><span style="font-size: 9pt; color: #000; font-weight: bold;">{phone}</span></a></td>
                      </tr>
                      <tr>
                        <td><img src="https://cdn-icons-png.flaticon.com/512/2965/2965306.png" width="13" height="13"></td>
                        <td style="width: 6px;"></td>
                        <td><a href="mailto:{email}"><span style="font-size: 9pt; color: #000; font-weight: bold;">{email}</span></a></td>
                      </tr>
                      <tr>
                        <td><img src="https://cdn-icons-png.flaticon.com/512/3991/3991775.png" width="13" height="13"></td>
                        <td style="width: 6px;"></td>
                        <td><a href="{linkedin}"><span style="font-size: 9pt; color: #000; font-weight: bold;">LinkedIn</span></a></td>
                      </tr>
                    </table>
                  </td>
                </tr>
              </table>
            </td>
            <td valign="middle" style="padding-left: 8px;">
              <img src="https://green-personal-roundworm-409.mypinata.cloud/ipfs/bafkreiffnenvfbuczumm3qnnqt2mwbcrjjzmmtz37uzf2qvmy4owrkfvg4" alt="Logo" style="height: 120px; width: auto;">
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>

  <!-- Social Section -->
  <table width="100%" cellpadding="0" cellspacing="0" style="max-width: 500px; background-color: #312d2d; border-radius: 4px;">
    <tr>
      <td align="center" style="padding: 2px 0 6px 0;">
        <span style="font-size: 14pt; font-weight: 600; color: #ffffff;">Follow Our Updates</span>
      </td>
    </tr>
    <tr>
      <td align="center" style="padding-bottom: 10px;">
        <table border="0" cellspacing="0" cellpadding="0">
          <tr>
            <td style="padding: 0 20px;"><a href="https://facebook.com/ConsolidatedMAD" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/145/145802.png" width="20" height="20"></a></td>
            <td style="padding: 0 20px;"><a href="https://instagram.com/consolidatedmad/" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/2111/2111463.png" width="20" height="20"></a></td>
            <td style="padding: 0 20px;"><a href="https://mosquitobuzz.net" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/841/841364.png" width="20" height="20"></a></td>
            <td style="padding: 0 20px;"><a href="https://www.youtube.com/channel/UCl76HEaHxK0h_z8IHuDSvtA" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/1384/1384060.png" width="20" height="20"></a></td>
            <td style="padding: 0 20px;"><a href="https://x.com/ConsolidatedMAD" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/145/145812.png" width="20" height="20"></a></td>
          </tr>
        </table>
      </td>
    </tr>
  </table>

  <!-- Disclaimer -->
  <table width="100%" cellpadding="0" cellspacing="0" style="max-width: 500px;">
    <tr>
      <td style="padding-top: 10px; font-size: 10.4px; color: #737373; line-height: 1.4; text-align: justify;">
        The content of this email is intended for the person or entity to which it is addressed only. This email may contain confidential information. If you are not the person to whom this message is addressed, be aware that any use, reproduction, or distribution of this message is strictly prohibited. If you received this in error, please contact the sender and immediately delete this email and any attachments.
      </td>
    </tr>
  </table>
</body>
</html>

"""

    file_path = filedialog.asksaveasfilename(defaultextension=".html", filetypes=[("HTML files", "*.html"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(html_content)
        count += 1
        write_count(count)
        print(f"File saved to {file_path}. Remaining uses: {MAX_USES - count}")

# Create the main application window
root = tk.Tk()
root.title("HTML Signature Generator")

# Set window size and center it
root.geometry("400x300")
root.eval('tk::PlaceWindow . center')

# Create and place the input fields
tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=5, sticky='e')
name_entry = tk.Entry(root, width=45)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Title").grid(row=1, column=0, padx=10, pady=5, sticky='e')
title_entry = tk.Entry(root, width=45)
title_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Phone").grid(row=2, column=0, padx=10, pady=5, sticky='e')
phone_entry = tk.Entry(root, width=45)
phone_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Email").grid(row=3, column=0, padx=10, pady=5, sticky='e')
email_entry = tk.Entry(root, width=45)
email_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Photo URL").grid(row=4, column=0, padx=10, pady=5, sticky='e')
photo_url_entry = tk.Entry(root, width=45)
photo_url_entry.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="LinkedIn URL").grid(row=5, column=0, padx=10, pady=5, sticky='e')
linkedin_entry = tk.Entry(root, width=45)
linkedin_entry.grid(row=5, column=1, padx=10, pady=5)

# Download button
generate_button = tk.Button(
    root,
    text="Download Signature Block",
    bg="#006400", fg="white",
    font=("Arial", 10, "bold"),
    padx=10, pady=4,
    command=generate_html
)
generate_button.grid(row=6, columnspan=2, pady=10)

# Footer
tk.Label(root, text="Developed by Salman Sakib © 2025", font=("Helvetica", 10)).grid(row=7, columnspan=2, pady=10)

# Run the main event loop
root.mainloop()
