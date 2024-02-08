import streamlit as st
import streamlit as st
import pandas as pd
import numpy as np
import csv
import xml.etree.ElementTree as ET
import pandas as pd



def seeTable(n):
    tree = ET.parse('tables.xml')
    root = tree.getroot()

    comp = root[n][0][0].text
    source = root[n][0][1].text
    typename = root[n][0][2].text

    head = root[n][1].text.strip().split('|')
    table = []
    for i in range(2, len(root[n])):
        table.append(root[n][i].text.strip().split('|'))

    table = pd.DataFrame(table, columns=head)
    return comp,source,typename,table



tables = []

# for i in range(1509):
for i in range(15):
    num = i
    comp,source,typename,table = seeTable(num)
    tables.append(table)


# for i in tables:
#     print(i, end='\n\n\n')


anno = []

def nextpage():
    st.session_state.page += 1

def prevpage():
    st.session_state.page -= 1

def restart(): 
    st.session_state.page = 0
bound = len(tables)


if "page" not in st.session_state:
    st.session_state.page = 0
    
st.write('Table')
placeholder = st.empty()
st.button("Submit & Next",on_click=nextpage)
st.button("Previous",on_click=prevpage)

# if st.session_state.page < bound:
#     # Replace the placeholder with some text:
#     placeholder.text(f"Hello, this is page {st.session_state.page}")

if st.session_state.page < bound:
    placeholder.table(tables[st.session_state.page])
    st.write("Instance Number "+str(st.session_state.page+1))
    txt = st.text_area('Write Annotated Text Here:', height=200)
    
    file = open("Annotated/"+str(st.session_state.page)+".txt","w")
    file.write(txt)
    file.close()
    
    st.write("Got: "+txt)
    st.empty()
    