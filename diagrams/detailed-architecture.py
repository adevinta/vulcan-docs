from diagrams import Cluster, Diagram, Edge
from diagrams.k8s.compute import Pod
from diagrams.aws.general import User
from diagrams.aws.compute import EC2, AutoScaling
from diagrams.aws.database import RDS
from diagrams.aws.storage import S3
from diagrams.aws.integration import SQS
from diagrams.onprem.container import Docker
from diagrams.onprem.inmemory import Redis

with Diagram("Detailed Vulcan Architecture", outformat="png", filename="docs/img/detailed-architecture", show=False):
        scan_result_queue = SQS("scan-result-queue")
        check_result_queue = SQS("check-result-queue")
        check_queue = SQS("check-queue")

        with Cluster("Docker Registry"):
                docker_image = Docker("docker-image")

        with Cluster("Vulcan Agent Clusters"):
                vulcan_agent = AutoScaling("vulcan-agent")

        with Cluster("Vulnerability DB"):
                vulndb_consumer = EC2("vulndb-consumer")
                vulndb_api = EC2("vulndb-api")
                vulndb_db = RDS("vulndb-db")
                vulndb_consumer >> vulndb_db
                vulndb_api >> vulndb_db

        vulndb_consumer >> check_result_queue

        user = User("user")

        with Cluster("User Faced"):
                with Cluster("Vulcan API"):
                        vulcan_api = Pod("vulcan-api")
                        vulcan_api_db = RDS("vulcan-api-db")
                        vulcan_api >> vulcan_api_db
                with Cluster("Vulcan UI"):
                        vulcan_ui = Pod("vulcan-ui")

        vulcan_ui >> vulcan_api
        user >> vulcan_api
        user >> vulcan_ui

        with Cluster("Vulcan Stream"):
                vulcan_stream= Pod("vulcan-stream")
                vulcan_stream_cache = Redis("vulcan-stream-cache")
                vulcan_stream >> vulcan_stream_cache

        with Cluster("Vulcan Persistence"):
                vulcan_persistence = Pod("vulcan-persistence")
                vulcan_persistence_db = RDS("vulcan-persistence")
                vulcan_persistence >> vulcan_persistence_db

        with Cluster("Vulcan Results"):
                vulcan_results = Pod("vulcan-results")
                vulcan_results_storage = S3("vulcan-results-storage")
                vulcan_results >> vulcan_results_storage
   
        vulndb_consumer >> vulcan_results


        
        vulcan_agent >> check_queue
        vulcan_agent >> vulcan_results
        vulcan_agent >> vulcan_stream
        vulcan_agent >> check_result_queue
        vulcan_agent >> docker_image

        with Cluster("Vulcan Scan Engine"):
                vulcan_scan_engine = Pod("vulcan-scan-engine")
                vulcan_scan_engine_db = RDS("vulcan-scan-engine")
                vulcan_scan_engine >> vulcan_scan_engine_db

        vulcan_scan_engine >> vulcan_persistence
        vulcan_scan_engine >> vulcan_stream
        vulcan_api >> vulcan_scan_engine
        vulcan_scan_engine >> check_queue
        check_result_queue >> vulcan_scan_engine
        vulcan_scan_engine >> scan_result_queue
        scan_result_queue >> vulcan_api
        vulcan_api >> vulndb_api

        with Cluster("Vulcan Crontinuous"):
                vulcan_crontinuous = Pod("vulcan-crontinuous")
                vulcan_crontinuous_storage = S3("vulcan-crontinuous-storage")
                vulcan_crontinuous >> vulcan_crontinuous_storage

        vulcan_crontinuous \
                >> Edge() \
                << vulcan_api

