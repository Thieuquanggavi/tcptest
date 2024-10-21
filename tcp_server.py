import socket

# Tạo một socket cho server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Địa chỉ IP và cổng cho server (localhost và cổng 12345)
server_host = '127.0.0.1'  # localhost
server_port = 12345

# Bind server với địa chỉ và cổng
server_socket.bind((server_host, server_port))

# Lắng nghe kết nối (tối đa 5 kết nối đồng thời)
server_socket.listen(5)
print(f"Server đang lắng nghe tại {server_host}:{server_port}...")

while True:
    # Chấp nhận kết nối từ client
    client_socket, client_address = server_socket.accept()
    print(f"Đã kết nối với {client_address}")

    # Nhận dữ liệu từ client (tối đa 1024 bytes)
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Nhận được từ client: {data}")

    # Phản hồi lại client
    response = "Dữ liệu đã nhận: " + data
    client_socket.send(response.encode('utf-8'))

    # Đóng kết nối với client
    client_socket.close()
