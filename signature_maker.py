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
  <!--[if mso]>
  <xml>
    <o:OfficeDocumentSettings>
      <o:AllowPNG/>
      <o:PixelsPerInch>96</o:PixelsPerInch>
    </o:OfficeDocumentSettings>
  </xml>
  <![endif]-->
  <style type="text/css">
    /* Outlook-safe styles */
    table, tr, td, a, span {{ font-family: Arial, Helvetica, sans-serif !important; }}
    a {{ text-decoration: none !important; color: inherit !important; }}
    img {{ display: block; border: 0; outline: none; }}
    table {{ border-collapse: collapse; mso-table-lspace: 0pt; mso-table-rspace: 0pt; }}
    
    /* Hide border-radius in Outlook */
    .outlook-round {{ border-radius: 50%; }}
    
    /*[if mso]*/
    .outlook-round {{ border-radius: 0 !important; }}
    /*[endif]*/
  </style>
</head>
<body style="margin: 0; padding: 0;">
  <!--[if mso | IE]>
  <table role="presentation" border="0" cellpadding="0" cellspacing="0" width="500">
  <tr>
  <td>
  <![endif]-->
  
  <table role="presentation" width="500" border="0" cellspacing="0" cellpadding="0" style="width: 500px; margin: 0; padding: 0;">
    <tr>
      <td style="padding: 0 0 12px 0;">
        <table role="presentation" border="0" cellspacing="0" cellpadding="0" width="500" style="width: 500px;">
          <tr>
            <td valign="top" width="128" style="width: 128px; padding-right: 8px; border-right: 2px solid #312d2d;">
              <img src="{photo_url}" alt="Photo" width="120" height="120" style="width: 120px; height: 120px; border-radius: 50%; display: block;">
            </td>
            <td valign="top" width="240" style="width: 240px; padding: 0 8px; border-right: 2px solid #312d2d;">
              <table role="presentation" border="0" cellspacing="0" cellpadding="0" width="240" style="width: 240px;">
                <tr>
                  <td style="padding: 4px 0;">
                    <div style="margin: 0; padding: 0; line-height: 1.2;">
                      <span style="font-size: 11pt; font-weight: bold; color: #006400; font-family: Arial, Helvetica, sans-serif;">{name} | </span><span style="font-size: 11pt; color: #000; font-family: Arial, Helvetica, sans-serif;">{title}</span>
                    </div>
                    <div style="margin: 2px 0 0 0; padding: 0; line-height: 1.2;">
                      <span style="font-size: 10pt; font-weight: bold; color: #000; font-family: Arial, Helvetica, sans-serif;">CONSOLIDATED MOSQUITO ABATEMENT DISTRICT</span>
                    </div>
                  </td>
                </tr>
                <tr>
                  <td style="padding-top: 8px;">
                    <table role="presentation" cellspacing="0" cellpadding="2" border="0">
                      <tr>
                        <td width="15" style="width: 15px;"><img src="https://cdn-icons-png.flaticon.com/512/16076/16076069.png" width="13" height="13" style="width: 13px; height: 13px; display: block;"></td>
                        <td width="4" style="width: 4px;">&nbsp;</td>
                        <td><a href="tel:{cleaned_phone}" style="text-decoration: none; color: #000;"><span style="font-size: 9pt; color: #000; font-weight: bold; font-family: Arial, Helvetica, sans-serif;">{phone}</span></a></td>
                      </tr>
                      <tr>
                        <td width="15" style="width: 15px;"><img src="https://cdn-icons-png.flaticon.com/512/2965/2965306.png" width="13" height="13" style="width: 13px; height: 13px; display: block;"></td>
                        <td width="4" style="width: 4px;">&nbsp;</td>
                        <td><a href="mailto:{email}" style="text-decoration: none; color: #000;"><span style="font-size: 9pt; color: #000; font-weight: bold; font-family: Arial, Helvetica, sans-serif;">{email}</span></a></td>
                      </tr>
                      <tr>
                        <td width="15" style="width: 15px;"><img src="https://cdn-icons-png.flaticon.com/512/3991/3991775.png" width="13" height="13" style="width: 13px; height: 13px; display: block;"></td>
                        <td width="4" style="width: 4px;">&nbsp;</td>
                        <td><a href="{linkedin}" target="_blank" style="text-decoration: none; color: #000;"><span style="font-size: 9pt; color: #000; font-weight: bold; font-family: Arial, Helvetica, sans-serif;">LinkedIn</span></a></td>
                      </tr>
                    </table>
                  </td>
                </tr>
              </table>
            </td>
            <td valign="top" width="124" style="width: 124px; padding-left: 8px;">
              <img src="https://green-personal-roundworm-409.mypinata.cloud/ipfs/bafkreiffnenvfbuczumm3qnnqt2mwbcrjjzmmtz37uzf2qvmy4owrkfvg4" alt="Logo" width="120" height="120" style="width: 120px; height: 120px; display: block;">
            </td>
          </tr>
        </table>
      </td>
    </tr>
  </table>

  <!-- Social Section -->
  <table role="presentation" width="500" cellpadding="0" cellspacing="0" border="0" style="width: 500px; background-color: #312d2d;">
    <tr>
      <td align="center" style="padding: 8px 0 6px 0;">
        <span style="font-size: 14pt; font-weight: bold; color: #ffffff; font-family: Arial, Helvetica, sans-serif;">Follow Our Updates</span>
      </td>
    </tr>
    <tr>
      <td align="center" style="padding: 0 0 10px 0;">
        <table role="presentation" border="0" cellspacing="0" cellpadding="0">
          <tr>
            <td style="padding: 0 10px;"><a href="https://facebook.com/ConsolidatedMAD" target="_blank" style="text-decoration: none;"><img src="https://cdn-icons-png.flaticon.com/512/145/145802.png" width="20" height="20" style="width: 20px; height: 20px; display: block;"></a></td>
            <td style="padding: 0 10px;"><a href="https://instagram.com/consolidatedmad/" target="_blank" style="text-decoration: none;"><img src="https://cdn-icons-png.flaticon.com/512/2111/2111463.png" width="20" height="20" style="width: 20px; height: 20px; display: block;"></a></td>
            <td style="padding: 0 10px;"><a href="https://consolidatedmadca.gov" target="_blank" style="text-decoration: none;"><img src="https://cdn-icons-png.flaticon.com/512/841/841364.png" width="20" height="20" style="width: 20px; height: 20px; display: block;"></a></td>
            <td style="padding: 0 10px;"><a href="https://www.youtube.com/channel/UCl76HEaHxK0h_z8IHuDSvtA" target="_blank" style="text-decoration: none;"><img src="https://cdn-icons-png.flaticon.com/512/1384/1384060.png" width="20" height="20" style="width: 20px; height: 20px; display: block;"></a></td>
            <td style="padding: 0 10px;"><a href="https://x.com/ConsolidatedMAD" target="_blank" style="text-decoration: none;"><img src="https://cdn-icons-png.flaticon.com/512/145/145812.png" width="20" height="20" style="width: 20px; height: 20px; display: block;"></a></td>
          </tr>
        </table>
      </td>
    </tr>
  </table>

  <!-- Disclaimer -->
  <table role="presentation" width="500" cellpadding="0" cellspacing="0" border="0" style="width: 500px;">
    <tr>
      <td style="padding: 10px 0 0 0; font-size: 8pt; color: #737373; line-height: 1.3; font-family: Arial, Helvetica, sans-serif;">
        The content of this email is intended for the person or entity to which it is addressed only. This email may contain confidential information. If you are not the person to whom this message is addressed, be aware that any use, reproduction, or distribution of this message is strictly prohibited. If you received this in error, please contact the sender and immediately delete this email and any attachments.
      </td>
    </tr>
  </table>

  <!--[if mso | IE]>
  </td>
  </tr>
  </table>
  <![endif]-->
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
