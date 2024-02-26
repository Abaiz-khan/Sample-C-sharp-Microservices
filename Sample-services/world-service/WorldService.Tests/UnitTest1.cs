using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Logging.Abstractions; // Add this namespace
using NUnit.Framework;
using WorldService.Controllers; // Import the correct namespace for WorldController

namespace WorldService.Tests.Controllers
{
    public class WorldControllerTests
    {
        [Test]
        public void Get_ReturnsWorld()
        {
            // Arrange
            var configuration = new ConfigurationBuilder()
                .AddInMemoryCollection(new Dictionary<string, string>
                {
                    { "FeatureFlags:WorldFeatureEnabled", "true" } // Set the feature flag to true
                })
                .Build();

            var controller = new WorldController(new NullLogger<WorldController>(), configuration);

            // Act
            IActionResult result = controller.Get();

            // Assert
            Assert.IsNotNull(result);
            var okResult = result as OkObjectResult;
            Assert.IsNotNull(okResult);
            Assert.AreEqual("World", okResult.Value);
        }
    }
}
