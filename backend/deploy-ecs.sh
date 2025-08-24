#!/bin/bash

# Variables
AWS_REGION="us-east-1"
AWS_ACCOUNT_ID="YOUR_ACCOUNT_ID"
ECR_REPOSITORY="downloads-organizer-backend"
ECS_CLUSTER="downloads-organizer-cluster"
SERVICE_NAME="downloads-organizer-backend"

echo "Starting ECS deployment..."

# Build and tag Docker image
echo "Building Docker image..."
docker build -t $ECR_REPOSITORY .

# Tag for ECR
docker tag $ECR_REPOSITORY:latest $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPOSITORY:latest

# Login to ECR
echo "Logging into ECR..."
aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com

# Create ECR repository if it doesn't exist
echo "Creating ECR repository..."
aws ecr create-repository --repository-name $ECR_REPOSITORY --region $AWS_REGION 2>/dev/null || echo "Repository already exists"

# Push image to ECR
echo "Pushing image to ECR..."
docker push $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPOSITORY:latest

# Create ECS cluster if it doesn't exist
echo "Creating ECS cluster..."
aws ecs create-cluster --cluster-name $ECS_CLUSTER --region $AWS_REGION 2>/dev/null || echo "Cluster already exists"

# Create CloudWatch log group
echo "Creating CloudWatch log group..."
aws logs create-log-group --log-group-name /ecs/$ECR_REPOSITORY --region $AWS_REGION 2>/dev/null || echo "Log group already exists"

# Register task definition
echo "Registering task definition..."
aws ecs register-task-definition --cli-input-json file://ecs-task-definition.json --region $AWS_REGION

# Create or update service
echo "Creating/updating ECS service..."
aws ecs describe-services --cluster $ECS_CLUSTER --services $SERVICE_NAME --region $AWS_REGION > /dev/null 2>&1

if [ $? -eq 0 ]; then
    echo "Service exists, updating..."
    aws ecs update-service --cluster $ECS_CLUSTER --service $SERVICE_NAME --task-definition $ECR_REPOSITORY --region $AWS_REGION
else
    echo "Service doesn't exist, creating..."
    aws ecs create-service --cli-input-json file://ecs-service.json --region $AWS_REGION
fi

echo "Deployment completed!"
echo "Check service status with: aws ecs describe-services --cluster $ECS_CLUSTER --services $SERVICE_NAME --region $AWS_REGION"