variable "gitlab_enviroment_values_file" {
    type = string
    default = "values.yaml"
}

variable "namespace" {
    type = string
    default = "gitlab-runner"
}

variable "timeout" {
    default = 120
}