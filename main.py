import json

# Listen for commands and respond accordingly
while True:
    command = input()  # Wait for input command
    response = {}

    if command == 'hello':
        response['message'] = 'Hello from Python script!'
    elif command == 'bye':
        response['message'] = 'Goodbye from Python script!'
    else:
        response['message'] = 'Unknown command'

    # Send the response as JSON
    print(json.dumps(response))
