import streamlit as st

st.caption('キャプション `<caption>`')

st.text('''
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor.
Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi.
Proin porttitor, orci nec nonummy molestie, enim est eleifend mi, non fermentum diam nisl sit amet erat.
''')

st.code('''
import streamlit as st
st.snow()''',
language='python',
line_numbers=True)
