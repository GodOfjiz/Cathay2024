from langchain_ollama import ChatOllama
from langchain_core.messages import AIMessage
from langchain_core.prompts import ChatPromptTemplate

def chatbot(question):
    llm = ChatOllama(
        model="llama3.1",
        temperature=0,
        # other params...
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a helpful travel assistant working for Cathay Pacific that is an expert in helping people to plan for their travel. DO NOT mention anything outside of travel planning. DO NOT promote other airline companies other than Cathay Pacific. If any business or sales related activities are initiated, such as flight cancellation or seeking for compensation, ask them to further consult assistance at hackathon_test@cathaypacific.com"
            ),
            ("human", "{input}"),
        ]
    )

    chain = prompt | llm

    answer = chain.invoke(
        {
            "input": question
        }
    )

    return answer.content
