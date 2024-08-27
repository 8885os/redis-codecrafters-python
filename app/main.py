import asyncio
import argparse

dir = None
dbfilename = None
async def connect(reader, writer):
    while True: 
        data = await reader.read(1024)
        data = data.decode('utf-8') 
        if not data:
            break
        data = data.split('\r\n')
        match data[2]:
            case 'ECHO':
                writer.write(f'+{data[4]}\r\n'.encode('utf-8'))
                await writer.drain()
            case 'PING':
                writer.write(f'+PONG\r\n'.encode('utf-8'))
                await writer.drain()
            case 'SET':
                dataList[data[4]] = f'+{data[6]}\r\n'
                for i in range(len(data)):
                    if data[i].lower() == 'px':
                        asyncio.ensure_future(timer(float(data[10]) / 1000, data))
                writer.write(f'+OK\r\n'.encode('utf-8'))
                await writer.drain()
                    
            case 'GET':
                writer.write(dataList.get(data[4]).encode('utf-8'))
                print(dataList.get(data[4]))
                await writer.drain()
            case 'CONFIG':
                for i in range(len(data)):
                    if data[i].lower() == 'get' and data[i+2].lower() == 'dir':
                        key = data[i+2]
                        resp = f'*2\r\n${len(key)}\r\n{key}\r\n${len(dir)}\r\n{dir}\r\n'
                        writer.write(resp.encode('utf-8'))
                        await writer.drain()
                    elif data[i].lower() == 'get' and data[i+2].lower() == 'dbfilename':
                        key = data[i+2]
                        resp = f'*2\r\n${len(key)}\r\n{key}\r\n${len(dbfilename)}\r\n{dbfilename}\r\n'
                        writer.write(resp.encode('utf-8'))
                        await writer.drain()
async def timer(time,data):
    await asyncio.sleep(time)
    print('this ran asyncio.sleep for', time)
    dataList[data[4]] = f'$-1\r\n'

async def main():
    global dataList
    dataList = {}
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', type=str)
    parser.add_argument('--dbfilename', type=str)
    args = parser.parse_args()
    print(args)
    global dir, dbfilename
    if args.dir:
        dir = args.dir
    if args.dbfilename:
        dbfilename = args.dbfilename
    server = await asyncio.start_server(connect,"localhost", 6379)
    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())