import streamlit as st
from streamlit_lottie import st_lottie
import requests
import json

def caesar_cipher(text, shift, alfabet):
    result = ""
    n = len(alfabet)

    for i in range(len(text)):
        char = text[i]

        # perulangan untuk menemukan indeks karakter dalam alfabet
        if char in alfabet:
            index = alfabet.index(char)
        else:
            result += char
            continue

        # geser index sesuai dengan jumlah pergeseran
        shifted_index = (index + shift) % n

        # tambahkan karakter yang digeser ke hasil
        shifted_char = alfabet[shifted_index]
        result += shifted_char

    return result
# st.set_page_config(page_title="Caesar Cipher Calculator", page_icon=":closed_lock_with_key:")

st.title("Caesar Cipher Calculator")

# Load animasi Lottie
def load_lottie_url(url:str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url = "https://assets1.lottiefiles.com/packages/lf20_480AU4.json"
lottie_json = load_lottie_url(lottie_url)

# Display animasi Lottie
if lottie_json is not None:
    st_lottie(lottie_json)
else:
    st.error("Error loading Lottie animation.")

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

# Fungsi dropdown buat pilih jenis alfabet
st.header("Pilih jenis alfabet")
tipe_alfabet = st.selectbox("Pilih jenis alfabet", ["English alphabet (A-Z)", "English alphabet and digits (A-Z, 0-9)", "Custom alphabet (A-Z, 0-9 chars only)"])

# Buat perulangan untuk atur alfabet berdasarkan jenis alfabet yang dipilih 
if tipe_alfabet == "English alphabet (A-Z)":
    alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
elif tipe_alfabet == "English alphabet and digits (A-Z, 0-9)":
    alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
else:
    alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    st.write("Note: Only characters A-Z and 0-9 will be included in the custom alphabet.")

# Encryption section
st.header("Caesar Cipher Encoder")
encrypt_text = st.text_input("Caesar Code plain text")
encrypt_shift = st.number_input("Enter the encrypt shift value", min_value=0, step=1)
if st.button("Enkripsi"):
    encrypted_text = caesar_cipher(encrypt_text, encrypt_shift, alfabet)
    st.write("Encrypted message: ", encrypted_text)

# buat space sedikit biar rapi
st.write("")

# Decryption section
st.header("Caesar Cipher Decoder")
decrypt_text = st.text_input("Caesar shifted ciphertext")
decrypt_shift = st.number_input("Enter the decrypt shift value", min_value=0, step=1)
if st.button("Dekripsi"):
    decrypted_text = caesar_cipher(decrypt_text, -decrypt_shift, alfabet)
    st.write("Decrypted message: ", decrypted_text)

# # Add some space between sections
# st.write("")
# st.write("")
# st.write("")

# # Automatic encryption/decryption section
# st.header("Automatic encryption/decryption")
# col5, col6 = st.columns(2)
# with col5:
#     text = st.text_input("Enter the text to encrypt/decrypt")
# with col6:
#     shift = st.number_input("Enter the shift value", min_value=0, step=1)
#     if st.button("Encrypt"):
#         encrypted_text = caesar_cipher(text, shift, alphabet)
#         st.write("Encrypted message: ", encrypted_text)
#     if st.button("Decrypt"):
#         decrypted_text = caesar_cipher(text, -shift, alphabet)
#         st.write("Decrypted message: ", decrypted_text)



# Add a watermark to the app
st.markdown(
    """
    <div style='position: fixed; bottom: 10px; right: 10px; color: black;'>Created by Ilham Rafiedhia Pramutighna</div>
    """,
    unsafe_allow_html=True
)