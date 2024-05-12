import hazelcast
def task5_2():
    client = hazelcast.HazelcastClient(cluster_name="ps_cluster", cluster_members=[])
    try:
        queue = client.get_queue("ps_queue").blocking()
        while True:
            item = queue.take()
            print("Recieved: ",str(item))
    finally:
        client.shutdown()

task5_2()