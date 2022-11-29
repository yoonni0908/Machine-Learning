import json

preprocessed_data = []

fileName = "방송/"

for i in range(1, 18):
    with open(fileName + str(i) + ".json", 'r', encoding='utf-8') as f1:
        json_data = json.load(f1)
        
        text_data = json_data["SJML"]["text"]
        
        
        
        for j in range(len(text_data)):
            data_candidates = text_data[j]["content"]
            
            data_candidates = " ".join(data_candidates)

            data_candidates = data_candidates.replace("  ", " <SP>")
            
            if(len(data_candidates) > 20):
                data_candidates = data_candidates[:20]
            
            if (j%2==1):
                preprocessed_data += data_candidates+" </S>\n"
                with open("sampling_data4.txt", "a") as f2:
                    f2.writelines(preprocessed_data)
            else:
                preprocessed_data = data_candidates +"\t" 
                
            
            