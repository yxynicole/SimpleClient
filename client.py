#!/usr/bin/python
import socket
import argparse

def main(cmd_line_args):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create a socket
    s.settimeout(10)
    s.connect((cmd_line_args.host_name, cmd_line_args.port))  # connect to the server

    prolog = b'cs5700fall2020'
    client_message=(prolog + b' HELLO ' + cmd_line_args.neu_id + b'\n')  # Client greets
    server_msg = talk(s,client_message)

    keep_talking = True
    while keep_talking:
        if 'STATUS' in server_msg:
            solution = round(eval(''.join(server_msg[2:5])))
            server_msg = talk(s,b'%s %d\n'% (prolog,solution))
        elif 'BYE' in server_msg:
            print(server_msg[1])
            keep_talking = False
        else:
            print("--Unknown message---")
            keep_talking = False

    s.close()


def talk(s,msg):
    s.sendall(msg)
    server_msg = s.recv(1024)

    server_msg = server_msg.strip().split(' ')
    return server_msg


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', dest='port', type=int, default=27995)
    parser.add_argument('-s', dest='ssl', action='store_true', default=False)
    parser.add_argument('host_name')
    parser.add_argument('neu_id')

    cmd_line_args = parser.parse_args()
    main(cmd_line_args)
