from PIL import Image
import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie
#emojis are in the following link: https://www.webfx.com/tools/emoji-cheat-sheet/

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")


# --- LOAD ASSETS ---
lottie_hello = load_lottieurl("https://lottie.host/b8d6d34f-6ab9-4e93-a80e-2f6faa20f0fc/d0peo4HvPq.json")
img_phone = Image.open("images/webdev.png")
gsu_logo = Image.open("images/gsulogo.png")
leetcode = Image.open("images/leetcode.png")
selflearning = Image.open("images/selflearning.png")
projects = Image.open("images/projects.png")


# ----- HEADER SECTION -----

st.title("Welcome to Application Development Track Tips")
st.subheader("Georgia State University Computer Information Systems Students")
st.write("This webpage is for CIS majors on the Application Development Track, the following are things you should know, run by Students for Students")
st.write("[Learn More About GSU CIS >](https://admissions.gsu.edu/program/computer-information-systems-bba/)")

# ---- What we are missing as CIS students"

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Data Structures and Algorithms")
        st.write('##')
        st.write(
            """
            As Computer Information Systems (CIS) Students we are actually behind in knowledge from Computer Science (CS) majors as Data Structures and Algorithms are not full classes
            in CIS as they are for CS majors. All CIS students still have a chance of becoming software engineers as long as they are determined and dedicated to learning more than what the school teaches.
            PLEASE DO NOT BE DISCOURAGED, the professors at GSU are part of the industry and they will also
            tell us to study more than what we learn in class!


            Data structures and algorithms are fundamentals that need to be learned and understood to properly pass a coding interview.

            Data Structures:
            - List
            - Tuples
            - Sets
            - Dictionary
            - etc

            Algorithms:
            - Time Complexity and Big O notion
            - Linear Search
            - Binary Search
            - Hashs
            - Binary Trees
            - etc

            Remember if you do not use it you lose it, so be prepared to practice over and over!
            Below you will see a link to a Python Data Structures and Algorithms book provided by GSU Libary:
            """
        )
        st.write("[GALEO Book: GSU LOGIN REQUIRED >](https://ebookcentral.proquest.com/lib/gsu/reader.action?docID=4868549&ppg=2)")
    with right_column:
        st_lottie(lottie_hello, height=300, key="hello")

#Tip number 1
with st.container():
    st.write("---")
    st.header("Tips For GSU Students")
    st.subheader("Tip #1")
    st.write("##")
    image_column, text_column = st.columns((1, 2))

    with image_column:
        st.image(gsu_logo)

    with text_column:
        st.subheader("Know What Track You want!")
        st.write(
            """

            Ensure that you know what Computer Information Systems track you are going to take, This website is geared more towards
            Application Development. Below you will find a link with all of the tracks straight from the information straight from the GSU CIS department.

            Around Two to Three-years out from graduation, you would have taken CIS 2010 (Introduction to Information Systems),
            this course introduces you to the basics of information systems technology and applications in organizations and professional settings.
            I dare to say that this is one of the easiest classes you will have as a CIS Major.

            Once you complete area A-E Core Curriculum you will begin your Computer Information Systems BBA Major classes with
            CIS 3260 Introduction to Programming where you will go over elementary programming in Python. At the end of the chapters,
            you should have an understanding of a few Python Data structures and the Foundation of Python. The course is very difficult if
            you are being introduced to coding so ensure that you are prepared to study.

            After taking completing CIS 3260 I would recommend attempting some of the leet code questions, the next tip talks about this so ensure to keep reading!

            A big tip that not many students know is that CIS 3260 also comes with an additional class 3260E which is "CIS Career Advancement"
            Where you need to attend Networking events, Career Fairs, and many other requirements. Take the chance to network and try to land an
            internship or at least get your name out there with a recruiter. These things seem very redundant but at the end of the day, you
            never know who you will meet and possibly land a job this way.



            """
        )
        st.markdown("[GSU CIS Tracks >](https://admissions.gsu.edu/program/computer-information-systems-bba/))")

