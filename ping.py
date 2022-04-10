from pythonping import ping

#função que ira realizar o ping e retornar os dados coletados
def pingar_servidor(host):
    ping_result = ping(target=host, count=10, timeout = 2)

    return {
        'host': host,
        'avg_latency': ping_result.rtt_avg_ms, #Bad = Greater than 100ms, Acceptable = 40-100ms, Good = 20-40ms
        'min_latency': ping_result.rtt_min_ms, #minimo de latencia
        'max_latency': ping_result.rtt_max_ms, #maximo de latencia
        'packet_loss': ping_result.packet_loss #perda de pacote
    }

#lista com os servidores a serem testados
hosts = [
    '8.8.8.8',
    '8.8.4.4'
]

for host in hosts:
    print(pingar_servidor(host))