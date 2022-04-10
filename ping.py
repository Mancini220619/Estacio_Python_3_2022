from pythonping import ping

#função que ira realizar o ping e retornar os dados coletados
def pingar_servidor(host):
    ping_result = ping(target=host, count=10, timeout = 2)

    return {
        'host': host,
        'avg_latency': ping_result.rtt_avg_ms,
        'min_latency': ping_result.rtt_min_ms,
        'max_latency': ping_result.rtt_max_ms,
        'packet_loss': ping_result.packet_loss
    }

#lista com os servidores a serem testados
hosts = [
    '8.8.8.8',
    '8.8.4.4'
]

for host in hosts:
    print(pingar_servidor(host))