class Cluster:
    def __init__(self, cluster):
        self.cluster = cluster

    @classmethod
    def constructCluster(cls, cluster_name):
        cluster = f"ON CLUSTER {cluster_name}"
        return cls(cluster)
