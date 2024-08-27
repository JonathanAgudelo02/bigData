import boto3 

  

# Crear una sesión de cliente de S3 

s3 = boto3.client('s3') 

  

# Obtener la lista de buckets 

response = s3.list_buckets() 

  

print("Buckets disponibles en tu cuenta:") 

for bucket in response['Buckets']: 

    print(f"  - {bucket['Name']}") 