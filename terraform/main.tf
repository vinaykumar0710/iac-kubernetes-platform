terraform {
  required_version = ">= 1.5.0"

  required_providers {
    helm = {
      source  = "hashicorp/helm"
      version = "~> 3.0"
    }
  }
}

provider "helm" {
  kubernetes = {
    config_path    = pathexpand("~/.kube/config")
    config_context = "kind-iac-platform"
  }
}

resource "helm_release" "platform_app" {
  name             = "platform-app"
  namespace        = "platform-dev"
  create_namespace = true

  chart = "${path.module}/../helm/platform-app"

  values = [
    file("${path.module}/../helm/platform-app/values-dev.yaml")
  ]

  set = [
    {
      name  = "image.tag"
      value = "1.0.1"
    }
  ]

  wait    = true
  timeout = 180
}
