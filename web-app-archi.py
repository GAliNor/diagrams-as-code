from diagrams import Diagram, Cluster, Edge
from diagrams.programming.language import Python
from diagrams.programming.language import Nodejs
from diagrams.programming.framework import Vue
from diagrams.onprem.inmemory import Redis
from diagrams.elastic.elasticsearch import Elasticsearch


with Diagram(name="App Business Architecture", show=False, direction="LR", outformat="png", filename="schemas/app"):

    with Cluster("Python scripts"):
        PRODUCER = Python("Producer")
        with Cluster("Consumers"):
            CONSUMERS = [
                Python("Consumer1"),
                Python("Consumer2"),
                Python("Consumer3")
            ]

    REDIS_QUEUE = Redis('Queue')
    ELASTICSEARCH = Elasticsearch("Index")
    NODEJS = Nodejs("Backend")
    VUE3JS = Vue("Frontend")

    PRODUCER >> Edge(color="darkgreen", label="push") >>\
    REDIS_QUEUE >> Edge(color="darkgreen", label="pop") >>\
    CONSUMERS >> Edge(color="blue") >>\
    ELASTICSEARCH >> Edge(color="darkgreen") >>\
    NODEJS >> Edge(color="darkgreen") >>\
    VUE3JS >> Edge(color="red")
