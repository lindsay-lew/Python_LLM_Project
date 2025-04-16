def llm(text):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                # content = prompt
                # Any time I'm using an LLM, I always provide an instruction about how long the output should be
                "content": text,
            }
        ],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content


def split_text(text, max_chunk_size=1000):
    '''
    Takes a string as input and returns a list of strings that are smaller than max_chunk_size. 

    >>> split_text('abcdefg', max_chunk_size=2)
    ['ab', 'cd', 'ef', 'g']

    This is the simplest possible way to split text.
    There are much more sophisticated possibilities.
    Other more complex algorithms will:
    1) Try not to split words/sentences/paragraphs
    2) Provide overlaps between the chunks
    '''
    accumulator = []
    while len(text) > 0:
        accumulator.append(text[:max_chunk_size])
        text = text[max_chunk_size:]
    return accumulator


def summarize_text(text):
    '''
    Our current problem: we cannot summarize large documents. 
    Our solution: recursive summarization. 
    Other solutions exist, no one knows what the best one is. 
    We use recursive summarization because it is easy and illustrates good CS concepts. 

    Two step process:
    1)  Split the document into chunks that are the size of the context window.
        Summarize those chunks using the LLM. 
        This gives us a sequence of smaller documents that we will append together to create a new document that 
        contains the same information as the original document but is smaller.
    2)  Call summarize_text on this new smaller document. 
    '''
    prompt = f'''
    Summarize the following text in 1-3 sentences.

    {text}
    '''
    # return llm(prompt)
    try:
        output = llm(prompt)
        return output.split('\n')[-1]
    except groq.APIStatusError:
        chunks = split_text(text, 10000)
        print('len(chunks)=', len(chunks))
        accumulator = []
        for i, chunk in enumerate(chunks):
            print('i=', i)
            # This is called recursion: recursion = when you call a function inside itself
            summary = summarize_text(chunk)
            accumulator.append(summary)
        summarized_text = ' '.join(accumulator)
        summarized_text = summarize_text(summarized_text)
        # print('summarized_text=', summarized_text)
        return summarized_text
        pass



if __name__ == '__main__':
        
    import argparse
    parser = argparse.ArgumentParser(
        prog='docsum',
        description='summarize the input document',
        )
    parser.add_argument('filename')
    args = parser.parse_args()      
    # print('filename=', args.filename)

    from dotenv import load_dotenv
    load_dotenv()  

    import os
    from groq import Groq
    import groq
    import base64

    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )

    # To pass images from URLs as inputs 
    completion = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Explain and describe what is in this image of the cube in 3 sentences, using English only. No HTML or formatting tags."
                    },

                    {
                        "type": "image_url",
                        "image_url": {
                            "url": "https://www.cmc.edu/sites/default/files/about/images/20170213-cube.jpg"
                        }
                    }
                ]
            }
        ],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=False,
        stop=None,
    )
    print(completion.choices[0].message)


    # To pass locally saved images as inputs
    # Encode the image
    def encode_image(image_path):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    # Path to your image
    image_path = "topic10/docsum/images/google.jpg"

    # Getting the base64 string
    base64_image = encode_image(image_path)

    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Google image meme"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}",
                        },
                    },
                ],
            }
        ],

        model="meta-llama/llama-4-scout-17b-16e-instruct",
    )
    print(chat_completion.choices[0].message.content)



    # One way to solve the problem of too much text for the context window is to remove the "unneccessary text"
    # For html files, that is the html tags
    from bs4 import BeautifulSoup
    import requests 
    import textract

    try:
        # Use textract to extract text from PDF
        if args.filename.lower().endswith('.pdf'):
            text = textract.process(args.filename).decode('utf-8')

        else:
            # Else, extract from html file
            with open(args.filename, 'r') as fin:
                html = fin.read()
            soup = BeautifulSoup(html, features="lxml")
            text = soup.text

    except (FileNotFoundError):
        # If the file doesn't exist, assume it's a URL
        url = args.filename
        print('url=', url)

        # Download html
        r = requests.get(url)
        status = r.status_code
        print('status=', status)
        html = r.text

        soup = BeautifulSoup(html, features="lxml")
        text = soup.text
    
    # print('text=', text)
    print(summarize_text(text))

