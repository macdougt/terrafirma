# On terrafirma with terraform

Let's start with a story. 

Suppose I want to install gitlab. I used to google dockerhub gitlab and then start with a docker-compose file or if a Dockerfile was enough, I would try that.

Now that I have ventured into the land of kubernetes, I peruse helm and then hopefully terraform.

To start with how do I get a helm chart for git lab working?

Using google once again, I found some instructions and proceeded with the following:

```bash
helm repo add gitlab https://charts.gitlab.io/
helm repo update
helm upgrade --install gitlab gitlab/gitlab \
  --set global.hosts.domain=example.com \
  --set global.hosts.externalIP=10.10.10.10 \
  --set certmanager-issuer.email=email@example.com
kubectl --address <ip> port-forwardservice/gitlab-webservice-default 8181:8181 &
```
[reference](https://docs.gitlab.com/charts/installation/deployment.html#deploy-using-helm)

After some tweaking, I arrived at the above commands and all's well that ends well.

Next I want to move my content to terraform and so I create my terrafirma directory and populated files as shown in the terraform directory.

Then run the following:
```bash
terraform init
terraform apply
kubectl --address <ip> port-forwardservice/gitlab-webservice-default 8181:8181 &
```