# Tip number 2
with st.container():
    st.write("---")
    st.header("Tips For GSU Students")
    st.subheader("Tip #2")
    st.write("##")
    image_column, text_column = st.columns((1, 2))

    with image_column:
        st.image(leetcode)

    with text_column:
        st.subheader("LeetCode")
        st.write(
            """

            LeetCode is very difficult at first but once you take CIS 3260 you will have a problem-solving mentality. This all comes
            from solving problems in class together with the professor and your peers. Do not stop their test yourself ensure that you
            can make your code as optimal as possible. Solving LeetCode questions will prepare you for an interview as many companies will
            have LeetCode questions and will use HackArank to test you during your technical interview process. I would recommend to
            practice one-two questions a day about one to two months out from an interview

            """
        )
        st.markdown("[LeetCode >](https://leetcode.com/))")

# Tip number 3
with st.container():
    st.write("---")
    st.header("Tips For GSU Students")
    st.subheader("Tip #3")
    st.write("##")
    image_column, text_column = st.columns((1, 2))

    with image_column:
        st.image(selflearning)

    with text_column:
        st.subheader("Self-Learning")
        st.write(
            """

            Ensuring that you are on top of your game with new technologies is very important, do not stop learning!
            self teach yourself and ensure that you are a few steps or one step ahead of your classes. If you know you are going
            to learn Java take the initiative and start watching videos or reading up about those languages. Self Learning will
            always be a part of a Software Engineers life so ensure that you develop good habits. A book I recommend is Cracking the
            coding interview, this book will break down the interview process and how you can stay steps ahead of your peers
            to secure an interview or even just be a better Software Engineer.

            """
        )
        st.markdown("[Cracking the Coding Interview >](https://www.crackingthecodinginterview.com/))")

# Tip number 4
with st.container():
    st.write("---")
    st.header("Tips For GSU Students")
    st.subheader("Tip #4")
    st.write("##")
    image_column, text_column = st.columns((1, 2))

    with image_column:
        st.image(projects)

    with text_column:
        st.subheader("Have your Own Projects")
        st.write(
            """
            Having any coding project will help you immensely in an interview and shows your willingness to learn and love
            for coding. My first project was a website for a podcast that I ran and now I created this website to help CIS students
            understand the tip of the iceberg of what it is to become a Software Engineer. Self Projects will show your skills and
            also show your initiative. Try coding a website, or a clock, or find something that interests you. It is very important
            to show off your skills to land that first Software Engineer Position.

            """
        )
        st.markdown("[Creating a website using Streamlit and Python >](https://www.youtube.com/watch?v=VqgUkExPvLY&list=LL&index=7))")

# Tip number 5
#with st.container():
 #   st.write("---")
  #  st.header("Tips For GSU Students")
   # st.write("##")
   # image_column, text_column = st.columns((1, 2))

    #with image_column:
     #   st.image(img_phone)

   # with text_column:
    #    st.subheader("Two-Years out from Graduation")
      #  st.write(
       #     """
        #    Ensure that you know what Computer Information Systems track you are wanting to go, This website is specific to
         #   Application Developemnt. Below you will find a link with all of the inforamtion stright from GSU CIS department.

          #  """
        #)
        #st.markdown("[GSU CIS Tracks >](https://admissions.gsu.edu/program/computer-information-systems-bba/))")

# --- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Students")
    st.write("##")

    # Documention: https://formsubmit.com/ CHANGE EMAIL ADDRESS
    contact_form = """
    <form action="https://formsubmit.co/cisappdevtips@gmail.com" method="POST">
      <input type="hidden" name="_captcha" value="false">
      <input type="text" name="name" placeholder="Your Name" required>
      <input type="email" name="email" placeholder= "Your Email" required>
      <textarea name="message" placeholder="Your Message Here" requried></textarea>
      <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
