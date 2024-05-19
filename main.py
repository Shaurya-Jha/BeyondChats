import requests
import os
import json
import pprint

endpoint = "https://devapi.beyondchats.com/api/get_message_with_sources";

response = requests.get(endpoint)

if response.status_code == 200:
    # clear the console
    os.system("cls")

    # data = response.content
    # data = response.json()
    # # newData = json.loads(data)
    # # formattedData = json.dumps(newData, indent=1)
    # print("Data: ",data)

    # # getting parent data
    # mainData = data['data']['data']
    # # print("\n\nParent data: ", mainData)

    # for data in mainData:
    #     print("\n\n\n",data['source'])

    #     # source - this is working
    #     sources = data['source']
    #     print("\nSources: ", sources)

    data = response.json()
    # print(data)

    # map through json and get the final data json object
    sourceData = data['data']['data']
    # print("\n\n", sourceData)

    # get all the sources in the json data object
    for responseList in sourceData:
        print("\nResponse: ", responseList['response'])
        sourceList = responseList['source']
        # print("\n\nSource List: ",sourceList)

        # prettying the output
        # formatData = json.load(sourceList)
        # print(formatData)
        # json_formatted_str = json.dump(formatData, indent=4)

        # citations
        citations = sourceList
        # print("\ncitations = ", citations)
        print("\ncitations: ")
        pprint.pprint(citations)

    # for source in sourceData:
    #     sourceList = source['source']
    #     print("\n\nSource List: ", sourceList)
elif response.status_code == 404:
    print("\nNot found")