import debugpy

'''
launch.json <---- create at root of project, port 5678 is the default port for visual studio code.
should be able to run python script with debugger and use the launch.json.
{
    "name": "UnrealEngine Python",
    "type": "debugpy",
    "request": "attach",
    "connect": {
        "host": "localhost",
        "port": 5678
    },
    "redirectOutput": true
}
'''

def add(a, b):
	return a + b

# Set up the debugger to listen on port 5678
debugpy.listen(("localhost", 5678))
# Wait for the client to attach
print("Waiting for debugger to attach...")
debugpy.wait_for_client()
# Set a breakpoint
debugpy.breakpoint()
print('hello world')

a = 10
b = 5 

c = add(a,b)
print(f"{a} + {b} = {c}")