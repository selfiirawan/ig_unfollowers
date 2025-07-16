# Instagram Unfollowers Scanner

A Python tool that helps you find out which Instagram accounts are not following you back by analyzing your exported HTML data from Instagram.

---

## 📌 What It Does

This script compares your "Following" and "Followers" lists (from your Instagram data export) to detect users you follow who don’t follow you back.

---

## ✅ How to Use

### 1. Export Your Instagram Data
1. Log in to Instagram **on a browser**.
2. Go to:  
   `More > Settings > Meta Account Center > See more in Account Center `
3. Once redirected to the **Accounts Center**, select:
   - `Your Information and Permissions` > `Download your informations` > `Download or transfer informations`
   - Select your account
   - Go to `Some of your information > Followers & Following` > `Next`
   - Select `Download to device`, let the format in HTML
   - Choose a date range (recommend: **All time**) > `Create files`
4. Wait for the email from Instagram (may take a few hours).
5. Download and unzip the file.

### 2. Prepare the HTML Files
- Locate `followers.html` and `followings.html` in the unzipped folder.
- Copy both files into this project folder.

### 3. Run the Script
Make sure you have Python 3 installed, then run:

```bash
python3 main.py -i followings.html -e followers.html 
```
---

## 📂  Required File 
- `followings.html`
- `followers.html`

---

## ⚙️ Requirements
- Python 3.x
> No external libraries required.

---

## 🙏 Acknowledgement

This project was originally inspired by [kk10128/igFollowers](https://github.com/kk10128/igFollowers.git).  
Significant changes and improvements have been made to fit my own use case.
