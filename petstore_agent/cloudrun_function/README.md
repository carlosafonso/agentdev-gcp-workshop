This is what I used to create the PetStore cloud run function. 
Since it is open and public you do not need to create it in your env.
Just use the provided function URL: ASK_JULIA_FOR_URL



Deployment:
export PROJECT_ID="YOUR_PROJECT_ID"
gcloud config set project $PROJECT_ID

# Create a Docker repository named 'cloud-run-source-deploy' in the 'europe-southwest1' region
gcloud artifacts repositories create cloud-run-source-deploy \
    --repository-format=docker \
    --location=europe-southwest1 \
    --description="Docker repository for my applications"

# The image path is now: REGION-docker.pkg.dev/PROJECT_ID/REPO_NAME/IMAGE_NAME
gcloud builds submit \
  --tag europe-southwest1-docker.pkg.dev/$PROJECT_ID/cloud-run-source-deploy/mock-pet-store

gcloud run deploy mock-pet-store \
  --image europe-southwest1-docker.pkg.dev/$PROJECT_ID/cloud-run-source-deploy/mock-pet-store \
  --platform managed \
  --region europe-southwest1 \
  --no-invoker-iam-check