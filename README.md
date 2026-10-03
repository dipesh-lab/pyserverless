## PY Serverless

### Set AWS credential by environment variables

```export AWS_ACCESS_KEY_ID```
```export AWS_SECRET_ACCESS_KEY```
```export AWS_SESSION_TOKEN```

```terraform init -backend-config 'region=ap-southeast-2' -backend-config 'bucket=tfstate-resources-128779316957-ap-southeast-2-an' -lock=true```
```aws sts get-session-token```
### Setup & select workspace
```terraform workspace select -or-create dev-ap-southeast-2```

### Plan resources
```terraform plan -var-file tfvars/dev.tfvars -out deployment.tfplan```

### Apply resources
```terraform apply deployment.tfplan```