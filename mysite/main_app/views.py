from django.shortcuts import render
from django.http import HttpResponse

import grpc
# generated gRPC files go here

# create your views here.
def home_view(request):
    # this variable will hold what we show to the user
    context = {}

    # Check if the user clicked the button (POST)
    if request.method == 'POST':
        # grab the text from the textbox from our html
        username = request.POST.get('username')

        try:
            # Logic: Talk to your C++ Microservice

            # (Replace with your actual gRPC stub/channel logic)
            # response = stub.GetUserReport(UserRequest(username=username))

            # response = stub.GetUserReport(UserRequest(username=username))
            # context['result'] = response.summary

            # Store the result for the template if success

            context['result'] = f"Successfully verified {username} via C++ Backend."

        except grpc.RpcError as e:
            # Captures specific network/VPC blocks
            context['error'] = f"gRPC Connection Failed: {e.code()} - {e.details()}"
        except Exception as e:
            # Captures local Python errors
            context['error'] = f"Local System Error: {str(e)}"

    # Both GET and POST return the same template
    # If it was a GET, context is empty, so no results show up.
    # If it was a POST, context has 'result' or 'error'.
    return render(request, 'main_app/index.html', context)
