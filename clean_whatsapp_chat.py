import re
import sys
import os
from rich import print  

# ✅ Default folder where WhatsApp exported chats are stored
default_folder = "/storage/emulated/0/Movies/"

# ✅ Ensure a filename is provided
if len(sys.argv) < 2:
    print("[bold red]❌ Usage:[/bold red] python clean_whatsapp_chat.py <filename>")
    sys.exit(1)

# ✅ Build the full file path
input_file = os.path.join(default_folder, sys.argv[1])

# ✅ Check if the file exists
if not os.path.exists(input_file):
    print(f"[bold red]❌ Error:[/bold red] File '{input_file}' not found!")
    sys.exit(1)

# ✅ Read the WhatsApp chat file
with open(input_file, "r", encoding="utf-8") as file:
    lines = file.readlines()

# ✅ Regex patterns to clean clutter
patterns = {
    "timestamp_sender": re.compile(r"^\d{2}/\d{2}/\d{2}, \d{2}:\d{2} - (?:[^:]+|(?:\+\d{1,3} \d{5,15})):\s*"),
    "media": re.compile(r".*\.(jpg|jpeg|png|gif|mp4|webp|pdf|vcf|opus|m4a|aac|wav|mp3|txt) file attached", re.UNICODE),
    "deleted": re.compile(r"This message was deleted"),
    "join_leave": re.compile(r".* joined using this group's invite link|.* left|.* added .*|.* removed .*"),
    "phone_change": re.compile(r".* changed their phone number to a new number.*"),
    "group_invite": re.compile(r"https:\/\/chat\.whatsapp\.com/.*"),
    "social_links": re.compile(r"https?:\/\/(www\.)?(facebook|youtube|youtu\.be|instagram|twitter|t\.co|linkedin|tiktok)\..*"),
    "any_links": re.compile(r"https?:\/\/\S+"),  # ✅ Removes ALL links (even unknown ones!)
    "encryption": re.compile(r"Messages and calls are end-to-end encrypted.*"),
    "self_encryption": re.compile(r"Messages to yourself are end-to-end encrypted.*"),
    "media_omitted": re.compile(r"<Media omitted>", re.IGNORECASE),
    "pinned_message": re.compile(r"You pinned a message")
}

# ✅ Logging Counters
total_messages = len(lines)
removed_messages = 0
removed_links = 0
removed_media = 0
removed_pinned_messages = 0

cleaned_messages = []

# **🔥 SINGLE LOOP: CLEAN EVERYTHING FAST!**
for line in lines:
    line = line.strip()

    # ✅ Remove timestamps & sender info
    line = patterns["timestamp_sender"].sub("", line)

    # ✅ Check if line matches clutter patterns
    if any(pattern.search(line) for pattern in patterns.values()):
        removed_messages += 1
        if patterns["media"].search(line):
            removed_media += 1
        elif patterns["group_invite"].search(line) or patterns["social_links"].search(line) or patterns["any_links"].search(line):
            removed_links += 1
        elif patterns["pinned_message"].search(line):
            removed_pinned_messages += 1
        continue  # Skip this line

    # ✅ **No extra blank lines – keep only valid messages**
    cleaned_messages.append(line)

# ✅ Define output file name
output_file = os.path.join(default_folder, f"Cleaned_{sys.argv[1]}")

# ✅ Save the cleaned chat
with open(output_file, "w", encoding="utf-8") as output:
    output.write("\n".join(cleaned_messages) + "\n")  # Ensure proper newline at the end

# ✅ **📌 Print Colorful Stats**
print(f"[bold green]✅ Cleaning Complete![/bold green] Saved as '[bold cyan]{output_file}[/bold cyan]'")
print("[bold blue]📊 Stats:[/bold blue]")
print(f"   🔹 [yellow]Total Messages Processed:[/yellow] {total_messages}")
print(f"   ❌ [red]Removed Messages:[/red] {removed_messages}")
print(f"   🔗 [cyan]Links Removed:[/cyan] {removed_links}")
print(f"   🖼️ [magenta]Media Messages Removed:[/magenta] {removed_media}")
print(f"   📌 [purple]Pinned Messages Removed:[/purple] {removed_pinned_messages}")
print(f"   ✔️ [bold green]Final Cleaned Messages:[/bold green] {len(cleaned_messages)}")

# ✅ **Auto-Open Cleaned File 📂**
os.system(f"xdg-open '{output_file}'")
