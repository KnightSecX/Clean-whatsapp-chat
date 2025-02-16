# Clean-whatsapp-chat
Because it purifies Exported chats like holy water!🫧💦 Slaying all unnecessary demons!👻

## 🚀 **Clean WhatsApp Chat – Remove Clutter Like a Pro!**

A Python script to clean WhatsApp exported chats by removing timestamps, sender names, numbers, media files, and unwanted clutter, leaving only the actual text messages.

# ✨ Features

✅ Removes timestamps, sender names & phone numbers

✅ Deletes media attachments & <Media omitted> messages

✅ Removes join/leave notifications, encryption alerts & pinned messages

✅ Deletes WhatsApp, YouTube, Facebook & ALL other links

✅ Keeps only the actual text messages, with proper formatting

## 📥 Step 1: Export a WhatsApp Chat
Follow these steps to export a WhatsApp chat as a .txt file:

1️⃣ Open WhatsApp and go to the chat you want to clean.

2️⃣ Tap the three dots in the top-right corner.

3️⃣ Select More > Export Chat.

4️⃣ Choose WITHOUT media (recommended).

5️⃣ Select Save to Files / Internal Storage / Google Drive (wherever you prefer).

_💡 Tip: If you choose "WITH media," the script will still remove media references._

## 📂 Step 2: Move & Rename the Chat File

1️⃣ Locate the exported chat file (usually named like WhatsApp Chat with XYZ.zip).

2️⃣ Extract text file from it & rename it to What.txt for simplicity.

3️⃣ Move it to: /storage/emulated/0/Movies/
You can use a file manager or Termux:

## ⚡ Step 3: Install & Run the Script in Termux

📌 Install Termux (If Not Installed)

Download Termux from [F-Droid](https://f-droid.org/en/packages/com.termux/)  (Recommended) or [Play Store](https://play.google.com/store/apps/details?id=com.termux).


### Install Git & Python


```
pkg update && pkg upgrade -y
pkg install python git -y
pip install rich
```

### Clone the Script from GitHub

```
cd $HOME
git clone https://github.com/KnightSecX/Clean-whatsapp-chat.git
cd Clean-whatsapp-chat
chmod +x clean_whatsapp_chat.py
```

### Run the Script

```
python clean_whatsapp_chat.py What.txt
```

### Add an Alias for Quick Use

```
echo 'alias cleanwhatsapp="python $HOME/Clean-whatsapp-chat/clean_whatsapp_chat.py"' >> ~/.bashrc
source ~/.bashrc
```

### Now you can clean WhatsApp chats with just:

```
cleanwhatsapp What.txt
```

## 📢 Want to Contribute?

⭐ Star this repo if you find it useful!

🛠 Improve the script & submit pull requests.

📢 Report bugs or suggest features in Issues.

### 🛡 FAQ

❓ What if I exported the chat WITH media?

_✅ No worries! The script will remove media filenames and messages automatically._

❓ Can I use this for WhatsApp Business?

_✅ Yes! The format is the same, so it works perfectly._

❓ What if I get an error while running the script?

### ✅ Make sure: 👇 

You have Python 3 installed 
```
(python --version)
```

The chat file is named What.txt and placed in /Movies/.

You typed the filename correctly in Termux.

---

## 📌 **Credits**

🛠 Developed by (@KnightSecX)

### 📜 Regex-powered chat cleaning with Python & Termux!
---
###🚀 Ready to Clean Your Chats?

**🔥 Clone & Run Now!**

Git clone [Script](https://github.com/KnightSecX/Clean-whatsapp-chat.git)

###🚀 No more clutter, just clean messages! 🎯
