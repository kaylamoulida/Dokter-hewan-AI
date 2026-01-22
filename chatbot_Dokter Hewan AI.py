# vet_chatbot.py
# Chatbot sederhana berperan sebagai dokter hewan


def bot_reply(user_text: str) -> str:
    text = user_text.lower()

    if "makan" in text or "diet" in text or "pakan" in text:
        return "Pastikan hewan mendapat makanan sesuai jenisnya. Hindari cokelat, bawang, dan anggur."
    elif "vaksin" in text or "imun" in text:
        return "Vaksinasi penting untuk mencegah penyakit. Konsultasikan jadwal vaksin ke klinik hewan."
    elif "muntah" in text or "diare" in text:
        return "Jika gejala ringan, pantau 24 jam. Jika berlanjut atau parah, segera ke dokter hewan."
    elif "kejang" in text or "sulit bernapas" in text or "darurat" in text:
        return "⚠️ Ini kondisi darurat! Segera bawa ke klinik atau rumah sakit hewan terdekat."
    else:
        return "Saya bisa bantu dengan info umum. Jelaskan spesies, usia, dan gejala agar lebih tepat."

def main():
    print("🐾 VetChat — Dokter Hewan AI")
    print("Ketik 'exit' untuk keluar.\n")

    while True:
        user_input = input("Anda: ")
        if user_input.lower() == "exit":
            print("VetChat: Terima kasih, semoga hewan peliharaan sehat selalu!")
            break

        reply = bot_reply(user_input)
        print("VetChat:", reply)

if __name__ == "__main__":
    main()
