import boto3
import yaml
from airflow.hooks.base import BaseHook
def config_load_function(region,bucket):
    if (region == 'env-local') or (region == 'env-us-local'):
        # / usr / local / airflow / dags
        # config_path = os.path.join('/home/ubuntu/fastApiProject/app', 'config.yaml')
        path=f'/usr/local/airflow/dags/config/{region}/config-{region}.yaml'
        with open(path) as f:
            config = yaml.safe_load(f)
    else:
        s3_client = boto3.client("s3")
        response = s3_client.get_object(Bucket=bucket, Key=f"dags/config/{region}/config-{region}.yaml")
        config = yaml.safe_load(response["Body"])


    return config


# def ecs_environment_load(region,LocalEcsUtil, EcsUtil,clusterName ,familyName,containerName, variable, config=None, aws_conn=None ):
#     if region == 'env-local':
#         Ecs = LocalEcsUtil()
#         # Recent Task 가져오기
#         recent_task, network = Ecs.getRecentTask(clusterName=clusterName, familyName=familyName,
#                                                  containerName=containerName, variable=variable, config=config,
#                                                  aws_conn=aws_conn)
#     else:
#         Ecs = EcsUtil()
#         recent_task, network = Ecs.getRecentTask(clusterName=clusterName, familyName=familyName,
#                                                  containerName=containerName, variable=variable)
#
#     return recent_task, network

def aws_conn_load(region,config):
    if (region == 'env-local') or (region == 'env-us-local'):
        aws_conn = BaseHook.get_connection(config['aws_conn_id'])
    else:
        aws_conn=None

    return aws_conn