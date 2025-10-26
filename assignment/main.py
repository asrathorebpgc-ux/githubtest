import google.generativeai as genai
import os
import json
import datetime

myfile="text.txt"
try:
    with open(myfile,'r') as myfile:
        prompt=myfile.read()
        print("successfully read from the file.")
except FileNotFoundError:
    print("Error: the file was not found.")
    prompt= None
if prompt:
    try: 
        api_key= "AIzaSyDMa6i7hNgsbGHREr1o8-0uu0_LEOqEwhg"
        genai.configure(api_key=api_key)
        model=genai.GenerativeModel('gemini-2.5-pro')
        print("Sending prompt to Gemini \n")
        response=model.generate_content(prompt)
        print("--- Full AI Response Object ---")
        print(response)
        print("-----------------------------\n")

        
        print("--- AI Response Text ---")
        print(response.text)
       

        
        ai_response_text = response.text

       
        output_data = {
            "prompt": prompt,
            "response": ai_response_text
        }

        
        timestamp_str = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"response_{timestamp_str}.json"

        
        with open(output_filename, 'w') as json_file:
            
            json.dump(output_data, json_file, indent=4)
        
        print(f"✅ Successfully saved the response to '{output_filename}'")

        print("------------------------\n")
    except Exception as e:
        print(f"An error occured in calling the api: {e}")
    pass

