# On terra firma with terraform

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
What does this mean?

terraform used helm to set up a kubernetes cluster.

Inspecting the charts [location](https://gitlab.com/gitlab-org/charts/gitlab) for gitlab. We can see that there is a lot of configuration provided in order to stand up a cluster with:

```
28 pods
23 services
14 deployments
14 replicasets
3 statefulsets
4 horizontal scalers
3 jobs
```

The [values.yaml](https://gitlab.com/gitlab-org/charts/gitlab/-/blob/master/values.yaml) configuration file contains 1087 lines: 
```bash
perl -e 'while (<>) {if (/^\s*\#/) {$commentCount++;} else {$nonCommentCount++;}} print "$commentCount comments vs. $nonCommentCount non comments\n";' values.yaml

355 comments vs. 732 non comments
```

There are 36 template files in the [templates](https://gitlab.com/gitlab-org/charts/gitlab/-/tree/master/templates) directory with the following line breakdown:
```
ls -R *.yaml *.tpl | xargs wc -l
      53 _application.tpl
      24 _boolean.tpl
      80 _certificates.tpl
     177 _checkConfig.tpl
      49 _checkConfig_geo.tpl
      97 _checkConfig_gitaly.tpl
      84 _checkConfig_mailroom.tpl
      20 _checkConfig_nginx.tpl
      38 _checkConfig_object_storage.tpl
      82 _checkConfig_postgresql.tpl
      88 _checkConfig_registry.tpl
      75 _checkConfig_sidekiq.tpl
      26 _checkConfig_toolbox.tpl
      50 _checkConfig_webservice.tpl
     427 _deprecations.tpl
      57 _geo.tpl
      82 _gitaly.tpl
     591 _helpers.tpl
      59 _ingress.tpl
      37 _kas.tpl
      22 _migrations.tpl
       8 _minio.tpl
      23 _oauth.tpl
      21 _pages.tpl
     118 _praefect.tpl
       9 _rails.tpl
      37 _redis.tpl
      67 _registry.tpl
      76 _runcheck.tpl
      42 _runner.tpl
      44 _shell.tpl
      13 _workhorse.tpl
     115 application.yaml
      11 chart-info.yaml
      21 initdb-configmap.yaml
      88 upgrade_check_hook.yaml
    2911 total
    ```
