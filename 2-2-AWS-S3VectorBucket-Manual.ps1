##Pre-Requisite 
<#
Install AWS CLI v2
msiexec.exe /i https://awscli.amazonaws.com/AWSCLIV2.msi
aws --version
aws configure
##Install s3vectors-embed-cli
pip install s3vectors-embed-cli
s3vectors-embed --help
#>
##Create the s3 bucket and the index
aws s3vectors create-vector-bucket --vector-bucket-name acd-aws-s3-cli-demo --region us-east-1
##Create vector index with 1024 dimensions, cosine distance metric and float32 data type
aws s3vectors create-index --vector-bucket-name acd-aws-s3-cli-demo --index-name demo-index --dimension 1024 --distance-metric cosine --data-type float32

s3vectors-embed put --vector-bucket-name acd-aws-s3-cli-demo --index-name demo-index --model-id amazon.titan-embed-text-v2:0 --text-value "I love cricket"
s3vectors-embed put --vector-bucket-name acd-aws-s3-cli-demo --index-name demo-index --model-id amazon.titan-embed-text-v2:0 --text-value "I love football"
s3vectors-embed put --vector-bucket-name acd-aws-s3-cli-demo --index-name demo-index --model-id amazon.titan-embed-text-v2:0 --text-value "I love AWS cloud"
s3vectors-embed put --vector-bucket-name acd-aws-s3-cli-demo --index-name demo-index --model-id amazon.titan-embed-text-v2:0 --text-value "Amazon EC2 is cloud computing"
s3vectors-embed put --vector-bucket-name acd-aws-s3-cli-demo --index-name demo-index --model-id amazon.titan-embed-text-v2:0 --text-value "Biryani is delicious food"

##Query the vectors with the text 
s3vectors-embed query --vector-bucket-name acd-aws-s3-cli-demo --index-name demo-index --model-id amazon.titan-embed-text-v2:0 --text-value "cloud" --k 2
##List the indexes
aws s3vectors list-indexes --vector-bucket-name acd-aws-s3-cli-demo

##To view the metadata and vectors
aws s3vectors get-vectors --vector-bucket-name acd-aws-s3-cli-demo --index-name demo-index --key 1388c6df-41ed-4561-bbb5-eec6b3ba5899 --return-data