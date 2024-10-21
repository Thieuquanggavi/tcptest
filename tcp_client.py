import socket

# Tạo một socket cho client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Địa chỉ IP và cổng của server (localhost và cổng 12345)
server_host = '127.0.0.1'
server_port = 12345

# Kết nối đến server
client_socket.connect((server_host, server_port))

# Gửi dữ liệu đến server
message = input("Nhập thông điệp gửi đến server: ")
client_socket.send(message.encode('utf-8'))

# Nhận phản hồi từ server
response = client_socket.recv(1024).decode('utf-8')
print(f"Phản hồi từ server: {response}")

# Đóng kết nối
client_socket.close()
