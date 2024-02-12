package test

import (
	"testing"
    
    "github.com/stretchr/testify/assert"
    "github.com/sirupsen/logrus"
	"github.com/gruntwork-io/terratest/modules/terraform"
	
)

func TestFoo(t *testing.T) {
    logrus.Info(t, "This will show up in stdout immediately")
}  

func TestTerraformAzureResources(t *testing.T) {
	terraformOptions := terraform.WithDefaultRetryableErrors(t, &terraform.Options{
		TerraformDir: "../terraform scripts",
      
	})

   

	defer terraform.Destroy(t, terraformOptions)

	terraform.InitAndApply(t, terraformOptions)

	// Retrieve the outputs of the Terraform configuration
	resourceGroupName := terraform.Output(t, terraformOptions, "resource_group_name")
	acrName := terraform.Output(t, terraformOptions, "acr_name")
	aksName := terraform.Output(t, terraformOptions, "aks_name")

	// Define the expected values
	expectedResourceGroupName := "microservice-deployment-demo-tf-scripttest"
	expectedACRName := "microserviceimagestfscripttest"
	expectedAKSName := "example-aks1-tf-scripttest"

	// Compare the outputs with the expected values
	assert.Equal(t, expectedResourceGroupName, resourceGroupName, "Resource group name does not match")
	assert.Equal(t, expectedACRName, acrName, "Azure Container Registry name does not match")
	assert.Equal(t, expectedAKSName, aksName, "Azure Kubernetes Cluster name does not match")
}
