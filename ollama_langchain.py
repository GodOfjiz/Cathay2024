from langchain_ollama import ChatOllama
from langchain_core.messages import AIMessage
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOllama(
    model="llama3.1",
    temperature=0,
    # other params...
)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful travel assistant that is an expert in helping people to plan for their travel. There will be data and parameters given for you to draft the plan. Respond in a json format in the following parameters: userID: {userID}, location: {location}, airport: {airport}, departureDate: {departureDate}, returnDate: {returnDate}, dayLength: {dayLength}, totalBudget: {totalBudget}. Do not add any extra words in the response unless they're in the .json. "
        ),
        ("human", "{input}"),
    ]
)

chain = prompt | llm

answer = chain.invoke(
    {
        "userID": "01234",
        "location": "Hong Kong",
        "airport": "HKG",
        "departureDate": "2024-12-30",
        "returnDate": "2025-01-12",
        "dayLength": "12",
        "totalBudget": "20000",
        "input": "Tell me what you can do in the location with an event: {events} in the json together with my data. Make sure the event is in the range of departuredate and returndate. Include as many events as you can and include a one to two line description."
    }
)

print(answer.content)


