import streamlit as st
import string
from PIL import Image

# ------------- MAIN PAGE -----------------
def main_page():
    pic1 = Image.open('p1.png')
    pic2 = Image.open('p2.png')

    st.title("Apa itu Cybersecurity?")
    st.write('''
    **Cyber** adalah awalan yang dipakai untuk hampir segala sesuatu yang melibatkan komunikasi lewat komputer. 
    **Cyber space** adalah tempat maya dimana komunikasi terjadi.''')
    st.write("***Cyber space*** ❌ ***Cyber crime***")
    st.write('''***Cyber security*** merupakan sebuah proses perlindungan program, data, sistem, maupun
    jaringan dari ancaman atau serangan digital.''')
    st.write("")

    # Center content, create 3 columns, use 2nd column
    col1, col2, col3 = st.columns(3)
    with col2:
        st.metric(label="Pengguna internet di Indonesia", value="82 juta", delta="peringkat 8 dunia")
      
    st.title("")
    st.title("")
    st.title("Kelemahan Cybersecurity di Indonesia")
    st.image(pic1)
    st.title("")
    st.image(pic2)

# --------------- SECOND PAGE --------------------
def page2():
    st.title("Perlindungan Cybersecurity")
    st.title("")
    st.subheader("Mekanisme yang dilakukan untuk perlindungan")
    st.write("• **Confidentiality** -> gangguan kerahasiaan")
    st.write("• **Integrity** -> integritas")
    st.write("• **Availability** -> ketersediaan informasi")

    st.title("")
    st.subheader("Permasalahan terkait dengan pembangunan Cybersecurity")
    st.write("1. Lemahnya pemahaman penyelenggara negara atan security terkait dengan dunia cyber yang memerlukan pembatasan pengunaan layanan yang servernya berada di luar negeri dan diperlukan adanya pengunaan secured system")
    st.write("2. Legalitas penanganan penyerangan di dunia cyber.")
    st.write("3. Pola kejadian cyber crime sangat cepat sehingga sulit ditangani.")
    st.write("4. Tata kelola kelembagaan cyber-security nasional.")
    st.write("5. Rendahnya awareness atau kesadaran akan adanya ancaman cyber attack internasional yang dapat melumpuhkan infrastruktur vital suatu negara.")
    st.write("6. Masih lemahnya industri kita dalam memproduksi dan mengembangkan perangkat keras atau hardware terkait dengan teknologi informasi yang merupakan celah yang dapat memperkuat maupun memperlemah pertahanan dalam dunia cyber.")
    

# ------------- CIPHER PAGE -----------------
def cipher_page():
    st.title('Enkripsi pesanmu')

    # Expand message
    with st.expander('Tentang Caesar Cipher'):
        st.write('**Caesar Cipher** adalah algoritma kriptografi klasik yang dahulu digunakan oleh Julius Caesar untuk mengirimkan pesan rahasia atau taktik militer. Salah satu teknik enkripsi paling sederhana dan paling terkenal. Sandi ini menggeser alfabet ke kanan atau ke kiri dengan kunci/angka tertentu')
    
    # Widgets
    st.title('')
    phrase = st.text_area("Masukkan pesan")
    shift_direction = st.selectbox("Arah Geser: ", ('Kanan', 'Kiri'))
    shift_amount = st.number_input("Angka Kunci: ", min_value = 1)

    # Creating dictionary
    st.cache()
    def create_dict():
        letter_to_no = {}
        no_to_letter = {}

        for no, letter in enumerate(string.ascii_lowercase):
            letter_to_no[letter] = no
            no_to_letter[no] = letter
    
        return letter_to_no, no_to_letter

    letter_to_no, no_to_letter = create_dict()

    # Shifting 
    st.cache()
    def shift(phrase, shift_direction, shift_amount):
        answer = ''
    
        for i in phrase:
            #Returns True if i is uppercase
            upper_case = i.isupper() 
        
            #Casts i to lowercase since dictionaries use lowercase
            i = i.lower()            
        
            if i in letter_to_no.keys():
                ind = letter_to_no[i]
            
                if shift_direction == 'Kanan':
                    shift_ind = ind + shift_amount
                else:
                    shift_ind = ind - shift_amount
            
                # Divides by 26 because alphabet has 26 letters
                # Uses remainder as key
                sub = no_to_letter[shift_ind % 26]
        
            else:
                sub = i
        
            sub = sub.upper() if upper_case else sub
            answer = answer + sub
    
        return answer

    answer = shift(phrase, shift_direction, shift_amount)

    # Outputs
    st.subheader(f'Hasil Enkripsi : ')
    st.markdown(f'{answer}')



# ---------- Selectbox for multipage ------------------------
pages = {
    "Definisi": main_page,
    "Perlindungan": page2,
    "Caesar Cipher": cipher_page
}

selected_page = st.sidebar.selectbox("Pindah halaman", pages.keys())
pages[selected_page]()
