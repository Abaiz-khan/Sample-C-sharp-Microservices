using HelloService.Controllers;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Logging.Abstractions; // Import NullLogger
using NUnit.Framework;

namespace HelloService.Tests.Controllers
{
    public class HelloControllerTests
    {
        [Test]
        public void Get_ReturnsHello()
        {
            // Arrange
            var logger = NullLogger<HelloController>.Instance;
            var configuration = new ConfigurationBuilder().Build();
            var controller = new HelloController(logger, configuration);

            // Act
            IActionResult result = controller.Get();

            // Assert
            Assert.IsNotNull(result);
            var okResult = result as OkObjectResult;
            Assert.IsNotNull(okResult);
            Assert.AreEqual("Hello", okResult.Value); // Ensure the expected value is "Hello" with capital H
        }
    }
}
