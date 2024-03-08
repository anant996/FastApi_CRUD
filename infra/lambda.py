import json
from auth import check_token

def lambda_handler(event, context):
    status_code = None
    message = None
    
    try:
        http_method = event['requestContext']['http']['method']
        
        if http_method == 'GET':
            query_params = event['queryStringParameters']
            first_name = query_params['first_name']
            last_name = query_params['last_name']
            if first_name is not None and last_name is not None:
                full_name = f"{first_name} {last_name}"
                status_code = 200
                message = full_name
            else:
                status_code = 400
                message = "Both 'first_name' and 'last_name' query parameters are required."
                
        elif http_method == 'POST':
            request_body = json.loads(event['body'])
            headers = event['headers']
            auth_token = headers['auth_token']
            if auth_token and check_token(auth_token):
                first_name = request_body['first_name']
                last_name = request_body['last_name']
                if first_name is not None and last_name is not None:
                    full_name = f"{first_name} {last_name}"
                    status_code = 200
                    message = full_name
                else:
                    status_code = 400
                    message = "Both 'first_name' and 'last_name' query parameters are required."
            else:
                status_code = 400
                message = "User not authenticated"
    except Exception as e:
        status_code = 500
        message = "Internal Server Error"
    
    finally:
        return {
            "status_code": status_code,
            "message": message
        }
        