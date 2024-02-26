using HelloService.Controllers;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Logging.Abstractions; // Add this namespace
using NUnit.Framework;

namespace HelloService.Tests.Controllers
{
    public class HelloControllerTests
    {
        [Test]
        public void Get_ReturnsHello()
        {
            // Arrange
            var configuration = new ConfigurationBuilder()
                .AddInMemoryCollection(new Dictionary<string, string>
                {
                    { "FeatureFlags:HelloFeatureEnabled", "true" } // Set the feature flag to true
                })
                .Build();

            var controller = new HelloController(new NullLogger<HelloController>(), configuration);

            // Act
            IActionResult result = controller.Get();

            // Assert
             Assert.IsNotNull(result);
            var okResult = result as OkObjectResult;
            Assert.IsNotNull(okResult);
            Assert.AreEqual("Hello", okResult.Value);
        }
    }
}
