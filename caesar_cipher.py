import streamlit as st
from streamlit_lottie import st_lottie

# Fungsi untuk melakukan Caesar Cipher
def caesar_cipher(text, shift, alphabet):
    encrypted_text = ""
    for char in text:
        if char in alphabet:
            idx = alphabet.index(char)
            new_idx = (idx + shift) % len(alphabet)
            encrypted_text += alphabet[new_idx]
        else:
            encrypted_text += char
    return encrypted_text

st.set_page_config(page_title="Caesar Cipher Calculator", page_icon=":closed_lock_with_key:")

# Set the background color
st.markdown(
    """
    <style>
    .reportview-container {
        background-color: #F5F5F5
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Tampilkan judul sebagai markdown
st.markdown("<h1 style='text-align: center;'>Caesar Cipher Calculator</h1>", unsafe_allow_html=True)

# Fungsi dropdown buat pilih jenis alfabet
st.header("Pilih jenis alfabet")
tipe_alfabet = st.selectbox("Pilih jenis alfabet", ["English alphabet (A-Z)", "English alphabet and digits (A-Z, 0-9)"])

# Buat perulangan untuk atur alfabet berdasarkan jenis alfabet yang dipilih 
if tipe_alfabet == "English alphabet (A-Z)":
    alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
else:
    alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

# Encryption section
st.header("Caesar Cipher Encoder")
encrypt_text = st.text_input("Caesar Code plain text")
encrypt_shift = st.number_input("Enter the encrypt shift value", min_value=0, step=1)
if st.button("Enkripsi"):
    encrypted_text = ""
    for char in encrypt_text:
        if char.isalpha():
            if char.isupper():
                encrypted_text += alfabet[(alfabet.index(char) + encrypt_shift) % len(alfabet)].upper()
            else:
                encrypted_text += alfabet[(alfabet.index(char) + encrypt_shift) % len(alfabet)].lower()
        elif char.isdigit():
            encrypted_text += str((int(char) + encrypt_shift) % 10)
        else:
            encrypted_text += char
    st.write("Encrypted message: ", encrypted_text)

# Decryption section
st.header("Caesar Cipher Decoder")
decrypt_text = st.text_input("Caesar Code cipher text")
decrypt_shift = st.number_input("Enter the decrypt shift value", min_value=0, step=1)
if st.button("Dekripsi"):
    decrypted_text = ""
    for char in decrypt_text:
        if char.isalpha():
            if char.isupper():
                decrypted_text += alfabet[(alfabet.index(char) - decrypt_shift) % len(alfabet)].upper()
            else:
                decrypted_text += alfabet[(alfabet.index(char) - decrypt_shift) % len(alfabet)].lower()
        elif char.isdigit():
            decrypted_text += str((int(char) - decrypt_shift) % 10)
        else:
            decrypted_text += char
    st.write("Decrypted message: ", decrypted_text)

# Add a watermark to the app
st.markdown(
    """
    <div style='position: fixed; bottom: 10px; right: 10px; color: black;'>Created by Ilham Rafiedhia Pramutighna</div>
    """,
    unsafe_allow_html=True
)