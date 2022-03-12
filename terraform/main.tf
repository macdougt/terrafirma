resource "helm_realease" "gitlab" {
    name       = "gitlab"
    repository = "https://charts.gitlab.io"
    chart      = "gitlab"
    values     = [
        file("${path.module}/${var.gitlab_enviroment_values_file}")
    ]
    namespace  = var.namespace
    timeout    = var.timeout
}