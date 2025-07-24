#!/usr/bin/env bash
# Build, push and deploy image + manifests.

IMAGE="dipakrasal2009/sre_bootcamp-api1:v27"

echo "🔨 Building $IMAGE"
docker build -t "$IMAGE" .

echo "🚀 Pushing $IMAGE"
docker push "$IMAGE"

echo "📦 Applying Kubernetes manifests"
kubectl apply -f k8s-manifest/namespace.yml
kubectl apply -f k8s-manifest/secrets.yml
kubectl apply -f k8s-manifest/database.yml
kubectl apply -f k8s-manifest/application.yml

echo "✅ Deployed!"

