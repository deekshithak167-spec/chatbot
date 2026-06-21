import os
from groq import Groq
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
print("welcome to chatbot: enter quit or exit orbye to stop")
while True:
    user_input=input("you:")
    if user_input.lower() in ["quit","exit","bye"]:
        print("Thankyou for using the chatbot ,have a nice day")
        break
    print("Chatbot:",end="",flush=True)
    try:
        stream=client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role":"system","content":"you are a helpful chatbot"},
                    {"role":"user","content":user_input}],
            stream=True
        )
        for chunks in stream:
            if chunks.choices[0].delta.content:
                print(chunks.choices[0].delta.content,end="",flush=True)
        print()
    except Exception as e:
        print("Error:",e)

