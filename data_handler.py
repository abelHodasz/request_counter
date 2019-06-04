
filename = "request_count.txt"


def increment_request(method_):
    requests = read_requests_from_file()
    for method, request in requests.items():
        if method == method_:
            requests[method] += 1
    write_requests_to_file(requests)


def write_requests_to_file(requests={'POST': 0, 'GET': 0, 'DELETE': 0, 'PUT': 0}):
    with open(filename, "w") as request_file:
        for method, request in requests.items():
            request_file.write(method + ":" + str(request) + "\n")


def read_requests_from_file():
    try:
        with open(filename, "r") as request_file:
            requests = {}
            for line in request_file.readlines():
                requests[line.split(":")[0]] = int(line.split(":")[1])
            return requests
    except FileNotFoundError:
        write_requests_to_file()
        return read_requests_from_file()
