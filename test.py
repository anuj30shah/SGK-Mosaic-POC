import boto3
import json

def get_info(company, product):

    prompt_data = f"""
    The product is {product} by {company}. Pretend you are an running an advertising campaign for this product. Make sure all photo shots are unique.
    Return text in the following format with brackets and quotes:

    {{
        "tagline": give a 10-12 word description for the product,
        "advantage1:": give another 3-4 word tagline for the product,
        "advantage2:": give another 3-4 word advantage of the product,
        "advantage3:": give another 3-4 word advantage of the product,
        "angle1": give one possible angle for the product shot,
        "angle2": give another possible angle for the product shot,
        "angle3": give another possible angle for the product shot,
        "angle4": give another possible angle for the product shot,
        "angle5": give another possible angle for the product shot,
        "angle6": give another possible angle for the product shot,
        "angle7": give another possible angle for the product shot,
        "angle8": give another possible angle for the product shot,
        "angle9": give another possible angle for the product shot
    }}

    Do not return any other text. Begin the response with the first "{{" and end with the last "}}". 
    """

    bedrock = boto3.client(service_name='bedrock-runtime')

    payload = {
        "inputText": prompt_data,
        "textGenerationConfig": {
            "maxTokenCount": 300,
            "stopSequences": [],
            "temperature": 0.5,
            "topP": 1
        }
    }

    body = json.dumps(payload)
    model_id = "amazon.titan-text-express-v1"
    response = bedrock.invoke_model(
        modelId=model_id,
        body=body,
        contentType="application/json",
        accept="application/json"
    )

    response_body = json.loads(response["body"].read())
    answer = response_body['results'][0]['outputText']

    print(answer)

    jayson = json.loads(answer)

    tagline = (jayson['tagline'])
    adv1 = (jayson['advantage1'])
    adv2 = (jayson['advantage2'])
    adv3 = (jayson['advantage3'])
    ang1 = (jayson['angle1'])
    ang2 = (jayson['angle2'])
    ang3 = (jayson['angle3'])
    ang4 = (jayson['angle4'])
    ang5 = (jayson['angle5'])
    ang6 = (jayson['angle6'])
    ang7 = (jayson['angle7'])
    ang8 = (jayson['angle8'])
    ang9 = (jayson['angle9'])

    return tagline, adv1, adv2, adv3, ang1, ang2, ang3, ang4, ang5, ang6, ang7, ang8, ang9
