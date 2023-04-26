#Importing the Neccessary Dependencies

import os
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI
from langchain.chains import LLMChain, SequentialChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory

#Utilising the openai API_key
os.environ['OPENAI_API_KEY'] = apikey 

#Frontend Display
#These next syntax displays the title of which is "Cooking Recipe"

st.title("Cooking Recipe")
prompt = st.text_input('Type in the Food You would Like to make')


#Prompt
recipe_template = PromptTemplate(
    input_variables = ['recipe'],
    template = 'Write me a detailed cooking stpes based on this {recipe}'
)

#Memory
recipe_memory = ConversationBufferMemory(input_key='recipe', memory_key='chat_history')


#LLMs
llm = OpenAI(temperature=0.97)
recipe_chain = LLMChain(llm=llm, prompt=recipe_template, verbose =True, output_key='recipe', memory=recipe_memory)


#Displaying the result

if prompt:
    recipe = recipe_chain.run(prompt)
    st.write(recipe)
    
    with st.expander('Recipe History'):
        st.info(recipe_memory.buffer)