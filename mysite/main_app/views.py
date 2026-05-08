from django.shortcuts import render
from django.http import HttpResponse

import os
import grpc
import services_pb2
import services_pb2_grpc
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
            # grab the address from the environment variable
            # localhost:50050 is the fallback
            orchestrator_target = os.getenv('ORCHESTRATOR_ADDRESS', 'localhost:50050')

            # open a connection to the Orchestrator with the given ip from gcp
            # The 'with' statement ensures the channel closes safely after the call
            with grpc.insecure_channel(orchestrator_target) as channel:


                # create the stub for the Orchestrator
                stub = services_pb2_grpc.OrchestratorStub(channel)

                # create the request message
                grpc_request = services_pb2.Name(name=username)

                # call the orchestrator server
                response = stub.ExecuteAccessCheck(grpc_request)

                # check if authenticated
                if response.is_authenticated:
                    # If valid, unpack the stats for the HTML template
                    context['result'] = f"User is Valid! {username}'s favorite color is {response.fav_color} and their number is {response.fav_number}."
                else:
                    # If invalid, show an error
                    context['error'] = f"Access Denied: '{username}' is not in the system."

            #context['result'] = f"Successfully verified {username} via C++ username checker service."

        except grpc.RpcError as e:
            # captures specific network/VPC blocks
            context['error'] = f"gRPC Connection Failed: {e.code()} - {e.details()}"
        except Exception as e:
            # captures local Python errors
            context['error'] = f"Local System Error: {str(e)}"

    # Both GET and POST return the same template
    # If it was a GET, context is empty, so no results show up.
    # If it was a POST, context has 'result' or 'error'.
    return render(request, 'main_app/index.html', context)




